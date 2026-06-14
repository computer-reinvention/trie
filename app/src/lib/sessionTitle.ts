// Session title + recency helpers for the agent panel session switcher.
//
// Reconstructed to satisfy the imports in AgentPanel / useSessions / agentStore.
// opencode auto-names new chats with a placeholder until the model generates a
// real title; these helpers decide what to show and how to order/hide chats.

import type { OpencodeSession } from "@/api/types"

// Placeholder titles opencode assigns before a real one is generated. A session
// with one of these (or no title) is "default" — hidden from the switcher until
// it has real content, and shown as a generic label when active.
const DEFAULT_TITLE_PATTERNS = [/^new session$/i, /^untitled$/i, /^trie desktop$/i, /^chat$/i]

export function isDefaultTitle(title?: string): boolean {
  const t = (title ?? "").trim()
  if (t === "") return true
  return DEFAULT_TITLE_PATTERNS.some((re) => re.test(t))
}

// Human-facing title for a session: the real title, or a generic fallback.
export function displayTitle(info: OpencodeSession | undefined | null): string {
  const t = (info?.title ?? "").trim()
  return t && !isDefaultTitle(t) ? t : "New chat"
}

// Best-available "last activity" timestamp (ms) for a session. Defensive: some
// session-info objects arrive without a `time` block.
export function updatedAt(info: OpencodeSession | undefined | null): number {
  if (!info) return 0
  return info.time?.updated ?? info.time?.created ?? 0
}

// Sort comparator: most-recently-active first. Accepts either a bare
// OpencodeSession or a session-state wrapper carrying `.info` — both call shapes
// exist (agentStore sorts sessions; useSessions sorts state items).
type SessionLike = OpencodeSession | { info?: OpencodeSession } | undefined | null

function infoOf(x: SessionLike): OpencodeSession | undefined {
  if (!x) return undefined
  const wrapped = (x as { info?: OpencodeSession }).info
  if (wrapped) return wrapped
  // a bare OpencodeSession has an `id`; treat it as the info itself
  if (typeof (x as OpencodeSession).id === "string") return x as OpencodeSession
  return undefined
}

export function byRecency(a: SessionLike, b: SessionLike): number {
  return updatedAt(infoOf(b)) - updatedAt(infoOf(a))
}

// Compact relative-time label ("just now", "2m", "3h", "5d") from a ms timestamp.
export function relativeTime(ts: number): string {
  if (!ts) return ""
  const seconds = Math.max(0, (Date.now() - ts) / 1000)
  if (seconds < 45) return "just now"
  const minutes = seconds / 60
  if (minutes < 60) return `${Math.round(minutes)}m`
  const hours = minutes / 60
  if (hours < 24) return `${Math.round(hours)}h`
  const days = hours / 24
  if (days < 7) return `${Math.round(days)}d`
  const weeks = days / 7
  return `${Math.round(weeks)}w`
}
