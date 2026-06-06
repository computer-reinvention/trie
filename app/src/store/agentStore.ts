import { create } from "zustand"
import type {
  OpencodeMessage,
  OpencodeMessageInfo,
  OpencodePart,
  OpencodeSession,
  PermissionRequest,
} from "@/api/types"

// The agent store models a real, multi-session opencode conversation.
//
// Each session has an ordered list of messages; each message is { info, parts }
// exactly as opencode returns them, so the transcript renders the true model
// (user/assistant, text, reasoning, tool calls with live status). Live SSE
// updates (part upserts, text deltas, message-info upserts) and bulk history
// loads both flow through the same reducers, keyed by message id / part id.
//
// Permissions live per-session keyed by request id and are correlated to their
// tool call via callID so the UI can render approve/deny inline on the row.

export interface SessionState {
  info: OpencodeSession
  messages: OpencodeMessage[]
  permissions: Record<string, PermissionRequest>
  running: boolean
  error: string | null
  loaded: boolean // history fetched at least once
}

interface AgentStore {
  sessions: Record<string, SessionState>
  order: string[] // session ids, most-recent first
  activeId: string | null

  // session lifecycle
  setSessions: (list: OpencodeSession[]) => void
  upsertSession: (info: OpencodeSession) => void
  removeSession: (id: string) => void
  setActive: (id: string | null) => void
  setMessages: (id: string, messages: OpencodeMessage[]) => void

  // live transcript updates (from SSE)
  applyPartUpdated: (sessionID: string, messageID: string, part: OpencodePart) => void
  applyTextDelta: (sessionID: string, messageID: string, partID: string, delta: string) => void
  applyReasoningDelta: (sessionID: string, messageID: string, partID: string, delta: string) => void
  applyMessageInfo: (sessionID: string, info: OpencodeMessageInfo) => void

  // turn status
  setRunning: (id: string, running: boolean) => void
  setError: (id: string, error: string | null) => void

  // optimistic user message (before the server echoes it)
  appendLocalUser: (id: string, text: string) => void

  // permissions
  addPermission: (req: PermissionRequest) => void
  removePermission: (sessionID: string, requestID: string) => void
}

function emptySession(info: OpencodeSession): SessionState {
  return { info, messages: [], permissions: {}, running: false, error: null, loaded: false }
}

// Find/clone the part list, upserting a part by id.
function upsertPart(parts: OpencodePart[], part: OpencodePart): OpencodePart[] {
  const idx = parts.findIndex((p) => p.id === part.id)
  if (idx === -1) return [...parts, part]
  const next = [...parts]
  next[idx] = part
  return next
}

// Apply a function to one message's parts, returning a new messages array.
function patchMessageParts(
  messages: OpencodeMessage[],
  messageID: string,
  fn: (parts: OpencodePart[]) => OpencodePart[],
): OpencodeMessage[] {
  const idx = messages.findIndex((m) => m.info.id === messageID)
  if (idx === -1) return messages
  const next = [...messages]
  next[idx] = { ...next[idx], parts: fn(next[idx].parts) }
  return next
}

