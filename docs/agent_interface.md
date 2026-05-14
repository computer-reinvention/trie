# The agent interface

The MCP surface trie exposes to coding agents. Designed for agents, not humans:
few verbs that match cognitive moves, rich parameters per verb, prose attached
where it helps the agent decide, every knob configurable on our side so we can
experiment without breaking the contract.

> **Status:** v1 design spec. Not yet implemented. This is the contract trie
> exposes when the rest of v1 lands.

---

## The basis test

Before listing the verbs: the surface has to span the space of legitimate
agent questions about a codebase, without overlap between verbs and without
gaps. The verbs are basis vectors over the question space.

The space decomposes into primitive operations:

- **Select** — pick symbols from the symbol table by some predicate.
- **Expand** — walk the reference graph from a set of symbols outward.
- **Attach** — fetch metadata (signature, prose, source location) for symbols.

Every agent question is a composition of these. The exposed verbs are
ergonomic groupings of select + expand + attach, shaped to match how agents
phrase questions, not how the database stores data.

What we deliberately don't expose as separate verbs:

- **Compare** ("what do A and B have in common?") — composes from two
  `locate` or `walk` calls and a set intersection in the agent's reasoning.
  Not a basis vector.
- **Aggregate / count** ("how many public functions in `trie/sync/`?") —
  expressible by `locate` with a predicate and reading the result length.
- **Time-travel** ("what changed last week?") — git owns this. The sentinel
  sections preserve intent across regenerations, which is the part that
  belongs to trie. Per-section change history is `git log` over
  `triefacts/`.

The result is three verbs, no more.

---

## Design principles

The principles are doing real work — every signature below traces back to
one of these.

1. **Verbs match cognitive moves.** Agents reason in three steps when
   navigating an unfamiliar codebase: _find it_, _understand it_, _trace
   it_. One verb per move.
2. **Few tools, rich parameters.** LLMs are bad at choosing among many
   tools and good at filling in many fields. Three tools, each with enough
   knobs to express the common case in one call.
3. **Round trips are the cost, not response size.** Every MCP call
   re-prompts the agent's full context. A 2k-token response that saves
   three follow-up calls is cheaper than three 500-token responses.
   Default response shapes anticipate the next call.
4. **One-liner on every symbol mention.** Pulled from the section body at
   index time, free to return. Kills the agent's "should I open this?"
   decision. The single most valuable piece of data on the surface.
5. **Resolution is binary, not fuzzy.** Static analysis either resolves
   a symbol's references exhaustively or it doesn't. Symbols whose
   references can't be statically resolved (dynamic dispatch, `getattr`
   indirection, metaclass magic) are flagged `incomplete` with structured
   notes explaining why. There is no "70% confident" edge — edges are
   precise or absent.
6. **Every knob is server-configurable.** Some defaults will be wrong. We
   need to flip them based on observed agent behaviour without a contract
   change. Everything below has a config knob even when the agent doesn't
   see it.

---

## The three verbs

```
locate(predicate, rank_by?, limit=10)
explain(qname)
walk(from_qname, direction, depth=2)
```

That's it. Every navigation question an agent has decomposes into a chain
of these.

### `locate` — find symbols matching a predicate

```
locate(
  predicate: {
    name_contains?: str,
    kind?: "function" | "class" | "method" | "any",
    scope_prefix?: str,
    scope_exclude?: [str],
    public_only?: bool,
    inbound_count?: { min?: int, max?: int },
    outbound_count?: { min?: int, max?: int }
  },
  rank_by?: "public_first" | "inbound_count" | "alphabetical" = "public_first",
  limit: int = 10
) -> [{
  qname: str,
  signature: str,
  file_pointer: str,           // "trie/sync/cascade.py:23"
  one_liner: str,              // first sentence of section body, "" if no triefact
  is_public: bool,
  kind: str,
  resolution: "complete" | "incomplete"
}, ...]
```

**Tool description (the string the agent reads):**

> Find symbols matching a predicate. Use when you have a name fragment,
> a path prefix, or a structural property (public, hub, leaf) but don't
> know which specific symbol you want. Returns up to `limit` matches
> ranked per `rank_by`. Each result includes a one-sentence description
> so you can pick the right one without opening it. Provide only the
> predicate fields you need — most queries use just `name_contains` or
> `scope_prefix`.

**Parameters worth defending:**

- `predicate` is a single nested object, not flat parameters. This is
  the load-bearing design choice. It means every query is a structured
  filter the agent assembles once; we can add predicate fields later
  without proliferating verbs or breaking signatures. Risk: agents
  over-specify when invited to. Mitigation: the tool description and
  examples lean hard on "use one or two fields, not all of them."
