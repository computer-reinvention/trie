// Shared tool → attention classification, mirroring trie/attention.py.
// Used by both the live SSE ingest (Phase 4) and any client-side recorder, so
// there is a single source of truth for "what kind of attention is this tool".

import type { AttentionEventType, SyntheticNode } from "@/api/types"
import { syntheticQname } from "@/api/types"

const TOOL_EVENT_TYPE: Record<string, AttentionEventType | null> = {
  read: "read",
  read_source: "read",
  explain_symbol: "read",
  explain_symbol_references: "read",
  trace: "trace",
  trace_flow: "trace",
  explain_flow: "trace",
  grep: "grep",
  grep_str: "grep",
  grep_str_all: "grep",
  grep_symbol: "grep",
  grep_entry_points: "grep",
  grep_symbol_and_neighbours: "grep",
  find_files: "grep",
  patch: "write",
  create_symbol: "write",
  rename_symbol: "write",
  delete_symbol: "write",
  write_file: "write",
  commit: "write",
  patch_apply: "write",
  // non-trie file-edit tools an agent harness may expose
  edit: "write",
  write: "write",
  str_replace_editor: "write",
}

const TOOL_SYNTHETIC_NODE: Record<string, SyntheticNode> = {
  read_source: "Filesystem",
  write_file: "Filesystem",
  find_files: "Filesystem",
  grep_str_all: "Filesystem",
  // common non-trie surfaces
  bash: "Bash",
  shell: "Bash",
  webfetch: "Web",
  fetch: "Web",
}

function bare(tool: string): string {
  return tool.startsWith("trie_") ? tool.slice(5) : tool
}

export function classifyTool(tool: string): AttentionEventType | null {
  return TOOL_EVENT_TYPE[bare(tool)] ?? null
}

export function classifySynthetic(tool: string): SyntheticNode | null {
  return TOOL_SYNTHETIC_NODE[bare(tool)] ?? null
}

// Synthetic qname for a tool that targets a non-code surface, or null.
export function syntheticTarget(tool: string): string | null {
  const node = classifySynthetic(tool)
  return node ? syntheticQname(node) : null
}
