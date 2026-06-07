// HTTP client for opencode session + permission operations.
// Routes through the IPC proxy — the renderer cannot reach 127.0.0.1 directly.
//
// Shapes mirror the real opencode server contracts (verified against
// packages/opencode/src/server/routes/instance/httpapi):
//   - prompt:      POST /session/:id/message   body { parts:[{type:"text",text}], model?, agent? }
//   - history:     GET  /session/:id/message   -> MessageV2.WithParts[]   (bare array)
//   - list:        GET  /session              -> Session.Info[]
//   - create:      POST /session              body { title? }
//   - abort:       POST /session/:id/abort
//   - perm reply:  POST /permission/:requestID/reply   body { reply, message? }
//   - perm list:   GET  /permission          -> Permission.Request[]

import type { OpencodeMessage, OpencodeSession, PermissionRequest, PermissionReply } from "./types"

let baseUrl = ""

export function setOpenCodeClientBase(opencodePort: number): void {
  baseUrl = `http://127.0.0.1:${opencodePort}`
}

// eslint-disable-next-line @typescript-eslint/no-explicit-any
const trie = () => (window as any).trie

async function req<T>(
  method: string,
  path: string,
  body?: unknown,
): Promise<{ status: number; data: T | null }> {
  const result = (await trie().httpRequest({
    method,
    url: `${baseUrl}${path}`,
    ...(body !== undefined ? { body: JSON.stringify(body) } : {}),
  })) as { status: number; body: string }
  let data: T | null = null
  if (result.body) {
    try {
      data = JSON.parse(result.body) as T
    } catch {
      data = null
    }
  }
  return { status: result.status, data }
}

export const opencodeClient = {
  // --- sessions ----------------------------------------------------------

  async listSessions(): Promise<OpencodeSession[]> {
    const { data } = await req<OpencodeSession[]>("GET", "/session?scope=project")
    return Array.isArray(data) ? data : []
  },

  async createSession(title?: string): Promise<OpencodeSession | null> {
    const { data } = await req<OpencodeSession>("POST", "/session", title ? { title } : {})
    return data
  },

  async deleteSession(sessionId: string): Promise<void> {
    await req("DELETE", `/session/${sessionId}`)
  },

  async renameSession(sessionId: string, title: string): Promise<void> {
    await req("PATCH", `/session/${sessionId}`, { title })
  },

  // --- messages ----------------------------------------------------------

  // Send a user message. Returns immediately-ish; the streamed assistant
  // response arrives over the desktop SSE stream (parts/deltas).
  async sendMessage(
    sessionId: string,
    text: string,
    opts?: { model?: { providerID: string; modelID: string }; agent?: string },
  ): Promise<void> {
    await req("POST", `/session/${sessionId}/message`, {
      parts: [{ type: "text", text }],
      ...(opts?.model ? { model: opts.model } : {}),
      ...(opts?.agent ? { agent: opts.agent } : {}),
    })
  },

  // Full transcript for a session (bare array of WithParts).
  async getMessages(sessionId: string): Promise<OpencodeMessage[]> {
    const { data } = await req<OpencodeMessage[]>("GET", `/session/${sessionId}/message`)
    return Array.isArray(data) ? data : []
  },

  // Cheap "has any messages?" probe (limit=1) for pruning empty stub sessions.
  async hasMessages(sessionId: string): Promise<boolean> {
    const { data } = await req<OpencodeMessage[]>("GET", `/session/${sessionId}/message?limit=1`)
    return Array.isArray(data) && data.length > 0
  },

  // Stop a running turn.
  async abort(sessionId: string): Promise<void> {
    await req("POST", `/session/${sessionId}/abort`)
  },

  // --- permissions -------------------------------------------------------

  async replyPermission(
    requestId: string,
    reply: PermissionReply,
    message?: string,
  ): Promise<void> {
    await req("POST", `/permission/${requestId}/reply`, {
      reply,
      ...(message ? { message } : {}),
    })
  },

  async listPermissions(): Promise<PermissionRequest[]> {
    const { data } = await req<PermissionRequest[]>("GET", "/permission")
    return Array.isArray(data) ? data : []
  },
}
