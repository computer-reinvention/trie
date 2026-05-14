# trie: code from the future

This is what trie is for. Not what it does. The README covers that. This is
the thing we believe, what follows from it, and where it ends up.

---

## The thing nobody says about coding agents

Coding agents today read code. Code is the executable form of intent, not the
explanatory form. Every time an agent reads `cascade.py` to answer a question,
it's an LLM reconstructing "what does this do and why" from `for` loops and
variable names, under context pressure, with the wrong abstraction. That's
where hallucinations come from. Not a lack of intelligence. The wrong
artifact.

The fix everyone reaches for is "give the agent better tools to read code":
semantic indexing, repo maps, smarter grep. These help. They don't change the
shape of the problem, because the problem isn't that code is hard to find.
It's that code isn't what the agent needs. The agent needs the intent. The
intent is in someone's head, sometimes in a comment, occasionally in a wiki
page that's six months out of date.

trie's claim: **the codebase should describe itself in prose, the description
should be kept in sync by construction, and that description should be the
primary artifact both humans and agents work against.** Code becomes the
executable form of the prose, not its source of truth.

> Code is prose constrained by rules necessary to make it comprehensible
> to machines made of molten sand.

That constraint is what makes code precise. It's also what makes code a
worse medium for the work agents and humans actually do, which is reason
about systems. Prose is the medium of reasoning; code is the medium of
execution. Models are natively better at prose because prose is what
they are made of. Every improvement in their capability amplifies the
medium they were trained on, faster than it improves the constrained
subset. Building on prose is building on the gradient.

---

## What happens

Four rings of effect, outward from the artifact. The first changes how
agents read. The second changes what they can answer. The third changes
what review and authorship are. The fourth changes what programming is.

### Ring 1: Navigation becomes nature

Agents stop grepping. They join paragraphs. Cross-file changes stop being
"open six files and reconstruct the call graph in context window"; they
become "walk the graph, read the relevant sections, change the code."
Hallucinations drop. Answers get sharper on the questions agents already
answer.

Reading the codebase stops being an act of reconstruction. The artifact
the agent reaches for is the one already written in the language of
intent. Navigation is no longer a skill the agent has to deploy under
pressure. It's the shape of the environment.

### Ring 2: The bigger picture becomes the starting point

A class of questions agents could answer today goes unasked. These
questions become casual lookups. The agent's first move stops being
"let me find the function" and becomes "let me understand the shape
of this."

**Blast-radius questions.** "If I change the return type of this function,
what breaks?" Today: agent greps callers, opens each file, infers whether
the change matters from syntax. Often wrong. With trie: one graph walk for
topology, prose-read on the three callers that actually use the return
value, done. The answer the agent gives is
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
architecture diagram every time someone asks. It's reading the one that
was written when the code was written.

**Cross-cutting concern queries.** "Where does this codebase handle auth?"
Today: grep `auth`, get 80 hits, sift. With trie: a semantic index of what
each symbol _does_, ranked, with one-sentence descriptions. The agent
reasons over a curated map, not a string match.

**Onboarding-as-conversation.** A new contributor, human or agent, asks
"where do I start to add a new auth provider?" Today: someone senior
writes a doc that goes stale. With trie: the answer is a chain of reads
that follow the existing auth provider's graph. Always current, always
specific to this codebase.

What these have in common: **the value is in the synthesis, not the
lookup.** Synthesis is the default move. Agents answer a new _category_
of question. Questions that were never reachable before.

### Ring 3: Code, again

Synthesis changes the work itself. The artifact people reach for
inverts; the artifact people argue about inverts; the artifact people
defend inverts. Code stops being the thing under discussion and becomes
the thing under generation.

**Prose becomes primary, code becomes its executable form.** Code is
the lagging shadow now, the place where the description gets compiled
to something the machine can run. A bug becomes "the paragraph said X,
the code does Y, the code is wrong." Specs get written as prose
paragraphs and implemented. **PR review inverts: you're reviewing
intent, not implementation. The code diff is just confirmation that
the change matches its description.**