- `name_contains` is substring, case-insensitive, against the symbol's
  local name (not qname).
- `scope_prefix` is a path prefix (`"trie/"`). `scope_exclude` is a list
  of prefixes to skip (`["tests/", "vendor/"]`). Together they cover
  the common case of "find me X in source code, not tests."
- `inbound_count` / `outbound_count` accept `{ min, max }` ranges. This
  is how "find hubs" (`inbound_count: { min: 20 }`) and "find leaves"
  (`outbound_count: { max: 0 }`) are expressed. No separate verb needed.
- `rank_by: "inbound_count"` is the orientation primitive: "what's
  load-bearing in this codebase?" returns the most-referenced symbols
  first regardless of name match.
- `limit` is the only output control. If the result set is too large,
  the agent narrows the predicate. We don't paginate — agents handle
  pagination poorly and a stable result set is worth more than
  completeness.
- `resolution` is on every result so the agent knows upfront whether
  this symbol's graph is exhaustive.

**Server config (not exposed):**

- `locate_max_limit`: hard ceiling on `limit`. Default 50.
- `locate_one_liner_max_chars`: truncate one-liners past this length.
  Default 200.
- `locate_default_rank_by`: if the agent doesn't set `rank_by`, use this.
  Default `"public_first"`. Flip to `"inbound_count"` if we find agents
  benefit from centrality-first orientation.

---

### `explain` — understand a specific symbol and its immediate context

```
explain(qname: str) -> {
  qname: str,
  signature: str,
  prose: str,                    // the section body, sentinels stripped
  source_pointer: str,           // "trie/sync/cascade.py:23-79"
  resolution: "complete" | "incomplete",
  callers: [{
    qname: str,
    signature: str,
    one_liner: str
  }, ...],
  callees: [{
    qname: str,
    signature: str,
    one_liner: str
  }, ...],
  notes?: [str]                  // present only when there's something to flag
}
```

**Tool description (the string the agent reads):**

