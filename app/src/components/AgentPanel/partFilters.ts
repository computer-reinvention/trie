import type { OpencodePart, TextPart } from "@/api/types"

// Server-injected text parts that are NOT real conversation content and must
// never render in the transcript (main OR sub-agent):
//   - `ignored`   — excluded from model input
//   - `synthetic` — system plumbing (plan→build notice, file-mention expansions,
//                   prompt-cache markers, task-result injections, …)
//   - `<system-reminder>` — raw reminder plumbing (defensive: even if the flags
//                   above are absent on the part)
// Leaking these is how prompt-cache / system artifacts surfaced in the panel.
export function isHiddenText(p: OpencodePart): boolean {
  if (p.type !== "text") return false
  const tp = p as TextPart
  if (tp.ignored || tp.synthetic) return true
  return tp.text.trimStart().startsWith("<system-reminder>")
}

// A renderable transcript part: a tool call, or a real (non-hidden, non-empty)
// text part. Used to flatten a message's parts for display.
export function isRenderablePart(p: OpencodePart): boolean {
  if (p.type === "tool") return true
  if (p.type === "text") return !isHiddenText(p) && (p as TextPart).text.trim().length > 0
  return false
}