**Architectural drift becomes visible early.** A change whose prose diff
lights up regions that "shouldn't be related" is the early-warning
signal for coupling that's wrong. Today this is invisible until someone
reviews the whole system holistically (rare) or until it causes pain
(late). With trie, the lit-region pattern shows it on every PR.
Reviewers ask "why did the auth change reach into the parser?" before
it's load-bearing.

**The senior/junior gap narrows on review.** Reviewing a PR
meaningfully has always required already holding the system in your
head. Exactly the population that needs agents the least.
With prose diffs as the primary review surface, a reviewer who has
never seen the repo asks the right question, because the system is
describing itself to them as they read. Senior review stops being a
tenure-locked skill.

**Knowledge stops walking out the door.** The engineer who knows why
the cascade skips hub symbols writes it in the prose. They leave. The
knowledge stays. Today, the same engineer leaves a comment that says
"TODO: explain why" and the institutional memory dies. The prose
layer is a structural fix for tribal knowledge loss. Not because we
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

### Ring 4: Vibes, again

This is the destination. Where the architecture is pointed, where the
choices we make today are choices toward.

Looking at code, line by line, is a thing humans do because the
executable form happens to also be the only durable form the intent
has. With a trustworthy prose layer and a first-class graph, the
executable form stops being the primary surface for human work. We
don't read it. We don't write it directly. We _shape_ the system at
a level above it, and the code conforms.

What that looks like, concretely:

**The IDE goes away.** The default work surface is no longer a text
editor showing a file. It's a navigable representation of the system:
prose, graph, dependencies, invariants. You move through it
spatially. You see the system the way you currently see a city from
above: regions, flows, scale, density. The Tony Stark moment is the
natural interface for working at the level of "what should this
system do" rather than "what should this line say."

**Changes are made by gesture, not by edit.** "Move auth out of the
request path and into a separate middleware tier" is a change you
describe in prose, with the system itself confirming the topology
makes sense before any line of code is touched. The implementation
is a downstream consequence, generated and verified against the
prose. You spend zero time on syntax and full time on architecture.
The protagonist rearranging glowing pieces of a holographic system
is what the work is.

**Code review becomes simulation.** You don't review a diff. You
inspect the proposed _new state of the system_, its prose, its
graph, its invariants, and ask "is this the system we want?" The
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
The next thing someone builds on top of it is a richer rendering,
and the thing after that, and the thing after that. The
prose-graph-fingerprint substrate underneath the glowing-components
moment looks a lot like what we're doing now, enormously refined.

This is the load-bearing constraint on the choices we make today.
Every design decision passes the test: **does this still make sense
in a future where humans stop reading code?** A design choice that
only works while humans are the primary readers of source files is
a design choice with an expiration date.

The intent layer has to be real and trustworthy first. That is the
work.

---

## All or nothing

Each of these has been tried. trie is none of them. Confuse the
distinction and trie collapses into something that has already failed.
These are not adjacent categories where trie is the better version.
They are different categories where the difference is the whole point.

**Not "write better docs."** Docs go stale. Prose that isn't kept in
sync by construction is worse than no prose. The trust collapses
faster than the writing. trie's whole architecture (fingerprints,
cascade, pre-commit verify) exists to remove that failure mode at
the substrate level. The fix is structural, not exhortative.

**Not "comments as documentation."** Comments live in the code, share
its context window, and are read by the same eyes that read the code.
Prose in a separate, navigable, graph-connected tree is a different
artifact for a different reader. The separation matters.

**Not "AI-generated docs."** Generated docs are the failure mode of
this approach, not the goal. The LLM is a scaffolder. The value lives
in the human-edited sentinel sections that capture _why_. The part
LLMs cannot derive from syntax. Prose that is just regurgitated code
is a worse code-reading tool; the architecture refuses it by
construction.

**Not "smarter search."** Semantic search, vector retrieval, repo maps:
these all answer "where is the thing." trie answers "what is the
thing and why is it that way." Search is a lookup mechanism over
code; trie is a parallel artifact in the language of intent. Different
question, different answer, different shape.

**Not a replacement for reading code.** Code is still the source of
truth for behaviour. trie is the source of truth for _intent_. When
they disagree, the bug is real and one of them is wrong. trie's
contribution is making that disagreement legible.