> Read a symbol's full description and the one-sentence summaries of every
> symbol that calls it or that it calls. Use after `locate` once you know
> which symbol you want to understand. Returns the narrative for this
> symbol plus enough context on its immediate neighbours to decide whether
> to follow a caller or callee with another `explain` or `walk` call. The
> `notes` field, when present, warns about known incompleteness in the
> references (e.g. dynamic dispatch the static analysis couldn't follow).

**Parameters worth defending:**

- No `with_neighbours` boolean. `explain` always returns one hop with
  prose one-liners. The common case is "I want to understand this thing
  _and_ what reaches it" — forcing two calls for that is the chattiness
  problem we're designing against.
- No depth knob. If the agent wants more than one hop, it uses `walk`.
  The verb split stays clean.
- `prose` is the section body verbatim, with the sentinel HTML comments
  stripped. No front-matter, no other sections.
- Edges carry no `confidence` field. Resolution is per-symbol, not
  per-edge. If a symbol's references can't be statically resolved, the
  symbol is flagged `incomplete` and the `notes` field explains what was
  unresolvable.

**Server config (not exposed):**

- `explain_neighbour_one_liner_max_chars`: tighter than the `locate` cap.
  Default 120. Neighbour one-liners are labels, not summaries.
- `explain_max_neighbours_per_direction`: cap on `callers` / `callees`
  length. Default 0 (unlimited). When hub symbols flood the response,
  cap and add a note: `"showed 20 of 47 callers; use walk(direction='callers')
  for full topology"`.
- `explain_prose_max_chars`: truncate prose past this length with
  `"...(truncated; see source)"`. Default 0 (unlimited).

**`notes` content:**

The agent reads `notes` as authoritative. We populate it only when
there's something specific to say:

- `"callees may be incomplete: this function dispatches via handlers[name]();
  the call sites are dynamic"` — emitted when the symbol's body contains
  dynamic dispatch patterns the analyzer couldn't resolve.
- `"this symbol has 47 inbound edges and is treated as a hub; cascade
  expansion stops here"` — emitted when the symbol exceeds the hub threshold.
- `"no triefact exists for this symbol's file; prose is empty"` — emitted
  when the symbol is in scope but hasn't been synced yet.

---

### `walk` — trace topology beyond one hop

```
walk(
  from_qname: str,
  direction: "callers" | "callees" | "both",
  depth: int = 2
) -> {
  root: {
    qname: str,
    signature: str,
    one_liner: str,
    resolution: "complete" | "incomplete"
  },
  nodes: {
    [qname: str]: {
      signature: str,
      one_liner: str,
      resolution: "complete" | "incomplete"
    }
  },
  edges: [{
    from: str,
    to: str,
    direction: "in" | "out"      // relative to root: "in" = caller-side
  }, ...],
  truncated_at?: [str],          // hub qnames where expansion stopped
  notes?: [str]
}
```

**Tool description (the string the agent reads):**

> Trace the call graph from a symbol outward. Returns signatures and
> one-sentence descriptions for every reachable symbol within `depth` hops,
> plus the edges between them. Use to understand the shape of a change's
> blast radius or to find related symbols beyond the immediate neighbours.
> Does not return full prose — when a specific node turns out to matter,
> follow up with `explain` on that node. `direction="both"` returns
> callers and callees; each edge is tagged with its direction relative
> to the starting symbol. Expansion stops at hub symbols (frequently
> referenced ones); their qnames appear in `truncated_at`.

**Parameters worth defending:**

- `direction="both"` is allowed and is the common case for blast-radius
  questions. Edges are direction-tagged so the agent can reconstruct
  topology from a single call.
- `depth=2` default. Depth=1 is what `explain` already gives; the verb
  exists for the depth>1 case. Going further than 2 is rare and we'd
  rather the agent ask explicitly than get it by default.
- Nodes are a `{qname: data}` map, not an array. Lets the agent look up
  a node by qname without scanning. Also makes shared neighbours
  obvious — if two callers reach the same hub, the hub appears once in
  `nodes` and twice in `edges`.
- No prose on nodes. The verb split is load-bearing here. If the agent
  needs prose for a specific node it found via `walk`, it calls
  `explain` on that node. The config knob to flip this exists; we
  experiment before exposing.
- Edges carry no `confidence`. Same reasoning as `explain`.

**Server config (not exposed):**

- `walk_max_depth`: hard ceiling on `depth`. Default 5. Agent-provided
  depth is clamped silently with a note.
- `walk_hub_threshold`: symbols with more than this many inbound edges
  are not expanded through (they appear as leaves and in `truncated_at`).
  Default 20, mirrors `cascade.hub_symbol_threshold`. Sharing this value
  is intentional — the agent's view of "where the graph stops" matches
  the cascade's view of "where invalidation stops."
- `walk_max_nodes`: hard cap on total nodes returned. Default 200. Belt-
  and-suspenders against pathological fan-outs the hub-skip doesn't catch.
  Truncation adds a note: `"walk reached max_nodes=200; result is
  BFS-ordered from root"`.
- `walk_prose_at_depth`: if non-zero, attach prose to nodes up to this
  BFS distance from root. Default 0 (off). The lever for the "should
  walk carry prose?" experiment.
- `walk_prose_budget`: when `walk_prose_at_depth > 0`, cap on number of
  nodes that get prose bodies. BFS-ordered. Default 10.

---

## How the three verbs compose

The point of the verb split is that real questions decompose cleanly.
Worked examples:

**"What does `compute_cascade` do?"**

```
explain("trie/sync/cascade:compute_cascade")
→ one call, prose + immediate neighbours with one-liners. Done.
```

**"Where is the cascade logic?"**

```
locate({ name_contains: "cascade", scope_prefix: "trie/" })
→ pick the right qname from the result (free, via one_liner).
explain(that qname)
→ two calls. The locate one-liners mean the agent doesn't open the wrong file.
```

**"What's the blast radius if I refactor `Store.references_in_with_files`?"**

```
walk("trie/graph/store:Store.references_in_with_files",
     direction="callers", depth=2)
→ topology of everything that reaches this method, two hops out.
explain(qname) on any node that looks worth understanding deeper.
→ 1 + N calls, where N is the number of branches that matter.
```

**"Where do I even start in this codebase?"**

```
locate({ scope_prefix: "trie/", public_only: true },
       rank_by="inbound_count",
       limit=10)
→ the 10 most-referenced public symbols. The architectural skyline.
explain on the two or three that look load-bearing.
```

**"What do `compute_cascade` and `run_incremental_sync` have in common?"**

```
walk("...:compute_cascade", direction="callers", depth=1)
walk("...:run_incremental_sync", direction="callers", depth=1)
→ intersect the node sets in the agent's reasoning. Two calls, no
   dedicated verb. Composition is the answer.
```

**"Find me hubs that aren't in tests"**

```
locate({ inbound_count: { min: 20 }, scope_exclude: ["tests/"] },
       rank_by="inbound_count")
→ one call. The aggregate question is just a predicate.
```

What's absent from these chains: any call that returns information the
agent didn't ask for. No whole-file reads. No "let me parse this Markdown
to find the section I want." No "let me make five calls because the graph
endpoint didn't carry one-liners."

---

## Error shapes

Errors are agent-readable. Every error response has the same shape:

```
{
  error: {
    code: "not_found" | "invalid_argument" | "out_of_scope" | "internal",
    message: str,                  // written for the agent
    suggestion?: str               // what to try instead
  }
}
```

Examples:

```
locate({ name_contains: "compute_cassade" }) // typo
→ { error: { code: "not_found",
             message: "No symbols match 'compute_cassade'. Closest matches:
                       'compute_cascade', 'CascadeResult'.",
             suggestion: "Try locate({ name_contains: 'cascade' }) for a broader search." } }

explain("trie/sync/cascade:Compute_Cascade") // wrong case
→ { error: { code: "not_found",
             message: "No symbol with qualified name 'trie/sync/cascade:Compute_Cascade'.
                       Did you mean 'trie/sync/cascade:compute_cascade'?",
             suggestion: "Use locate({ name_contains: '...' }) to find the exact qname." } }

walk("...:compute_cascade", direction="callers", depth=10)
→ depth silently clamped to walk_max_depth. Not an error; surfaced as a note:
  notes: ["depth was clamped from 10 to 5 (server max)"]
```

The `suggestion` field is load-bearing. Agents recover from errors better
when they're told what to do next, not just what went wrong.

---

## Server-side configuration

All knobs above live in `trie.toml` under `[mcp]`:

```toml
[mcp]
# locate
locate_max_limit = 50
locate_one_liner_max_chars = 200
locate_default_rank_by = "public_first"

# explain
explain_neighbour_one_liner_max_chars = 120
explain_max_neighbours_per_direction = 0    # 0 = unlimited
explain_prose_max_chars = 0                  # 0 = unlimited

# walk
walk_max_depth = 5
walk_hub_threshold = 20                      # mirrors cascade.hub_symbol_threshold
walk_max_nodes = 200
walk_prose_at_depth = 0                      # 0 = no prose on walk
walk_prose_budget = 10
```

These are deliberately not part of the MCP tool schemas the agent reads.
The agent sees one stable contract; we adjust behaviour underneath.

---

## What this replaces

The current tools in `trie/mcp_server.py`:

| Current | Successor | Notes |
| --- | --- | --- |
| `get_triefact(source_path)` | _removed_ | Whole-file reads are a debugging affordance, not an agent primitive. |
| `find_symbol(name, limit)` | `locate(predicate, ...)` | Predicate object replaces flat parameters; adds graph-property filters. |
| `references_to(qname)` | `explain(qname).callers` + `walk(qname, "callers", depth)` | Same data, prose joined, edges precise. |
| `references_from(qname)` | `explain(qname).callees` + `walk(qname, "callees", depth)` | Same data, prose joined, edges precise. |

The shift is from four nouns to three verbs, with the verbs aligned to the
cognitive moves an agent makes when navigating a codebase.

---

## What this requires upstream

The interface above assumes the underlying graph is precise. That requires
the v1 reference extractor to be static-analysis-based (Pyright / SCIP)
rather than the v0.1 tree-sitter heuristic. The agent contract has no
notion of edge confidence — symbols are either fully resolved or flagged
`incomplete` with structured notes.

Concretely, before the interface ships:

1. **Replace `trie/parse/references.py`** with a static analyzer driver.
2. **Drop the `confidence` field** from the `edges` table schema. Add a
   `resolution` field to the `symbols` table (`complete` | `incomplete`)
   and a per-symbol `unresolved_notes` field.
3. **Update `compute_cascade`** to read the new schema. Hub-threshold
   logic is unchanged; the change is in what edges exist, not how they're
   walked.

This is upstream work, not interface work. It's noted here so the
interface contract isn't read as if it works over the v0.1 graph — it
doesn't, and shouldn't.

---

## Open questions

These are real, and should be answered by dogfooding, not in this doc.

1. **Does `walk` need prose?** Spec says no, config knob exists. Run the
   eval harness with `walk_prose_at_depth = 0` and `= 1`, compare task
   success rate and total tokens consumed. Decide.
2. **Does `locate` need pagination?** Spec says no, `limit` is the only
   control. If agents routinely hit the limit and have no way to narrow,
   that's a signal.
3. **Should `locate` return prose, not just one-liners?** Probably not —
   the one-liner is meant to be cheap. But if agents regularly call
   `locate` followed by `explain` on the top result, the one-liner
   isn't enough.
4. **Default `rank_by`.** `"public_first"` is the obvious default;
   `"inbound_count"` (centrality) might be better for unfamiliar
   codebases. Config knob exists; A/B in dogfooding.
5. **Does over-specification on `locate.predicate` show up in practice?**
   The fear: agents fill in every predicate field when they only need
   one. If logs show this, the tool description needs sharpening or the
   predicate fields need separating into "common" and "advanced" tiers.

Each is a small experiment that doesn't change the API.