export const useAgentStore = create<AgentStore>((set, get) => ({
  sessions: {},
  order: [],
  activeId: null,

  setSessions: (list) =>
    set((s) => {
      const sessions = { ...s.sessions }
      for (const info of list) {
        sessions[info.id] = sessions[info.id]
          ? { ...sessions[info.id], info }
          : emptySession(info)
      }
      const order = list.map((i) => i.id)
      const activeId = s.activeId && sessions[s.activeId] ? s.activeId : (order[0] ?? null)
      return { sessions, order, activeId }
    }),

  upsertSession: (info) =>
    set((s) => {
      const exists = !!s.sessions[info.id]
      const sessions = {
        ...s.sessions,
        [info.id]: s.sessions[info.id] ? { ...s.sessions[info.id], info } : emptySession(info),
      }
      const order = exists ? s.order : [info.id, ...s.order]
      return { sessions, order, activeId: s.activeId ?? info.id }
    }),

  removeSession: (id) =>
    set((s) => {
      const sessions = { ...s.sessions }
      delete sessions[id]
      const order = s.order.filter((x) => x !== id)
      const activeId = s.activeId === id ? (order[0] ?? null) : s.activeId
      return { sessions, order, activeId }
    }),

  setActive: (id) => set({ activeId: id }),

  setMessages: (id, messages) =>
    set((s) => {
      const cur = s.sessions[id]
      if (!cur) return {}
      return { sessions: { ...s.sessions, [id]: { ...cur, messages, loaded: true } } }
    }),

  applyPartUpdated: (sessionID, messageID, part) =>
    set((s) => {
      const cur = s.sessions[sessionID]
      if (!cur) return {}
      // Ensure the message exists (assistant message may arrive via info first,
      // but if a part lands before info, create a stub assistant message).
      let messages = cur.messages
      if (!messages.some((m) => m.info.id === messageID)) {
        messages = [
          ...messages,
          {
            info: { id: messageID, sessionID, role: "assistant", time: { created: Date.now() } },
            parts: [],
          },
        ]
      }
      messages = patchMessageParts(messages, messageID, (parts) => upsertPart(parts, part))
      return { sessions: { ...s.sessions, [sessionID]: { ...cur, messages } } }
    }),

  applyTextDelta: (sessionID, messageID, partID, delta) =>
    set((s) => {
      const cur = s.sessions[sessionID]
      if (!cur) return {}
      const messages = patchMessageParts(cur.messages, messageID, (parts) => {
        const idx = parts.findIndex((p) => p.id === partID)
        if (idx === -1) {
          return [...parts, { id: partID, type: "text", text: delta } as OpencodePart]
        }
        const p = parts[idx]
        if (p.type !== "text") return parts
        const next = [...parts]
        next[idx] = { ...p, text: p.text + delta }
        return next
      })
      return { sessions: { ...s.sessions, [sessionID]: { ...cur, messages } } }
    }),

  applyReasoningDelta: (sessionID, messageID, partID, delta) =>
    set((s) => {
      const cur = s.sessions[sessionID]
      if (!cur) return {}
      const messages = patchMessageParts(cur.messages, messageID, (parts) => {
        const idx = parts.findIndex((p) => p.id === partID)
        if (idx === -1) {
          return [...parts, { id: partID, type: "reasoning", text: delta } as OpencodePart]
        }
        const p = parts[idx]
        if (p.type !== "reasoning") return parts
        const next = [...parts]
        next[idx] = { ...p, text: p.text + delta }
        return next
      })
      return { sessions: { ...s.sessions, [sessionID]: { ...cur, messages } } }
    }),

  applyMessageInfo: (sessionID, info) =>
    set((s) => {
      const cur = s.sessions[sessionID]
      if (!cur) return {}
      // When the server echoes a real user message, drop our optimistic local
      // stub(s) so the message isn't shown twice.
      let base = cur.messages
      if (info.role === "user") {
        base = base.filter((m) => !(m.info.role === "user" && m.info.id.startsWith("local-")))
      }
      const idx = base.findIndex((m) => m.info.id === info.id)
      let messages: OpencodeMessage[]
      if (idx === -1) {
        messages = [...base, { info, parts: [] }]
      } else {
        messages = [...base]
        messages[idx] = { ...messages[idx], info }
      }
      return { sessions: { ...s.sessions, [sessionID]: { ...cur, messages } } }
    }),

  setRunning: (id, running) =>
    set((s) => {
      const cur = s.sessions[id]
      if (!cur) return {}
      return {
        sessions: { ...s.sessions, [id]: { ...cur, running, error: running ? null : cur.error } },
      }
    }),

  setError: (id, error) =>
    set((s) => {
      const cur = s.sessions[id]
      if (!cur) return {}
      return { sessions: { ...s.sessions, [id]: { ...cur, error, running: false } } }
    }),

  appendLocalUser: (id, text) =>
    set((s) => {
      const cur = s.sessions[id]
      if (!cur) return {}
      const localId = `local-${crypto.randomUUID()}`
      const msg: OpencodeMessage = {
        info: { id: localId, sessionID: id, role: "user", time: { created: Date.now() } },
        parts: [{ id: `${localId}-text`, type: "text", text }],
      }
      return {
        sessions: { ...s.sessions, [id]: { ...cur, messages: [...cur.messages, msg], running: true } },
      }
    }),

  addPermission: (req) =>
    set((s) => {
      const cur = s.sessions[req.sessionID]
      if (!cur) return {}
      return {
        sessions: {
          ...s.sessions,
          [req.sessionID]: { ...cur, permissions: { ...cur.permissions, [req.id]: req } },
        },
      }
    }),

  removePermission: (sessionID, requestID) =>
    set((s) => {
      const cur = s.sessions[sessionID]
      if (!cur) return {}
      const permissions = { ...cur.permissions }
      delete permissions[requestID]
      return { sessions: { ...s.sessions, [sessionID]: { ...cur, permissions } } }
    }),
}))

// Selector helper: the active session state (or null).
export function useActiveSession(): SessionState | null {
  return useAgentStore((s) => (s.activeId ? (s.sessions[s.activeId] ?? null) : null))
}
