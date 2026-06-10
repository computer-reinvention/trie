# AGM — Handoff: visual/UX issues to fix next session

Context: the "Sync system retry and rate limiting policy" turn, current build
(commit `771ba1d`). This iteration is close to the intended design — region
halos with uppercase headings render, spokes radiate from a visible centre, the
sidebar collapses to a rail. Remaining issues below, grouped by severity.

Files: `app/src/components/AGMCanvas/index.tsx`, `app/src/agm/layout.ts`,
`app/src/agm/style.ts`.

---

## A. High — structure & the core read

1. **Region halos are enormous and overlap heavily.** AGENT-INTEGRATION, UTIL,
   CONFIG-MANAGEMENT each draw as a large faint circle, and they overlap each
   other and the centre. The halo radius (`Math.hypot(bounds)/2 + 34`) balloons
   when a region's members are spread. Result: overlapping blobs that obscure the
   "distance = relevance" read. Fix: cap halo radius, or base it on member count
   not extent, or draw a softer convex-hull/blob instead of a big circle.

2. **`synthetic/Filesystem` sits dead-centre as the single most prominent node.**
   It's the gravitational centre and the brightest pill — so the headline reads
   "the agent is focused on the filesystem", which is misleading (file reads are
   plumbing). Down-weight/cap synthetic mass or move synthetics to a fixed
   peripheral lane so a real symbol holds the centre.

3. **Two near-duplicate regions: `CONFIG` and `CONFIG-MANAGEMENT`.** They sit
   adjacent and read as redundant. These are two distinct trie roles, but
   visually they should be distinguishable or merged-at-a-glance. Consider role
   de-duplication / clearer separation, or showing the role only once.

4. **Almost everything is an unlabeled dot; very few names.** Only ~8 pills show
   (`_is_retryable`, `_run_with_retry`, `synthetic/Filesystem`, `Sync`, `emit`,
   `_retry_after_seconds`, region headings). The actual focus of THIS turn
   (`_run_with_retry`, `_is_retryable`, `_backoff_delay`, `_retry_after_seconds`,
   `RetryStats`, `configure_inflight_limit`) is mostly dots. The named set should
   surface the turn's real subjects. Revisit the percentile/cap so the hottest
   handful are always named.

5. **The centre is just a faint `+` with the busiest node on top of it.** The
   "attention origin" doesn't read as a meaningful anchor. Give it a subtle ring
   / keep an empty inner radius so nothing sits exactly on it, and ensure the
   hottest REAL symbol orbits just outside it.

---

## B. Medium — distribution & legibility

6. **Angular distribution is lopsided / wasteful.** Regions bunch upper-left
   (AGENT-INTEGRATION, UTIL) and right (CONFIG/CONFIG-MANAGEMENT), with large
   dead space lower-left and a lone LLM-CLIENT region at the bottom. Role base
   angles should spread more evenly so the canvas is used and regions don't pile.

7. **Spokes all converge on the exact centre regardless of which region.** Every
   node draws a line to (0,0), so a node in the bottom LLM-CLIENT region has a
   long spoke crossing the whole canvas to the centre. Reads as a starburst, not
   "relevance radius". Consider: spokes only for hot/visible nodes, or spokes to
   the region centroid rather than the global centre, or fade spoke length.

8. **Region heading vs member legibility.** Headings (UTIL, CONFIG…) are clear,
   but members inside are tiny dots with no grouping cue beyond the faint halo.
   When a region has 1–2 visible members the big halo looks empty/odd
   (e.g. UTIL with just `_is_retryable`).

9. **Dot sizes barely vary** — hard to tell a warm dot from a cold one. Increase
   the dot radius/opacity range with relevance.

---

## C. Low — polish

10. **No trace constellations visible** even though this was a read/trace-heavy
    turn (the transcript cites many reads). Verify attention (trace) edges are
    created + drawn; right now the only lines are radial spokes.

11. **No "focus" affordance.** A caption ("focus: _run_with_retry") or a clear
    brightest-node highlight would nail the 2–3s read.

12. **Lots of empty canvas** — the field occupies maybe 60% of the area; could
    scale the layout to fill more, or zoom-to-fit on settle.

13. **Region halo dashed stroke + fill is subtle** to the point the regions look
    like ghost circles. Either commit to the region styling (a touch more
    presence) or replace with a label-only treatment + faint member tint.

---

## D. Open design questions

- **Synthetics in a fixed peripheral lane?** Strong candidate — keeps real
  symbols central and stops Filesystem from being the headline.
- **Halo shape:** big circle vs. convex hull vs. just a tinted region behind
  members vs. label-only. Big circles overlap badly at this node count.
- **Spoke target:** global centre vs. region centroid vs. drop spokes entirely
  for cold nodes.
- **Named set:** top-N absolute (e.g. always name the 6–8 hottest) instead of a
  percentile, so the turn's real subjects are always labelled.
- **Role spread:** even angular distribution + maybe collapsing near-duplicate
  roles (CONFIG vs CONFIG-MANAGEMENT).

---

## Quick wins to try first

1. Cap region-halo radius (and/or switch to a tinted hull) so regions stop
   overlapping into blobs.
2. Down-weight/cap synthetic-node mass so a real symbol takes the centre; or
   pin synthetics to a peripheral lane.
3. Name the top ~6–8 hottest symbols always (absolute cap), dots for the rest.
4. Even out role base angles; scale layout to fill the canvas.
5. Confirm trace edges render; strengthen dot size/opacity contrast.
</content>
