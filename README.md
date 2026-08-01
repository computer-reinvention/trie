# <img src="landing/logo.svg" width="28" alt="trie logo" /> trie

> **An index of meaning and intent for your codebase.**

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Status: pre-alpha](https://img.shields.io/badge/status-pre--alpha-orange.svg)](https://computerreinvention.com/trie/docs.html)

**[Website](https://computerreinvention.com/trie/)** · **[Documentation](https://computerreinvention.com/trie/docs.html)**

---

Every coding agent's session starts by re-deriving context: _what does this code do, and why is it like this?_ The code answers the first question bit-by-bit and the second not at all. Commit messages describe diffs, not decisions; documentation rots because nothing stops it from rotting. Symbol-level intent lives in the programmer's head or between an agent's conversation turns — and is lost either way.

trie fixes both, in the repo, with the mechanism your code already trusts: version control and a pre-commit gate. It keeps two indexes in sync with your source in real time:

- **Meaning** (`triefacts/`) — one Markdown file per source file, one section per symbol, describing what each thing does. LLM-generated, regenerated only when the source actually changes, cascade-aware, and verified at commit time.
- **Intent** (`triefacts/triediffs/`) — the reason each symbol changed, recorded when the change is made and enforced at commit time. Archived per commit as a _triediff_ that shows up in your PRs. Months later, `trie read <symbol> --history` tells you the actual why.

trie never writes your code. You (or your agent) own every change; trie owns the record of what it means and why it happened. No server, no hosted index — if you can clone the repo, you have all of it.

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

That's the loop: `init` → `setup` → edit → `trie sync` before each commit. The [full quickstart](https://computerreinvention.com/trie/docs.html#quickstart) covers cost previews, capped first runs, and the day-to-day cycle.

## Documentation

Everything else — how each index works, the commit gate, agent integration, the command reference, configuration, costs, CI, team adoption, and troubleshooting — lives at **[computerreinvention.com/trie/docs.html](https://computerreinvention.com/trie/docs.html)**.

## License

MIT. See [LICENSE](LICENSE). Contributions welcome — issues, discussions, PRs. For large changes, open an issue first so we can talk through the design.
