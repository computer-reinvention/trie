# trie

A documentation tree that mirrors your source tree — kept coherent with the code by an LSP/SCIP-aware cascade and a pre-commit invariant. Exposed to coding agents (Claude Code, Codex, etc.) via MCP as a persistent, shared, versioned context layer.

## Status

Pre-alpha. v0.1 in active development. Not ready for use yet.

## The wedge

When you edit a symbol, trie's reference graph determines which *other* doc files also need regenerating — not just the doc for the file you edited. That cascade, plus a pre-commit check that the doc tree is coherent at every commit, is what trie does that nothing else does.

## Roadmap

- **M1** — `trie sync --file <path>` end-to-end on one file
- **M2** — bootstrap a whole repo
- **M3** — `trie check` for pre-commit
- **M4** — SCIP integration + cascade *(the wedge)*
- **M5** — MCP server
- **M6** — polish

See [the v0.1 plan](https://github.com/pankajgarkoti/trie) for details.

## License

MIT — see [LICENSE](./LICENSE).
