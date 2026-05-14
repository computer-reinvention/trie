# Validating trie

Notes on how we decide whether trie is worth continuing to build, what to measure,
and — first — what has to be true about the product before any of those measurements
are meaningful.

> **TL;DR.** trie makes four distinct value claims. The riskiest is _agents do
> better work with triefacts than without_. We can't test that until the MCP /
> CLI surface is good enough for an agent to actually drive trie on its own. So
> the order of operations is **agent-readiness first, validation second.** If
> validation comes back flat, we shelf.

---

## The four claims trie makes

trie is doing four things, and each needs its own kill criterion. A metric that
proves one tells you nothing about the others.

| # | Claim | Side it serves |
| - | --- | --- |
| 1 | Agents do better work when reading triefacts than when reading code. | agent |
| 2 | Humans review faster / catch more when reviewing prose diffs than code diffs. | human |
| 3 | The cascade actually keeps prose in sync; drift stays bounded. | integrity |
| 4 | The maintenance cost of triefacts is less than the value they return. | economics |

Most likely failure mode if we don't pick these apart: cascade works, `trie
verify` holds the line, every offline number looks great — and **no agent gets
measurably better, no human reviews faster**. That's a very correct system
nobody needs. Claims 1 and 2 are load-bearing. 3 and 4 are necessary but not
sufficient.

---

## The elephant: agent-readiness comes first

There is no point running an A/B on "agent with trie" vs. "agent without trie"
if the agent can't fluently use trie. Garbage in, garbage out — the test
would measure the awkwardness of the surface, not the value of the underlying
artifact.

So the gate before validation is: **can a coding agent, given only the MCP
server and the CLI, drive trie end-to-end on a real task without us holding
its hand?**

### What "agent-ready" means concretely

The agent must be able to, unprompted, in a normal session:

1. **Discover** that trie exists in the project and what it offers.
2. **Read** the triefact tree at a useful granularity (file, symbol, neighbourhood).
3. **Navigate** the graph (callers / callees / "what does this thing connect to").
4. **Trust** the artifact — meaning it knows when the artifact is stale, missing,
   or untrustworthy, and falls back to code gracefully in those cases.
5. **Trigger writes** indirectly — not by writing triefacts itself (that's `trie
   sync`, which is gated by humans by design), but by knowing _when to suggest
   the human run `trie sync`_, and being able to verify drift state itself.

Each of those maps to either a missing capability or a sharp edge in the current
surface. The gaps are the work.

### Audit of the current surface

**MCP tools today** (`trie/mcp_server.py`):

| Tool | Status | Gap |
| --- | --- | --- |
| `get_triefact(source_path)` | shipped | Returns the entire Markdown file. No way to ask for a single symbol's section without parsing the whole thing. Agent burns tokens. |
| `find_symbol(name)` | shipped | Substring match only. No kind filter (function/class/method), no public-only filter. Returns up to 50 — no pagination, no ranking signal beyond `is_public`. |
| `references_to(qualified_name)` | shipped | Returns the raw edge list with a `confidence` field but no triefact-side context (what does the caller _do_?). Agent has to make a second call per result. |
| `references_from(qualified_name)` | shipped | Same — edge list with no narrative join. |

**Things the agent will want and we don't expose:**

- `get_section(qualified_name)` — fetch a single section by symbol, not a whole
  file. This is the right granularity for graph-walk-then-read patterns.
- `neighbourhood(qualified_name, depth=1)` — one round-trip to get a symbol's
  section + its callers' sections + its callees' sections, with bodies. The
  current API forces N+1 calls for the most common access pattern.
- `list_triefacts(glob)` — directory listing of what triefacts exist, so the
  agent can orient before searching.
- `drift_status()` — read-only equivalent of `trie verify`. The agent needs to
  know "is the triefact for this file currently trustworthy?" without shelling
  out. Without this, every read is implicitly "maybe stale."
- `outline(source_path)` — front-matter + section headers only, no bodies. The
  cheapest possible "is it worth opening this triefact?" check.

**CLI ergonomics that block agent fluency:**

- No structured (JSON) output mode on any command. An agent that wants to run
  `trie verify` and parse the result has to scrape human text. `--format json`
  on `verify`, `plan`, and `sync` is the minimum.
- `trie sync` is interactive on first run (asks for confirmation in a tty).
  Fine for humans, but an agent harness running it non-interactively has to
  know to pass `--limit` or `--budget`. The contract isn't documented from the
  agent's POV.
- The MCP install path is good for humans (`trie mcp install --target ...`),
  but there's no programmatic way for an agent to ask "am I currently
  registered with this project's trie?" — it has to read config files itself.

**Discoverability:**

- An agent that lands in a repo for the first time has no signal that trie is
  installed beyond noticing `triefacts/` or `trie.toml`. No system prompt, no
  conventions doc the agent reads to learn what to do with them. We need an
  `AGENTS.md`-style file (or a section in the existing one) that's written
  _for_ the agent, not for human contributors.

### The pre-validation work, ordered

1. **Section-level MCP reads** (`get_section`, `outline`). The single biggest
   token-efficiency win. Without it, the prose layer fights the context
   window instead of helping it.
2. **`neighbourhood(qname, depth)`** — collapses the common multi-call pattern
   into one round-trip with prose bodies attached. This is _the_ artifact that
   makes graph-walking cheap.
3. **`drift_status()` MCP tool + `--format json` on `trie verify`**. Agents need
   to know when not to trust a triefact. Both surfaces should return the same
   structured result.
4. **A `for-agents.md` (or section in AGENTS.md) co-located with `trie.toml`**
   that the agent is instructed to read at session start. Conventions, tool
   selection guide, failure-mode fallbacks. Without this, you're testing
   whether the agent can guess your design, not whether the design is good.
5. **JSON output on `plan`, `sync`, `verify`**. Lets an orchestrator script
   (and an eval harness) consume trie state without scraping.
6. **A `trie status` command** that summarises in one call: graph health,
   drift count, last sync time, triefact coverage %. Both for humans and as
   the JSON the agent reads at orientation.

Only after 1–4 are in place is it honest to A/B test agent quality with
vs. without trie. Items 5–6 are nice-to-haves for the eval harness itself.

---

## What we measure once agent-readiness is in

Each claim gets its own test. Don't mush them.

### Claim 1 — Agents work better with triefacts

The cleanest test: **task-paired A/B with and without the MCP server.** Same
agent, same prompt, same repo state. Two conditions: triefacts available vs.
not.

Primary metrics:

- **Task success rate** on a fixed eval set of repo questions and small
  implementation tasks. Score binary (worked / didn't) by replaying against
  tests, not by LLM-as-judge.
- **Hallucination rate** — count claims in the agent's output that are
  factually wrong about the codebase (wrong file, wrong signature, fabricated
  API). Hand-graded on a 20-task sample is enough signal.
- **Tokens-to-first-correct-answer.** Triefacts only win if the prose lets
  the agent skip grep cycles. If triefact-augmented runs consume _more_
  context than baseline (because the agent reads both prose and code), the
  abstraction is leaking.
- **Tool-call count.** Fewer `Read` / `Glob` / `Grep` calls per task is the
  operational proxy for "right abstraction." Cheap to measure; strong signal.
- **Cross-file change correctness.** Pick tasks that require touching 3+
  files. Triefacts should help most here — the graph is the whole point. If
  the lift is concentrated in single-file tasks, the cascade isn't earning
  its keep.

**Kill criterion:** < 15% lift on success rate at > 5% confidence over 50
tasks, **or** token cost goes up with no quality gain.

**Strong-form test (do this if the weak form passes):** compare not against
"naked grep" but against a credible baseline — Serena MCP, Cursor with
semantic indexing, aider's repo-map. If we only beat the no-tools baseline,
we've proven nothing the market doesn't already know. The question is
whether prose plateaus _higher_ than smarter code-reading, not whether it's
better than nothing.

### Claim 2 — Humans review faster

- **Time-to-decide on a PR.** Two conditions: reviewer sees the code diff
  only, vs. code diff + triefact diff. Stopwatch from PR open to
  approve/reject. Same PR set, randomised reviewer assignment.
- **Defect catch rate.** Seed PRs with known bugs (logic errors that touch
  reachable callers). Measure caught/missed by condition. This is the
  headline number for the human bet.
- **Subjective: "did you understand the scope of this change?"** 1–5 scale.
  Soft, but cheap.
- **Triefact-diff-only review viability** — can a reviewer who reads _only_
  the prose diff catch the same bugs as one reading the code? If yes,
  we've proven the strong form. If no, prose is supplementary, which is
  fine but reframes the pitch.

**Kill criterion:** no measurable defect-catch improvement on seeded PRs
across ≥ 10 reviewers × ≥ 20 PRs.

### Claim 3 — Cascade integrity

Easiest to measure and most likely to look good. Be skeptical of yourself
here — a green dashboard on (3) is not permission to skip (1) and (2).

- **Drift incidents per N commits in production use.** Run trie on 3–5 real
  repos for a month. How often does `trie verify` fire? How often does it
  fire _correctly_ (a real semantic change) vs. spuriously (formatting,
  comments, a real refactor that didn't change behaviour)?
- **Cascade precision / recall.** When a symbol changes, did the cascade
  pick exactly the right downstream triefacts? Ground truth by manual audit
  on a sample. The tree-sitter heuristic _will_ have false negatives —
  quantify them, because that's the case for v0.2 SCIP precision.
- **Hub-skip damage.** How often does the 20-inbound-ref cap silently miss
  a real propagation? Pick 20 cascade events through hub symbols, audit
  which dropped downstream triefacts genuinely should have regenerated.
- **Time-to-resync on a typical PR.** Median seconds for `trie sync` on a
  5-file change. If it's > 2 minutes, friction kills adoption regardless
  of value.
- **Verify wall time.** Has to be < 5s on a 100 kloc repo, or it can't be
  a pre-commit hook in practice.

**Kill criterion:** cascade precision < 80% _or_ recall < 90% on real-world
edits (not synthetic). The asymmetry is intentional: false positives waste
tokens; false negatives erode trust, which is fatal.

### Claim 4 — Economics

- **$ per kloc to bootstrap** at current Sonnet pricing on real repos.
  Intuition: under $20 for a 50 kloc Python repo, or this is dead.
- **$ per sync on an average PR.** Day-two cost. Must round to "lunch money"
  or developers won't run it.
- **Triefact-prose half-life.** How often does a generated section get
  hand-edited within a week? High edit rate means the LLM output isn't
  trusted, and the real value is the human edit — at which point why
  bother with the LLM step?
- **Sentinel preservation correctness.** Zero tolerance. Any case where regen
  clobbers human prose is a catastrophic bug. Track incidents; treat as
  P0 if any occur in production use.

### Cross-cutting / leading indicators

- **Triefact read frequency by agents in real sessions.** Instrument the MCP
  server. If agents call `get_triefact` (or its section-level successor)
  < 1× per task on average, they're not using the artifact regardless of
  what we think.
- **Which MCP tool wins?** If 90% of calls are `find_symbol` and almost
  none are `references_to/from`, the graph isn't the value — the symbol
  index is, and we've over-built. That would suggest pivoting to a
  lighter-weight "smart symbol search" product.
- **Triefact open rate by humans.** Are reviewers actually clicking into
  triefact diffs in PRs, or are they collapsed-and-ignored? Cheap to
  measure via the GitHub API.

---

## The plan

**Phase 0 — Agent-readiness (now).**
Build the six items in _The pre-validation work, ordered_ above. Dogfood on
trie's own repo: drive trie from an agent session and notice every friction
point. Each fix lands as a small PR.

**Phase 1 — Instrumentation.**
Add MCP server call-count logging (off by default, opt-in via env var) and
a `--format json` mode on `verify`, `plan`, `sync`. Build the eval harness
shell — a script that runs a task set under two conditions and dumps
structured results.

**Phase 2 — One-week kill-or-ship signal.**
In order of risk:

1. **Agent A/B on a 30-task eval set** against this repo and one other
   Python repo we know well. Headline number: task success rate delta.
   Tests claim 1 — the riskiest. If it fails, the others don't matter.
2. **MCP server call counts** in dogfood sessions. Free signal on whether
   the artifact is being used at all.
3. **Cascade precision / recall audit on 50 real commits** from any active
   repo. Tells us whether v0.2 SCIP precision is mandatory or marginal.
4. **Seed 10 PRs with bugs and run a small human study** (even N = 3
   reviewers). Rough signal on claim 2. If defects-caught looks flat,
   shelf or pivot before investing further in the human-review pitch.

Skip the economics deep-dive until 1 and 4 are positive. Cost only matters
if value is established.

**Phase 3 — Decide.**
Greenlight = both (1) and (2) show positive lift against a credible
baseline, with cascade precision/recall above threshold. Anything short of
that, shelf. We are not in the business of building a correct system nobody
needs.

---

## Shelf criteria

We commit to shelving if any of these hold after we have real data:

**The prose is too generated.** If 50% of generated sections get
hand-rewritten within a week, the LLM is adding friction, not value.
The half-life of generated prose is the real test of whether this works.

**Drift compounds despite the cascade.** If `trie verify` fires
constantly on real refactors, or worse, misses real drift and the tree
silently rots, trust collapses and the system becomes worse than nothing.
Bidirectional drift detection is load-bearing.

**Agents don't change their behaviour.** If, given the MCP server, agents
keep grepping anyway — because the prose surface is awkward, or because
their training is too biased toward code-reading — Ring 1 never lands and
Ring 2 is impossible.

**Humans don't change their behaviour.** If reviewers ignore the prose
diff and only look at the code diff, Ring 3 never lands. The prose layer
becomes a parallel artifact nobody trusts, which is the fate of every
"living documentation" attempt before this one.

**Ring 1 lands but Ring 2 doesn't.** We become "another MCP server" in a
crowded market. Useful, but commodity. The most likely failure mode and
the one to watch for hardest.

**Prose is good but unnecessary.** The single biggest risk that isn't a
specific metric. Agents are getting better at reading code directly;
context windows are growing; tooling like Serena and aider does
graph-aware code reading without the prose artifact. trie's bet is that
the prose layer is _qualitatively_ different from "smarter code reading,"
not quantitatively better at the same thing. The metric that answers it:
**does triefact-augmented agent quality plateau higher than
code-reading-with-better-tools?** That's the strong-form test in claim 1.
Beating the no-tools baseline proves nothing the market doesn't already
know.

The distinction we hold ourselves to: **"trie works"** (Ring 1) vs.
**"trie matters"** (Rings 2 and 3). The first is easy to demonstrate
and not enough. The second is the near-term bet. Ring 4 is not something
we will validate in the next year; it's the direction the architecture
has to remain consistent with, and the reason we won't compromise the
substrate to win Ring 1 faster.
