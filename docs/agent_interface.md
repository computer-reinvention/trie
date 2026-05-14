# The agent interface

The MCP surface trie exposes to coding agents. Designed for agents, not humans:
fat parameter objects over many tools, prose attached where it helps the agent
decide, every knob configurable on our side so we can experiment without
breaking the contract.

> **Status:** design spec. Not yet implemented. Supersedes the four-tool surface
> in `trie/mcp_server.py` (`get_triefact`, `find_symbol`, `references_to`,
> `references_from`), which will be retired once this lands.

---

## Design principles

The principles are doing real work — every signature below traces back to one
of these.

1. **Verbs match cognitive moves.** Agents reason in three steps when
   navigating an unfamiliar codebase: _find it_, _understand it_, _trace it_.
   The surface has one verb per move. No tool overlaps with another.
2. **Few tools, rich parameters.** LLMs are bad at choosing among many tools
   and good at filling in many fields. Three tools, each with enough knobs to
   express the common case in one call.
3. **Round trips are the cost, not response size.** Every MCP call re-prompts
   the agent's full context. A 2k-token response that saves three follow-up
   calls is cheaper than three 500-token responses. Default response shapes
   anticipate the next call.
4. **One-liner on every symbol mention.** Pulled from the section body at
   index time, free to return. Kills the agent's "should I open this?"
   decision. The single most valuable piece of data on the surface.
5. **Heuristic gaps are surfaced, not hidden.** Tree-sitter reference
   resolution has known holes (attribute access, dynamic dispatch). We
   declare gaps in a `notes` field on every response instead of letting the
   agent silently reason over an incomplete graph.
6. **Every knob is server-configurable.** Some defaults will be wrong. We
   need to flip them based on observed agent behaviour without a contract
   change. Everything below has a config knob even when the agent doesn't
   see it.

---

## The three tools

```
locate(hint, kind?, scope_prefix?, limit=10)
explain(qname)
walk(from_qname, direction, depth=2)
```

That's it. Every navigation question an agent has decomposes into a chain of
these three.

### `locate` — find a symbol when you have a name fragment or rough description

```
locate(
  hint: str,
  kind?: "function" | "class" | "method" | "any" = "any",
  scope_prefix?: str = null,
  limit: int = 10
) -> [{
  qname: str,
  signature: str,
  file_pointer: str,           // "trie/sync/cascade.py:23"
  one_liner: str,              // first sentence of section body, or "" if no triefact
  is_public: bool,
  kind: str
}, ...]
```

**Tool description (the string the agent reads):**

> Find symbols by name fragment. Use when you have a name (or part of one) but
> don't know its location. Returns up to `limit` matches ranked by public-first
> then qname. Filter with `kind` to restrict to functions, classes, or methods.
> Filter with `scope_prefix` (a path prefix like `"trie/"`) to exclude tests
> or vendored code. Each result includes a one-sentence description of what
> the symbol does, so you can pick the right one without opening it.

**Parameters worth defending:**

- `hint` is a substring match, case-insensitive, against the symbol's local
  name (not qname). Agents type `"cascade"`, not `"trie/sync/cascade:compute_cascade"`.
- `kind` defaults to `"any"` because the agent often doesn't know the kind
  upfront. Filtering is opt-in.
- `scope_prefix` is path-based, not module-based. The agent sees file paths
  in its file-reading tools, so the mental model is consistent.
- No pagination. `limit` is the only knob. If the agent's `hint` returns >
  `limit`, that's a signal to narrow the hint — exactly what we want.
- `one_liner` is empty string when no triefact exists for the symbol's file.
  Not null — agents handle empty strings more consistently than they handle
  nulls in JSON.

**Server config (not exposed):**

- `max_limit_cap`: hard ceiling on what `limit` can be. Default 50.
- `rank_strategy`: `"public_first" | "alphabetical" | "centrality"`. Default
  `"public_first"`. `"centrality"` (rank by inbound edge count) is the
  experiment lever — surface "important" symbols first regardless of name
  match position.
- `one_liner_max_chars`: truncate one-liners past this length. Default 200.

---

### `explain` — understand a specific symbol and its immediate context

```
explain(qname: str) -> {
  qname: str,
  signature: str,
  prose: str,                    // the full section body, sentinels stripped
  source_pointer: str,           // "trie/sync/cascade.py:23-79"
  callers: [{
    qname: str,
    signature: str,
    one_liner: str,
    confidence: "tree_sitter_import" | "name_match"
  }, ...],
  callees: [{
    qname: str,
    signature: str,
    one_liner: str,
    confidence: "tree_sitter_import" | "name_match"
  }, ...],
  notes?: [str]                  // present only when there's something to flag
}
```

**Tool description (the string the agent reads):**

