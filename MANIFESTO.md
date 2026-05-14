# The bet

This is what trie is for. Not what it does — the README covers that. What it's
_for_, what we think happens if it works, and what would make us shelf it.

---

## The thing nobody says about coding agents

Coding agents today read code. Code is the executable form of intent, not the
explanatory form. Every time an agent reads `cascade.py` to answer a question,
it's an LLM reconstructing "what does this do and why" from `for` loops and
variable names, under context pressure, with the wrong abstraction. That's
where hallucinations come from. Not a lack of intelligence — the wrong
artifact.

The fix everyone reaches for is "give the agent better tools to read code":
semantic indexing, repo maps, smarter grep. These help. They don't change the
shape of the problem, because the problem isn't that code is hard to find —
it's that code isn't what the agent needs. The agent needs the intent. The
intent is in someone's head, sometimes in a comment, occasionally in a wiki
page that's six months out of date.

trie's bet: **the codebase should describe itself in prose, the description
should be kept in sync by construction, and that description should be the
primary artifact both humans and agents work against.** Code becomes the
executable form of the prose, not its source of truth.

---

## What we think happens if it works

There are four rings of effect. The first is the cost of admission — a
useful product, not a category. The second is where the value really lives
near-term. The third is the thing worth building a company around. The
fourth is where this is all going on a decade-plus timescale, and the
reason the architecture is shaped the way it is.

### Ring 1 — Navigation gets cheap

Agents stop grepping. They join paragraphs. Cross-file changes stop being
"open six files and reconstruct the call graph in context window"; they
become "walk the graph, read the relevant sections, change the code." Token
spend drops. Hallucinations drop. The agent's answers get faster and more
accurate on the questions agents already answer.

This is the floor. If trie only delivers Ring 1, it's a useful tool — a
better MCP server, a cheaper way to feed context to Claude Code. Worth
shipping, not worth building a company around. Lots of people are competing
for this prize: Serena, aider's repo-map, Cursor's semantic indexing. We
would be one entry in a crowded race.

### Ring 2 — Questions that weren't economical become routine

This is where it gets interesting. There's a class of questions agents
_could_ answer today but don't, because the cost of answering them is
prohibitive. With navigation cheap, these questions become casual lookups.

**Blast-radius questions.** "If I change the return type of this function,
what breaks?" Today: agent greps callers, opens each file, infers whether
the change matters. Five minutes, several thousand tokens, often wrong.
With trie: one graph walk for topology, prose-read on the three callers
that actually use the return value, done. The answer the agent gives is
"here are the 3 places that care, here's why each cares, here's the one
that's actually a problem." That's a kind of answer agents currently
don't give because it's too expensive to construct.

**"Why is this the way it is" questions.** "Why does this function skip
hub symbols on cascade?" Today: agent reads the code, sees the threshold
check, fabricates a plausible reason. With trie: the prose section _says
why_, because the rationale was captured at write time and survives
regeneration via the human-edited sentinel sections. Tribal knowledge
stops being tribal.

**Architecture archaeology.** "How does a request flow from middleware to
response?" Today: a research task. Open files, build a mental model, write
it up. With trie: locate the entry, walk callees, read the narrative shape
of the flow in one chain of calls. The agent isn't reconstructing the
architecture diagram every time someone asks — it's reading the one that
was written when the code was written.

**Cross-cutting concern queries.** "Where does this codebase handle auth?"
Today: grep `auth`, get 80 hits, sift. With trie: a semantic index of what
each symbol _does_, ranked, with one-sentence descriptions. The agent
reasons over a curated map, not a string match.

**Onboarding-as-conversation.** A new contributor — human or agent — asks
"where do I start to add a new auth provider?" Today: someone senior
writes a doc that goes stale. With trie: the answer is a chain of reads
that follow the existing auth provider's graph. Always current, always
specific to this codebase.

What these have in common: **the value is in the synthesis, not the
lookup.** Today the lookup is so expensive the synthesis never happens.
Ring 2 is the bet that cheap lookup makes synthesis the default.

If we deliver Ring 2 — if agents answer a new _category_ of question
that wasn't economical before — trie is a category, not a feature. That
is the bet worth taking.

### Ring 3 — The artifact inverts

This is speculative. We don't know yet that this happens. But if Ring 2
works, these effects follow, and they're the thing worth building a
company around.

**Prose becomes primary, code becomes its executable form.** Right now,
code is the source of truth and prose is a lagging, often-wrong shadow.
trie inverts this _only if_ the prose is trustworthy enough that
disagreements get resolved toward it. When that happens: a bug becomes
"the paragraph said X, the code does Y, the code is wrong." Specs get
written as prose paragraphs and implemented because the implementation
is the cheap part. **PR review inverts: you're reviewing intent, not
implementation. The code diff is just confirmation that the change
matches its description.**

