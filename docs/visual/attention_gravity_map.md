# Attention Gravity Map (AGM)

## Product Requirements Document

Version: 2.0

Status: Prototype Design

---

# Executive Summary

Attention Gravity Map (AGM) is a real-time visualization system for AI agents operating on large codebases.

Unlike traditional code visualizations, AGM does not attempt to show repository structure.

Instead, AGM visualizes the agent's current cognitive state projected onto the repository.

The repository graph acts as topology.

Roles act as geography.

Agent events inject energy.

Attention flows through the system.

Users observe reasoning rather than architecture.

The primary design goal is:

> Allow a human observer to understand what an AI agent is thinking about without reading logs, prompts, traces, or source code.

---

# Core Principle

Visualize attention.

Not code.

Not dependencies.

Not architecture.

Not UML.

Not repository structure.

The repository graph exists only as a substrate upon which attention propagates.

The user should perceive:

```text
Authentication is active
Session management is under investigation
The agent is converging on Redis
```

rather than:

```text
SessionStore imports RedisClient
```

---

# Existing Inputs

The system already possesses the necessary telemetry.

## Repository Graph

Generated from Tree-sitter indexing.

Contains:

```text
Symbols
Dependencies
Ownership
Qualified Names
```

---

## Roles

Every symbol belongs to one or more roles.

Examples:

```text
Authentication
Payments
Search
Analytics
Infrastructure
Caching
Observability
```

Roles are manually curated and already exist.

Roles are first-class entities.

Roles are the primary unit of visualization.

---

## Agent Events

Current telemetry:

```text
grep
read
trace
```

All events are associated with symbol qualified names.

Example:

```python
Event(
    type="read",
    qname="auth.session.SessionStore.get"
)
```

These events form the foundation of the entire system.

---

# Mental Model

The visualization behaves like a universe.

The universe contains:

```text
Roles
Symbols
Investigations
Attention
```

Roles are continents.

Symbols are cities.

Attention is weather.

Investigations are storms.

The user primarily perceives movement of attention across roles.

Symbols become visible only when necessary.

---

# Design Goals

Users should answer within five seconds:

- What is the agent working on?
- Which subsystem is active?
- What recently became important?
- What is being investigated?
- Is the investigation converging?

Without:

- reading logs
- opening traces
- inspecting prompts
- understanding repository structure

---

# System Hierarchy

The system operates at three layers.

```text
Role Layer
    ↓

Symbol Layer
    ↓

Reasoning Layer
```

---

# Layer 1: Role Layer

Default view.

Always visible.

Example:

```text
Authentication ██████████

Infrastructure ███████

Observability ██

Payments █
```

The user should spend most of their time here.

Role heat communicates system activity.

---

# Layer 2: Symbol Layer

Visible only inside active roles.

Example:

```text
Authentication

SessionStore ████████

AuthService █████

LoginRoute ██
```

Shows local activity.

---

# Layer 3: Reasoning Layer

Visible on demand.

Contains:

```text
Reads
Greps
Traces
Search Results
Tool Outputs
```

Used for deep inspection.

---

# Repository Graph

Generated from Tree-sitter.

Node types:

```text
Package
Module
File
Class
Method
Function
Endpoint
Schema
Table
```

Relationships:

```text
contains
imports
calls
references
inherits
implements
depends_on
```

This graph is never fully rendered.

It serves only as topology for attention propagation.

---

# Role System

Roles are primary objects.

Examples:

```text
Authentication
Payments
Search
Infrastructure
Caching
Analytics
```

Each role acts as a gravitational body.

Role positions remain relatively stable.

Roles define the geography of the universe.

---

# Symbol Assignment

Symbols belong to one or more roles.

Example:

```text
Authentication

 ├ LoginRoute
 ├ AuthService
 ├ SessionStore
 └ TokenValidator
```

Mass can accumulate simultaneously on:

- symbols
- roles

---

# Event Interpretation

The three telemetry events represent distinct cognitive stages.

---

## Grep

Meaning:

```text
Exploration
```

The agent suspects relevance.

Example:

```python
grep_weight = 10
```

Interpretation:

> This might matter.

---

## Read

Meaning:

```text
Attention Commitment
```

The agent spends context budget.

Example:

```python
read_weight = 40
```

Interpretation:

> This is worth understanding.

---

## Trace

Meaning:

```text
Explanation
```

The symbol participates in causal reasoning.

Example:

```python
trace_weight = 80
```

Interpretation:

> This explains something important.

Trace events represent the strongest signal currently available.

---

# Attention Mass

The system's primary metric.

Each symbol maintains:

```python
symbol_attention_mass
```

Example:

```python
mass =
    grep_count * 10 +
    read_count * 40 +
    trace_count * 80
```

---

# Role Attention Mass

Roles accumulate attention from symbols.

Example:

```python
Authentication.mass += SessionStore.mass
Authentication.mass += AuthService.mass
Authentication.mass += LoginRoute.mass
```

Role mass is derived.

Not manually assigned.

---

# Heat Model

Maintain:

```python
symbol_heat[qname]
```

and

```python
role_heat[role]
```

Events add heat.

Heat decays continuously.

```python
heat *= 0.995
```

