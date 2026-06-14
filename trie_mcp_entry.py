"""
PyInstaller entrypoint for the trie MCP stdio server.
Usage: trie-mcp <project-dir>
"""

from __future__ import annotations

import sys
from pathlib import Path


def main() -> None:
    if len(sys.argv) < 2:
        print("usage: trie-mcp <project-dir>", file=sys.stderr)
        sys.exit(1)

    project_root = Path(sys.argv[1]).resolve()
    if not project_root.exists():
        print(f"error: project directory does not exist: {project_root}", file=sys.stderr)
        sys.exit(1)

    from trie.mcp_server import run_stdio

    run_stdio(project_root)


if __name__ == "__main__":
    main()