> Read a symbol's full description and the one-sentence summaries of every
> symbol that calls it or that it calls. Use after `locate` once you know
> which symbol you want to understand. Returns the narrative for this symbol
> plus enough context on its immediate neighbours to decide whether to follow
> a caller or callee with another `explain` call. The `notes` field, when
> present, warns about known incompleteness in the references (e.g. dynamic
> dispatch the static analysis missed).

**Parameters worth defending:**

- No `with_neighbours` boolean. `explain` always returns one hop with prose
  one-liners. The common case is "I want to understand this thing _and_ what
  reaches it" — forcing two calls for that is the chattiness problem we're
  designing against.
- No depth knob. If the agent wants more than one hop, it uses `walk`. The
  verb split stays clean.
- `prose` is the section body verbatim, with the sentinel HTML comments
  stripped. No front-matter, no other sections. One symbol's worth of prose.

**Server config (not exposed):**

- `include_signature_in_neighbours`: bool. Default `true`. If we find agents
  reason fine off `one_liner` alone, drop the signature to save tokens.
- `neighbour_one_liner_max_chars`: tighter than the `locate` cap. Default 120.
  Neighbour one-liners are labels, not summaries.
- `max_neighbours_per_direction`: cap on `callers` / `callees` length. Default
  unlimited. If hub symbols flood the response, cap and add a note: `"showed
  20 of 47 callers; use walk(direction='callers') for full topology"`.
- `prose_max_chars`: truncate prose past this length with `"...(truncated;
  see source)"`. Default unlimited. Useful guardrail for pathological cases.

**`notes` content:**

The agent reads `notes` as authoritative warnings. We only populate it when
there's something specific to say. Examples:

- `"callees list may be incomplete: attribute-style references (e.g.
  store.foo) are not resolved by the current heuristic"` — emitted when
  the symbol's source contains attribute access patterns we know we miss.
- `"this symbol has 47 inbound edges and is treated as a hub; cascades stop
  here"` — emitted when the symbol exceeds the hub threshold.
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
  root: { qname, signature, one_liner },
  nodes: {
    [qname: str]: {
      signature: str,
      one_liner: str
    }
  },
  edges: [{
    from: str,
    to: str,
    direction: "in" | "out",      // relative to root: "in" = caller-side
    confidence: "tree_sitter_import" | "name_match"
  }, ...],
  truncated_at?: [str],           // hub qnames where expansion stopped
  notes?: [str]
}
```

**Tool description (the string the agent reads):**

> Trace the call graph from a symbol outward. Returns signatures and
> one-sentence descriptions for every reachable symbol within `depth` hops,
> plus the edges between them. Use to understand the shape of a change's blast
> radius or to find related symbols beyond the immediate neighbours. Does
> not return full prose — when a specific node turns out to matter, follow
> up with `explain` on that node. `direction="both"` returns callers and
> callees; each edge is tagged with its direction relative to the starting
> symbol. Expansion stops at hub symbols (frequently-referenced ones); their
> qnames appear in `truncated_at`.

**Parameters worth defending:**

- `direction="both"` is allowed and is the common case for "what's the blast
  radius?" Edges are direction-tagged so the agent can reconstruct topology
  from a single call.
- `depth=2` default. Depth=1 is what `explain` already gives; the verb
  exists for the depth>1 case. Going further than 2 is rare and we'd rather
  the agent ask explicitly than get it by default.
- Nodes are a `{qname: data}` map, not an array. Lets the agent look up a
  node by qname without scanning. Also makes shared neighbours obvious —
  if two callers reach the same hub, the hub appears once in `nodes` and
  twice in `edges`.
- No prose on nodes. The verb split is load-bearing here. If the agent
  needs prose for a specific node it found via `walk`, it calls `explain`
  on that node. We may flip this based on observed behaviour (see config).

**Server config (not exposed):**

- `max_depth_cap`: hard ceiling on `depth`. Default 5. Agent-provided depth
  is clamped silently with a note.
- `hub_threshold`: symbols with more than this many inbound edges are not
  expanded through (they appear as leaves and in `truncated_at`). Default
  20, same as `cascade.hub_symbol_threshold`. Sharing this value is
  intentional — the agent's view of "where the graph stops" matches the
  cascade's view of "where invalidation stops."
- `max_nodes`: hard cap on total nodes returned. Default 200. Belt-and-
  suspenders against pathological fan-outs the hub-skip doesn't catch.
  Truncation adds a note: `"walk reached max_nodes=200; result is BFS-
  ordered from root"`.
- `prose_at_depth`: if non-zero, attach prose to nodes up to this BFS
  distance from root. Default 0 (off). This is the lever for the
  "should walk carry prose?" experiment — flip to 1 or 2 in config,
  observe whether round-trip counts drop, decide whether to expose.
- `prose_budget`: when `prose_at_depth > 0`, cap on number of nodes that
  get prose bodies. BFS-ordered. Default 10.

---

## How the three tools compose