**Architectural drift becomes visible early.** A change whose prose diff
lights up regions that "shouldn't be related" is the early-warning
signal for coupling that's wrong. Today this is invisible until someone
reviews the whole system holistically (rare) or until it causes pain
(late). With trie, the lit-region pattern shows it on every PR.
Reviewers ask "why did the auth change reach into the parser?" before
it's load-bearing.

**The senior/junior gap narrows on review.** Today, reviewing a PR
meaningfully requires already holding the system in your head — which
is exactly the population that needs agents the least. With prose
diffs as the primary review surface, a reviewer who has never seen the
repo can ask the right question, because the system is describing
itself to them as they read. Senior review may stop being a
tenure-locked skill.

**Knowledge stops walking out the door.** The engineer who knows why
the cascade skips hub symbols writes it in the prose. They leave. The
knowledge stays. Today, the same engineer leaves a comment that says
"TODO: explain why" and the institutional memory dies. The prose
layer is a structural fix for tribal knowledge loss — not because we
asked people to write more docs, but because the cost of _not_ writing
them shows up immediately as agent hallucinations the team feels.

**Agents contribute to the model, not just consume it.** Today an
agent that figures something out about your codebase puts that
knowledge in its session memory and loses it when the conversation
ends. With trie, the agent's next move after understanding something
is to write that understanding into the relevant section between
sentinels, propose it as a PR. The codebase's self-description gets
richer with every agent pass that humans ratify. This is the
compounding loop: **the artifact gets better the more it's used, by
both humans and agents.**

### Ring 4 — Programming stops being about code

This is a decade out, minimum. Probably more. We name it because the
architecture we're building only makes sense if something like this
is where the work ends up. This is the shape of the future trie is
reaching toward.

The premise: looking at code, line by line, is a thing humans do
because the executable form happens to also be the only durable form
the intent has. Once the prose layer is trustworthy and the graph is
first-class, the executable form stops being the primary surface for
human work. We don't read it. We don't write it directly. We _shape_
the system at a level above it, and the code conforms.

What that looks like, concretely:

**The IDE goes away.** The default work surface is no longer a text
editor showing a file. It's a navigable representation of the system:
prose, graph, dependencies, invariants. You move through it
spatially. You see the system the way you currently see a city from
above — regions, flows, scale, density. The Tony Stark moment is the
natural interface for working at the level of "what should this
system do" rather than "what should this line say."

**Changes are made by gesture, not by edit.** "Move auth out of the
request path and into a separate middleware tier" is a change you
describe in prose, with the system itself confirming the topology
makes sense before any line of code is touched. The implementation
is a downstream consequence, generated and verified against the
prose. You spend zero time on syntax and full time on architecture.
The protagonist rearranging glowing pieces of a holographic system
is what the work actually is, once the intent layer is real.

**Code review becomes simulation.** You don't review a diff. You
inspect the proposed _new state of the system_ — its prose, its
graph, its invariants — and ask "is this the system we want?" The
old version is right next to it, the differences highlighted at
whatever altitude you choose: paragraph, region, whole-architecture.
You see consequences before they ship.

**Programming languages stop being load-bearing.** The choice of
Python vs. Rust vs. whatever-comes-next becomes a property of the
compile target, not the medium of thought. The medium of thought is
the intent layer. Different parts of the same system compile to
different targets. The artifact a human works against is the same
across all of them.

**"Senior engineer" stops meaning "person who has read enough code."**
It means "person whose sense of what a good system looks like is
sharp." Holding the system in your head is no longer the
prerequisite, because the system describes itself to you at every
level of zoom. The barrier to contributing to a large unfamiliar
system collapses from "spend three months reading code" to "spend
an afternoon exploring the prose and graph."

We are building the seed of this. A sentinel-preserving prose tree
synced to a reference graph with bidirectional drift detection is,
structurally, the bottom of the stack the Ring 4 world is built on.
The next thing someone builds on top of it is a richer rendering —
and the thing after that, and the thing after that. By the time
anyone is literally rearranging glowing components in a Tony Stark
room, the prose-graph-fingerprint substrate underneath looks a lot
like what we're doing now, enormously refined.

This is a load-bearing constraint on the choices we make today. Every
design decision passes the test: **does this still make sense if it
becomes the seed of a future where humans stop reading code?** A
design choice that only works while humans are the primary readers
of source files is a design choice with an expiration date.

