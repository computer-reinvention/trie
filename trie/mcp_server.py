"""MCP server exposing the trie triefact tree + symbol graph to coding agents.

Read-only. Speaks MCP over stdio so an agent harness (Claude Code, Codex, etc.) can spawn
it as a subprocess and consult the triefact tree as context separate from its own
conversation memory.

Tools exposed:

- `get_triefact(source_path)` — return the Markdown triefact for a source file.
- `find_symbol(name)` — substring search over symbol names.
- `references_to(qualified_name)` — list inbound references (callers).
- `references_from(qualified_name)` — list outbound references (callees).

Example client wiring (Claude Code's mcp_servers config):

    {
      "trie": {
        "command": "trie",
        "args": ["mcp"],
        "cwd": "/path/to/project"
      }
    }
"""

from __future__ import annotations

from dataclasses import asdict
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP

from trie.config import Config
from trie.graph.store import Store


class TrieTools:
    """The four MCP tools as plain methods, so they can be tested without the transport.

    Owns the Store for the lifetime of the surrounding server process.
    """

    def __init__(self, project_root: Path) -> None:
        self.config, self.root = Config.find_and_load(project_root)
        self.triefacts_root = self.root / self.config.triefacts.root
        self.src_root = (self.root / self.config.triefacts.source_root).resolve()
        self.store = Store(self.root / ".trie" / "graph.db")

    def close(self) -> None:
        self.store.close()

    def get_triefact(self, source_path: str) -> str:
        """Return the Markdown triefact for a source file.

        `source_path` should be source-root-relative (e.g. `src/foo.py`). If the agent
        passed a `.md` path, it's used as-is. If no triefact exists, returns a notice the
        agent can use as a fallback signal.
        """
        rel = Path(source_path)
        triefact_rel = rel if rel.suffix == ".md" else rel.with_suffix(".md")
        triefact_path = self.triefacts_root / triefact_rel
        if not triefact_path.exists():
            return f"No trie triefact for {source_path}. Run `trie sync` to generate one."
        return triefact_path.read_text()

    def find_symbol(self, name: str, limit: int = 50) -> list[dict[str, Any]]:
        """Substring search over symbol names (the local part, not qname).

        Public symbols come first. Use to narrow before calling `get_triefact` when the
        agent has a name but not a file.
        """
        hits = self.store.search_symbols(name, limit=limit)
        return [asdict(h) for h in hits]

    def references_to(self, qualified_name: str) -> list[dict[str, Any]]:
        """Return symbols that reference `qualified_name`.

        Each result: `{src_qname, file_path, confidence}`. Confidence labels:
        `tree_sitter_import` (precise, from an explicit import), `name_match` (heuristic,
        may over-match within a module).
        """
        rows = self.store.references_in_with_files(qualified_name)
        return [{"src_qname": s, "file_path": f, "confidence": c} for s, f, c in rows]

    def references_from(self, qualified_name: str) -> list[dict[str, Any]]:
        """Return symbols that `qualified_name` references."""
        rows = self.store.references_out(qualified_name)
        return [{"target_qname": t, "confidence": c} for t, c in rows]


def build_server(project_root: Path) -> tuple[FastMCP, TrieTools]:
    """Construct an MCP server bound to the trie state under `project_root`.

    Returns the server and the underlying TrieTools instance — the latter is exposed so
    tests can call tool methods directly without driving the MCP transport.
    """
    tools = TrieTools(project_root)
    server = FastMCP("trie")
    server.tool()(tools.get_triefact)
    server.tool()(tools.find_symbol)
    server.tool()(tools.references_to)
    server.tool()(tools.references_from)
    return server, tools


def run_stdio(project_root: Path) -> None:
    """Run the MCP server over stdio. Blocks until the parent closes the pipe."""
    server, _tools = build_server(project_root)
    server.run()