The point of the verb split is that real questions decompose cleanly. Some
worked examples:

**"What does `compute_cascade` do?"**

```
explain("trie/sync/cascade:compute_cascade")
→ one call, prose + immediate neighbours with one-liners. Done.
```

**"Where is the cascade logic?"**

```
locate("cascade", scope_prefix="trie/")
→ pick the right qname from the result list (free, via one_liner).
explain(that qname)
→ two calls. The locate one-liners mean the agent doesn't open the wrong file.
```

**"What's the blast radius if I refactor `Store.references_in_with_files`?"**

```
walk("trie/graph/store:Store.references_in_with_files",
     direction="callers", depth=2)
→ topology of everything that reaches this method, two hops out.
explain(qname) on any node that looks worth understanding deeper.
→ 1 + N calls, where N is the number of branches that matter. The walk
   one-liners gate which N is.
```

**"How does `compute_cascade` interact with the hub threshold?"**

```
explain("trie/sync/cascade:compute_cascade")
→ prose mentions hub_threshold; agent sees the parameter list and
  the description of what it does.
locate("hub", scope_prefix="trie/")
→ if there's a separate hub-related symbol to understand.
walk("trie/sync/cascade:compute_cascade", direction="callees", depth=1)
→ if the agent wants to see what compute_cascade itself reaches.
```

Note what's _absent_ from these chains: any call that returns information
the agent didn't ask for. No whole-file reads. No "let me parse this
markdown to find the section I want." No "let me make 5 calls because the
graph endpoint didn't carry prose."

---

## Error shapes

Errors are agent-readable. Every error response is the same shape:

```
{
  error: {
    code: "not_found" | "invalid_argument" | "out_of_scope" | "internal",
    message: str,                  // human-readable, but written for the agent
    suggestion?: str               // what the agent should try instead
  }
}
```

Examples:

```
locate("compute_cassade", ...) // typo
→ { error: { code: "not_found",
             message: "No symbols match 'compute_cassade'. The closest matches are
                       'compute_cascade', 'CascadeResult'.",
             suggestion: "Try locate('cascade') for a broader search." } }

explain("trie/sync/cascade:Compute_Cascade") // wrong case
→ { error: { code: "not_found",
             message: "No symbol with qualified name 'trie/sync/cascade:Compute_Cascade'.
                       Did you mean 'trie/sync/cascade:compute_cascade'?",
             suggestion: "Use locate() with just the name fragment to find the exact qname." } }

walk("trie/sync/cascade:compute_cascade", direction="callers", depth=10)
→ depth silently clamped to max_depth_cap. Not an error; emitted as a note:
  notes: ["depth was clamped from 10 to 5 (server max)"]
```

The `suggestion` field is the load-bearing part. Agents recover from errors
better when they're told what to do next, not just what went wrong.

---

## Server-side configuration

All knobs above are read from `trie.toml` under `[mcp]`:

```toml
[mcp]
# locate
locate_max_limit = 50
locate_rank_strategy = "public_first"
locate_one_liner_max_chars = 200

# explain
explain_include_signature_in_neighbours = true
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
| `get_triefact(source_path)` | _hidden / removed_ | Whole-file reads are a debugging tool, not an agent primitive. If we keep it at all, it's not advertised in the tool list. |
| `find_symbol(name, limit)` | `locate(hint, kind, scope_prefix, limit)` | Adds filters and one-liners. |
| `references_to(qname)` | `explain(qname).callers` and `walk(qname, "callers", depth)` | Same data, prose joined. |
| `references_from(qname)` | `explain(qname).callees` and `walk(qname, "callees", depth)` | Same data, prose joined. |

Migration is internal — the MCP tool list visibly changes from four nouns to
three verbs. Existing agent configs (`.mcp.json` etc.) keep working because
they reference the server, not specific tools.

---

## Open questions

These are real, and they should be answered by dogfooding, not in this doc.

1. **Does `walk` need prose?** Spec says no, config knob exists. Run the
   eval harness with `walk_prose_at_depth = 0` and `= 1`, compare task
   success rate and total tokens consumed. Decide.
2. **Does `explain` need a depth knob after all?** If agents routinely
   `explain` → `explain` on a returned neighbour, the depth-1 default is
   wrong. Knob already exists internally (`walk_prose_at_depth = 1` is
   roughly the same thing); the question is whether to expose it on
   `explain` directly.
3. **Should `locate` return prose, not just one-liners?** Probably not —
   the one-liner is meant to be cheap. But if agents regularly call
   `locate` followed by `explain` on the top result, that's a signal the
   one-liner isn't enough and we should consider it.
4. **Centrality ranking on `locate`.** Public-first ranking is the
   obvious default; ranking by inbound edge count ("most-referenced
   first") might be better. Config knob exists; A/B in dogfooding.

Each of these is a small experiment that doesn't change the API.