The bet isn't that this future arrives on any specific date. The bet
is that **whatever shape it takes, the intent layer has to be real
and trustworthy first** — and that is the work trie is doing now.

---

## What this is not

We owe ourselves clarity about what we're not claiming, because the
adjacent ideas have all been tried and most have failed.

**Not "write better docs."** Docs go stale. trie's whole architecture —
fingerprints, cascade, pre-commit verify — exists because we believe
prose that isn't kept in sync by construction is worse than no prose.
The bet is structural, not exhortative.

**Not "comments as documentation."** Comments live in the code, share
its context window, and are read by the same eyes that read the code.
Prose in a separate, navigable, graph-connected tree is a different
artifact for a different reader. The separation matters.

**Not "AI-generated docs."** Generated docs are the failure mode of
this approach, not the goal. The LLM is a scaffolder. The value comes
from human-edited sentinel sections that capture _why_, which is what
LLMs can't generate from syntax. If the prose is just regurgitated
code, we've built a worse code-reading tool.

**Not "smarter search."** Semantic search, vector retrieval, repo maps
— these all answer "where is the thing." trie answers "what is the
thing and why is it that way." Search is Ring 1, and we'll lose that
race to teams who only do search. Our prize is Rings 2 and 3 or
nothing.

**Not a replacement for reading code.** Code is still the source of
truth for behaviour. trie is the source of truth for _intent_. When
they disagree, the bug is real and one of them is wrong. trie's
contribution is making that disagreement legible.

---

## What would make us shelf it

The product fails if:

**The prose is too generated.** If 50% of generated sections get
hand-rewritten within a week, the LLM is just adding friction. The
half-life of generated prose is the real test of whether this works.

**Drift compounds despite the cascade.** If `trie verify` fires
constantly on real refactors, or worse, if it misses real drift and
the tree silently rots, the trust collapses and the system becomes
worse than nothing. Bidirectional drift detection is load-bearing.

**Agents don't change their behaviour.** If, given the MCP server,
agents keep grepping anyway — because the prose surface is awkward,
or because their training is too biased toward code-reading — Ring
1 never lands, and Ring 2 is impossible.

**Humans don't change their behaviour.** If reviewers ignore the
prose diff and only look at the code diff, Ring 3 never lands. The
prose layer becomes a parallel artifact nobody trusts, which is the
fate of every "living documentation" attempt before this one.

**Ring 1 lands but Ring 2 doesn't.** We become "another MCP server"
in a crowded market. Useful, but commodity. Probably the most likely
failure mode and the one we should watch for hardest.

We will measure these — see `docs/validation.md` for how. The
distinction we hold ourselves to is between **"trie works"** (Ring 1)
and **"trie matters"** (Rings 2 and 3). The first is easy to
demonstrate and not enough. The second is the near-term bet. Ring 4
is not something we will validate in the next year; it's the
direction the architecture has to remain consistent with, and the
reason we won't compromise the substrate to win Ring 1 faster.

---

## Why now

Three things changed in the last 18 months that make this bet
possible where it wasn't before:

1. **Long-context models are good enough that whole-file prose can
   live in the agent's working memory cheaply.** Five years ago this
   architecture was hypothetical because the context window couldn't
   hold the prose layer.
2. **MCP became a thing.** A standardised protocol for agents to read
   structured context from a separate process means we don't have to
   convince every agent vendor to integrate. They already integrate
   with anything that speaks MCP.
3. **Coding agents went from demo to daily.** A year ago, building
   for "the agent" was speculative. Now teams notice the
   hallucination tax every day, and they're looking for the missing
   piece. We think the missing piece is the artifact, not the model.

If any of these reverse — if context windows shrink, if MCP loses,
if agents fall back to a different paradigm — the bet weakens. We
should keep an eye on them.

---

## The honest part

The biggest risk isn't any specific failure mode. It's that **prose
is good but unnecessary.** Agents are getting better at reading code
directly. Context windows are growing. Tooling like Serena and aider
does graph-aware code reading without the prose artifact. Our bet is
that the prose layer is _qualitatively_ different from "smarter code
reading," not quantitatively better at the same thing.

The metric that actually answers that: do trie-augmented agents
plateau higher than code-reading-with-better-tools? Not "do they
beat naked grep" — that's table stakes. Do they beat the best
non-prose competitor?

If yes, we have a category. If no, we have a feature, and we should
shelf and join one of the teams that's winning the search race.

This document exists so we can come back to it in six months and
ask: which ring are we actually in? If we're stuck at Ring 1, the
honest move is to stop. The thing worth building is Rings 2 and 3,
or nothing.