per tick.

---

# Attention Propagation

Attention spreads through the graph.

Example:

```text
SessionStore
```

receives:

```python
+100
```

Nearby symbols receive:

```python
neighbor_gain =
    source_heat *
    edge_weight *
    propagation_factor
```

Result:

```text
RedisClient +20

AuthService +15

SessionToken +10
```

The graph begins anticipating future reasoning.

---

# Edge Weights

Suggested defaults:

```text
trace            1.0
calls            1.0
inherits         0.9
implements       0.8
references       0.7
imports          0.5
contains         0.2
```

---

# Role-to-Role Flow

The system should derive attention transfer.

Example:

```text
Authentication
    →
Infrastructure

Infrastructure
    →
Observability
```

These transitions emerge from trace paths.

---

# Attention Graph

Maintain a separate graph.

Repository graph:

```text
possible relationships
```

Attention graph:

```text
actual reasoning paths
```

Example:

```text
LoginRoute
    ⇒
AuthService

AuthService
    ⇒
SessionStore

SessionStore
    ⇒
RedisClient
```

The attention graph is more important than the repository graph.

---

# Trace Path Storage

Store transitions.

```python
AttentionEdge(
    source,
    target,
    timestamp
)
```

Heat accumulates on edges.

Example:

```python
edge_heat[(source,target)]
```

---

# Gravity System

Mass determines attraction.

Objects with greater mass move closer to the attention center.

---

# Attention Center

The center is not the agent.

The center is the weighted centroid of attention.

Example:

```text
SessionStore 300

RedisClient 200

AuthService 50
```

The center naturally shifts toward SessionStore.

The visualization follows thought.

---

# Role Gravity

Roles act as massive bodies.

Example:

```text
Authentication
```

pulls:

```text
SessionStore
AuthService
LoginRoute
```

toward itself.

Roles provide stability.

Symbols provide motion.

---

# Stable Geography

Roles should not rearrange constantly.

Authentication should remain near Authentication.

Payments should remain near Payments.

Infrastructure should remain near Infrastructure.

Only local attention changes.

The universe remains learnable.

---

# Symbol Motion

Symbols move according to:

```text
Role Gravity
+
Attention Gravity
+
Dependency Attraction
+
Repulsion
```

---

# Repulsion

All nodes repel.

Purpose:

Prevent visual collapse.

Maintain readability.

---

# Investigation Nodes

Synthetic entities.

Example:

```text
Fix Login Timeout
```

Relationships:

```text
Fix Login Timeout

 ├ SessionStore
 ├ RedisClient
 ├ LoginRoute
```

Investigations become temporary gravity wells.

---

# Investigation Confidence

Evidence increases confidence.

```python
confidence += evidence
```

Higher confidence produces:

```text
Stronger attraction
Tighter clusters
Reduced uncertainty
```

Users can observe convergence.

---

# Negative Evidence

Support hypothesis elimination.

Example:

```text
Not AuthService
```

Apply:

```python
attention_mass -= 100
```

Node drifts outward.

Rejected hypotheses become visible.

---

# Uncertainty Visualization

Wide distribution:

```text
Auth

Billing

Redis

Search
```

Means:

```text
Low confidence
```

Tight cluster:

```text
SessionStore

RedisClient

CacheConfig
```

Means:

```text
High confidence
```

---

# Visibility Rules

Do not render entire repository.

Render only active universe.

---

## Hidden

```python
mass < threshold
```

Invisible.

---

## Visible

```python
mass >= threshold
```

Rendered.

---

## Dominant

```python
mass >= dominant_threshold
```

Large labels.

Priority rendering.

---

# Progressive Emergence

Initial state:

```text
Authentication

Payments

Infrastructure
```

No symbols.

---

After exploration:

```text
Authentication

  LoginRoute

  AuthService
```

---

After investigation:

```text
Authentication

  SessionStore

  AuthService

Infrastructure

  RedisClient
```

The graph emerges from activity.

---

# Attention Trails

Store historical positions.

Render fading paths.

Purpose:

Visualize movement of reasoning.

---

# Zoom Levels

Level 0

```text
Roles
```

---

Level 1

```text
Roles + Active Symbols
```

---

Level 2

```text
Detailed Symbol Graph
```

---

Level 3

```text
Reasoning Events
```

---

# Performance Requirements

Repository size:

```text
100k+ symbols
```

Visible symbols:

```text
20-100
```

Visible roles:

```text
10-50
```

Rendering must scale independently of repository size.

---

# Success Criteria

A successful implementation causes users to say:

> The agent is investigating Authentication and converging on SessionStore.

Not:

> I can see the dependency graph.

The user's mental model should be:

```text
attention
reasoning
investigation
convergence
```

rather than:

```text
files
imports
dependencies
architecture
```

---

# Future Extensions

- Multi-agent universes
- Shared investigations
- Attention replay
- Time travel mode
- Attention forecasting
- Concept emergence
- Human + AI collaborative maps
- Production telemetry overlays
- Incident replay
- Long-term cognitive memory
- Repository evolution timelines

Long-term, AGM should become a navigable representation of agent cognition where roles provide geography, symbols provide detail, investigations provide narrative, and attention provides motion.
