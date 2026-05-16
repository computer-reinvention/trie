# Using trie

A guide for coding agents working in a project that has trie installed.

trie indexes source code into a graph of symbols and references, attaches
prose to each public symbol, and exposes three navigation tools over MCP:
`locate`, `explain`, and `walk`. This document is about how to use them
well — when to reach for which, when not to, and how the tools compose.

If you've never used trie before, the discipline below is load-bearing.
Picking the right verb at the right moment is most of the value.

---

## The three tools, at a glance

```
locate(predicate, rank_by?, limit?)   →  find symbols
explain(qname)                        →  understand a symbol + immediate context
walk(from_qname, direction, depth?)   →  trace the call graph farther
```

Every navigation question decomposes into a short chain of these. You
almost never need more than three calls to answer a question about an
unfamiliar codebase.

---

## The core discipline: `locate` is your grep for code

**For anything that lives in indexed source code, reach for `locate`
first. Not `grep`.**

`locate` is strictly more useful than `grep` for source files trie has
indexed. It works in two modes, and the response shape tells you which:

1. **Symbol-name match.** When your `name_contains` matches one or more
   symbol names, `locate` returns full symbol details: signature, file
   pointer, one-liner from the prose, public/private flag, inbound/outbound
   edge counts. You picked the right symbol from prose, not by guessing.

2. **Grep fallback.** When `name_contains` doesn't match any symbol name
   but the literal string appears inside indexed source, `locate` falls
   back to grep — but **attributes each match to the smallest enclosing
   symbol**, then ranks results by `inbound_count` (most-referenced first)
   and caps at a configured limit. So instead of `file.py:line 47`, you
   get `pkg/module:function_name` plus its signature, one-liner, and where
   it lives in the call graph.

Both modes share one envelope. The response always looks like:

```json
{
  "hits": [ /* symbol-name matches, if any */ ],
  "fallback": { /* present only when hits is empty */
    "kind": "grep" | "grep_empty" | "none",
    /* ...kind-specific fields... */
  }
}
```

