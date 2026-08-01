# <img src="landing/logo.svg" width="28" alt="trie logo" /> trie

> **A self-hosted index of meaning and intent for your codebase.**

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Status: pre-alpha](https://img.shields.io/badge/status-pre--alpha-orange.svg)](https://computerreinvention.com/trie/docs.html)

**[Website](https://computerreinvention.com/trie/)** · **[Documentation](https://computerreinvention.com/trie/docs.html)**

---

Every coding agent's session starts by re-deriving context: _what does this code do, and why is it like this?_ The code answers the first question bit-by-bit and the second not at all. Commit messages describe diffs, not decisions; documentation rots because nothing stops it from rotting. Symbol-level intent lives in the programmer's head or between an agent's conversation turns — and is lost either way.

_trie_ makes this context explicit and permanent by creating and maintaining two separate indexes within your codebase.

- **The Index of Meaning** (`triefacts`) — one Markdown file per source file, one section per symbol, describing what each thing does. LLM-generated, regenerated only when the source actually changes, cascade-aware, and verified at commit time. Entries in a triefact file have the same graph dependency as the actual source code.

- **The Index of Intent** (`triediffs`) — the reason each symbol changed, recorded when the change is made and enforced at commit time. Archived per commit as a _triediff_ that shows up in your PRs. Months later, `trie read <symbol> --history` tells you the actual why. Also makes for a very nice and readable summary at PR time. Reduces review pressure drastically.

![An agent investigates a bug, fixes it, and is gated until it records the discovered cause; without trie that knowledge is lost; months later another agent answers the why-question from the recorded intent](https://raw.githubusercontent.com/computer-reinvention/trie/main/landing/demo.gif)

## Quickstart

Requires **Python 3.11+**, [`uv`](https://docs.astral.sh/uv/), and [`ripgrep`](https://github.com/BurntSushi/ripgrep) on PATH, plus an Anthropic API key in `ANTHROPIC_API_KEY` for prose generation (the gates, graph, and queries run offline).

```bash
uv tool install git+https://github.com/computer-reinvention/trie

cd /path/to/your/project
export ANTHROPIC_API_KEY=...
trie init      # writes trie.toml, scans the symbol graph
trie setup     # wire up your coding agent (auto-detects opencode / claude-code / cursor / ...)
trie sync      # generate the meaning index
```

That's the loop: `init` → `setup` → edit → `trie sync` before each commit. A pre-commit hook will make sure the agent always records intent with `trie patch` for each symbol. The coding agent has to follow this structure by design - it can't commit otherwise.

`trie setup` will override your agent's default `grep` with `trie grep` which is backed by the meaning and intent index - ~3.5 less round-trips. It will also add tools that invoke `trie read` and `trie trace` which utilize graph semantics over triefacts to one-shot the same questions that take a non-augmented agent many reads and greps.

## Documentation

To learn more about how each index works, the commit gate, agent integration details, the command reference, configuration, costs, CI, team adoption, and troubleshooting check out the docs at **[computerreinvention.com/trie/docs.html](https://computerreinvention.com/trie/docs.html)**.

## License

MIT. See [LICENSE](LICENSE).
Contributions welcome — issues, discussions, PRs. For large changes, open an issue first so we can talk through the design.