When `hits` is non-empty, ignore `fallback` (it's absent). When `hits` is
empty, the `fallback.kind` tells you what happened:

- **`"grep"`** — the literal string appears in source bodies. `matches`
  is a ranked list of enclosing symbols, capped at `locate_fallback_match_limit`
  (default 20). The `match_count` and `unique_symbols` fields tell you
  the breadth of the underlying hit; if `matches.length` is less than
  `unique_symbols`, the note explains how many were truncated.

- **`"grep_empty"`** — neither symbol names nor source bodies contain the
  query. Likely a typo or a name that doesn't exist in this project.

- **`"none"`** — the predicate had no `name_contains` for grep to use.
  Add a name substring or relax other filters.

### When `grep` is still the right tool

`grep` (or your editor's text search) remains the right answer when:

- **The target isn't in indexed source.** Markdown, logs, commit
  messages, config files, generated fixtures. trie indexes the language
  it's configured for (typically Python `.py` files); everything else is
  grep territory.

- **You want a string-pattern search, not a symbol search.** E.g. "find
  every call site that passes `db_path` positionally" or "every place
  that uses `f-string` with a specific format token." These are patterns
  over source text, not queries about symbols. `locate` would only match
  symbols whose *names* contain `db_path`.

- **You're looking for module-level constants.** trie indexes functions,
  methods, and classes. A `MAX_RETRIES = 5` at module level isn't a
  separate symbol; `locate("MAX_RETRIES")` will only find symbols whose
  names contain `MAX_RETRIES` as substring. Grep for the constant
  literal.

For everything else inside indexed source, default to `locate`. If a
navigation flow feels awkward through these tools, that's a signal worth
flagging to whoever maintains the project's trie setup — not a reason to
silently fall back to grep.

---

## `locate` — finding symbols

```
locate(predicate, rank_by?, limit?)
```

### The predicate object

Build your query as a single nested object. All fields optional; most
queries use one or two.

```python
# Find symbols by name substring (case-insensitive, local name only)
locate({ "name_contains": "compute_cascade" })

# Restrict to a path prefix — "in trie/ but not tests/"
locate({ "name_contains": "cascade", "scope_prefix": "trie/" })

# Exclude paths
locate({ "name_contains": "config", "scope_exclude": ["tests/", "vendor/"] })

# Filter by symbol kind
locate({ "kind": "class", "scope_prefix": "trie/" })
# kind: "function" | "class" | "method" | "any"

# Only public symbols (no leading underscore)
locate({ "name_contains": "store", "public_only": true })

# Structural filters: find hubs (most-called) or leaves (uncalled)
locate({ "inbound_count": { "min": 20 } })          # hubs
locate({ "outbound_count": { "max": 0 } })          # leaves
locate({ "inbound_count": { "min": 5, "max": 15 } }) # mid-tier
```

### Ranking

```python
locate({ ... }, rank_by="public_first")    # default; public symbols first
locate({ ... }, rank_by="inbound_count")   # most-referenced first
locate({ ... }, rank_by="alphabetical")    # by qname
```

`rank_by="inbound_count"` is the **architectural orientation primitive**:
"What's load-bearing in this codebase?"

```python
# Top 10 most-referenced public symbols under trie/
locate({ "scope_prefix": "trie/", "public_only": true },
       rank_by="inbound_count", limit=10)
```

This is often the first call to make in an unfamiliar codebase. It
returns the architectural skyline — the symbols everything else flows
through.

### What you get back

Each hit (whether in `hits` or in `fallback.matches`) carries:

```json
{
  "qname": "trie/sync/cascade:compute_cascade",
  "signature": "def compute_cascade(...) -> CascadeResult",
  "file_pointer": "trie/sync/cascade.py:23",
  "one_liner": "Walk the reference graph outward from changed symbols up to hub_threshold.",
  "is_public": true,
  "kind": "function",
  "inbound_count": 7,
  "outbound_count": 4
}
```

The `one_liner` is the first sentence of the symbol's prose. It lets you
**pick the right symbol from a list without opening any of them**. This
is the single most valuable piece of data on the response — it kills the
"should I open this?" decision.

---

## `explain` — understanding a specific symbol

```
explain(qname)
```

Use this **after `locate`**, once you know which symbol you want to
understand.

```python
explain("trie/sync/cascade:compute_cascade")
```

Returns:

- **`signature`** — the function/method signature, verbatim.
- **`prose`** — the full triefact section body for this symbol. Whatever
  documentation has been generated and curated.
- **`source_pointer`** — `path:start_line-end_line` so you can open the
  source if prose isn't enough.
- **`callers`** — every symbol that calls this one, with `qname`,
  `signature`, and `one_liner` for each.
- **`callees`** — every symbol this one calls, same shape.
- **`notes`** — present only when there's something to flag (incomplete
  resolution, hub-capping, missing triefact).

The key property: **callers and callees come back with one-liners**.
You don't need a follow-up call to know "what does that caller do?" —
the one-sentence summary is in the response.

This is why `explain` is one call and not three. The common cognitive
move when reading a function is "what does this do AND what reaches it?"
We pre-bundle that for you.

### Qname format

trie uses `path/to/file:LocalName` for top-level symbols and
`path/to/file:ClassName.method` for methods. Drop the `.py` extension;
use forward slashes regardless of OS.

When `locate`, `explain`, or `walk` returns a `qname`, you can pass it
straight back to `explain` or `walk` — no rewriting needed. Round-trip.

---

## `walk` — tracing topology beyond one hop

```
walk(from_qname, direction, depth?)
```

When one hop (which `explain` already gives you) isn't enough, use
`walk` to traverse the call graph farther.

```python
# What calls compute_cascade, transitively, two hops out?
walk("trie/sync/cascade:compute_cascade",
     direction="callers", depth=2)

# What does run_incremental_sync end up calling, two hops down?
walk("trie/sync/incremental:run_incremental",
     direction="callees", depth=2)

# Both directions — blast radius and dependencies in one call
walk("trie/graph/store:Store.replace_all_edges",
     direction="both", depth=2)
```

### Return shape

```json
{
  "root": { "qname": "...", "signature": "...", "one_liner": "..." },
  "nodes": {
    "qname1": { "signature": "...", "one_liner": "..." },
    "qname2": { "signature": "...", "one_liner": "..." }
  },
  "edges": [
    { "from": "qname1", "to": "qname2", "direction": "in" }
  ],
  "truncated_at": ["hub_qname"]   // present when expansion stopped at hubs
}
```

`direction` on each edge is **relative to the root**: `"in"` means
caller-side, `"out"` means callee-side. With `direction="both"`, the
edge tags let you reconstruct topology from one call.

Nodes come back as a `{qname: data}` map, not an array — when the same
symbol is reached through multiple paths, it appears once in `nodes`
and the multiple edges in `edges` make the shared dependency obvious.

### When `walk` stops

Expansion halts at **hub symbols** (those with very high `inbound_count`,
configurable via `walk_hub_threshold`). Hubs are listed in `truncated_at`.
The rationale: hubs are usually framework code or shared utilities;
expanding through them floods the result with irrelevant nodes.

If you specifically want to see what reaches a hub, query it directly
with another `walk` call.

### `walk` doesn't carry prose

Only signatures and one-liners. When a specific node in the walk turns
out to matter, follow up with `explain(qname)` on that node to get its
full prose plus immediate neighbours.

This is intentional. `walk` is about topology; `explain` is about
substance. The verb split keeps each response focused.

---

## Worked examples: composing the three verbs

**"What does `compute_cascade` do?"**

```python
explain("trie/sync/cascade:compute_cascade")
# → one call, prose + immediate neighbours with one-liners. Done.
```

**"Where is the cascade logic?"** (you know the term, not the qname)

```python
locate({ "name_contains": "cascade", "scope_prefix": "trie/" })
# → pick the right qname from the result (use one_liner to disambiguate)
explain(that_qname)
# → two calls. The one-liners mean you don't open the wrong file.
```

**"What's the blast radius if I refactor `Store.replace_all_edges`?"**

```python
walk("trie/graph/store:Store.replace_all_edges",
     direction="callers", depth=2)
# → topology of everything that transitively reaches this method.
explain(qname) on any node that looks worth understanding deeper.
# → 1 + N calls, N = branches that matter.
```

**"Where do I even start in this codebase?"**

```python
locate({ "scope_prefix": "trie/", "public_only": true },
       rank_by="inbound_count", limit=10)
# → the 10 most-referenced public symbols. The architectural skyline.
explain on the two or three that look load-bearing.
# → builds your mental model from the top.
```

**"What do functions A and B have in common?"**

```python
walk("...:A", direction="callers", depth=1)
walk("...:B", direction="callers", depth=1)
# → intersect the node sets in your own reasoning.
# Two calls, no special verb. Composition is the answer.
```

**"Find me hubs that aren't in tests"**

```python
locate({ "inbound_count": { "min": 20 }, "scope_exclude": ["tests/"] },
       rank_by="inbound_count")
# → one call. Aggregate questions are just predicates.
```

**"Where is the string 'rate limited' used?"** (a literal, not a symbol name)

```python
locate({ "name_contains": "rate limited" })
# → hits will be empty; fallback.kind == "grep", matches attributed
#   to enclosing symbols. Better than raw grep because you get the
#   symbol context, not just file:line.
```

---

## What NOT to do

- **Don't grep for things that are in indexed source.** You lose the
  symbol-attribution and graph context that `locate` provides for free.

- **Don't call `explain` repeatedly to traverse a graph.** That's what
  `walk` is for. Each `explain` call is heavier (full prose); use it
  when you actually want to understand a symbol, not when you're tracing.

- **Don't paginate `locate`.** There's no page parameter. If the result
  set is too big, **narrow the predicate** (add `scope_prefix`, tighten
  `name_contains`, restrict `kind`). `limit` exists; pagination doesn't.

- **Don't over-specify the predicate.** Pick one or two fields. Filling
  in every field of the predicate usually means you're guessing — better
  to start broad and narrow based on results.

- **Don't manually parse a triefact file to find a section.** `explain`
  returns the section body for the symbol you asked about, directly.

- **Don't worry about whether a triefact exists.** If a symbol doesn't
  have prose yet, `explain` still returns the signature, callers, and
  callees from the graph; `prose` will be empty and `notes` will say so.

---

## Edge cases and limitations

**Module-level constants and module-level code aren't indexed as
symbols.** `locate("MAX_RETRIES")` won't find a top-level `MAX_RETRIES = 5`
constant — only symbols (functions, methods, classes) whose names
*contain* "MAX_RETRIES". When you need to find constants, grep for the
literal.

**Dynamic dispatch isn't always resolved.** If a function calls
`handlers[name]()` where `handlers` is built at runtime, the static
analyzer can't trace which functions get called. trie flags this with
a `notes` field on the symbol's `explain` response: *"callees may be
incomplete: this function dispatches via handlers[name]()"*. Read
`notes` as authoritative.

**Hub symbols cap the walk depth.** Symbols above the configured
inbound-count threshold appear as leaves in `walk` results (listed in
`truncated_at`) to prevent fanout explosions. If you specifically need
the hub's neighbourhood, query it directly with another `walk`.

**Stale graph.** If `trie` is set up with a turn-boundary refresh hook,
the graph stays current automatically. If not, the graph reflects the
last `trie sync` or `trie refresh` run. Symbols added or removed since
then are absent or stale; `locate` won't find them and `explain` will
return "not found" errors. Run `trie refresh` to bring the graph up to
date.

---

## Errors

Every error response has one shape:

```json
{
  "error": {
    "code": "not_found" | "invalid_argument" | "out_of_scope" | "internal",
    "message": "...",
    "suggestion": "..."     // present when there's something concrete to try
  }
}
```

The `suggestion` field is load-bearing. When you get a not-found, the
suggestion will usually point you at the closest matching qname or
suggest a broader `locate` query. Read it and use it.

---

## TL;DR

- Use **`locate`** to find symbols. It replaces grep for indexed source.
- Use **`explain`** to understand one symbol + its immediate neighbours.
- Use **`walk`** to trace the call graph more than one hop out.
- One-liners are everywhere; use them to triage without opening files.
- Grep is still right for non-code files, string patterns, and module-level
  constants.
