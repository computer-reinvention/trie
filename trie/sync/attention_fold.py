"""Sync-time historical-mass fold for AGM.

Historical mass is a long-term *cognitive importance* signal: "how often does
agent cognition return to this symbol across investigations?" It is stamped into
the triefact sentinel (`hist_mass=<v>@<ts>`) and updated only here — when
`trie sync` regenerates a file's triefact.

The fold, per symbol with a section in the triefact:

    aged = old_mass · exp(-HISTORICAL_LAMBDA · (now - old_ts))      # 21-day decay
    new  = aged + (# DISTINCT investigations that drew attention to it
                   since the last fold)                              # recurrence

Recurrence — not raw attention magnitude — is what accrues: a symbol hammered in
one investigation but never revisited should not outweigh one returned to lightly
across several investigations. The distinct-investigation counts come from the
compressed attention event store (`trie.attention_store`), which the desktop /
opencode capture path populates live.

This runs against the in-memory `TriefactFile` just before it's rendered to disk,
so the new mass lands in the same write that regenerated the prose — no extra
diff churn. The event store's fold watermark is advanced once per sync run.
"""

from __future__ import annotations

import math
import time
from pathlib import Path

from trie import attention_store
from trie.attention import HISTORICAL_LAMBDA
from trie.sync.writer import TriefactFile


def fold_historical_mass(
    triefact: TriefactFile,
    *,
    project_root: Path,
    now: float | None = None,
    since: float | None = None,
) -> int:
    """Decay-and-accrue historical mass for every section in `triefact`.

    Mutates the triefact in place (via `set_section_historical_mass`) and returns
    the number of sections whose mass changed. Does NOT advance the global fold
    watermark — call `advance_fold_watermark` once after all files in a sync run
    are folded, so every file sees the same `since` window.

    `since` defaults to the store's last-fold watermark; pass an explicit value
    in tests. A symbol with no attention since `since` still gets its stored mass
    decayed forward (so abandoned symbols cool), but only restamped when the
    quantized value actually changes.
    """
    now = time.time() if now is None else now
    since = attention_store.get_last_fold_ts(project_root) if since is None else since

    changed = 0
    for qn in triefact.section_qnames():
        section = triefact.get_section(qn)
        if section is None:
            continue

        aged = _decayed(section.historical_mass, section.historical_mass_ts, now)
        recurrence = len(
            attention_store.investigations_touching_symbol_since(project_root, qn, since=since)
        )
        new_mass = aged + float(recurrence)

        # Restamp only when the quantized (1-decimal) value moves, so quiet syncs
        # don't churn the triefact diff. Always restamp when recurrence > 0 (the
        # ts must advance to anchor future decay).
        if recurrence > 0 or round(new_mass, 1) != round(section.historical_mass, 1):
            triefact.set_section_historical_mass(qn, new_mass, now)
            changed += 1

    return changed


def advance_fold_watermark(project_root: Path, ts: float | None = None) -> None:
    """Record that the fold has consumed events up to `ts` (default: now).

    Called once at the end of a sync run so the next run's recurrence window
    starts here. Best-effort (the store swallows failures)."""
    attention_store.set_last_fold_ts(project_root, time.time() if ts is None else ts)


def _decayed(mass: float, mass_ts: float, now: float) -> float:
    """Exponentially decay `mass` from `mass_ts` to `now` on the historical
    half-life. A zero/unset timestamp means no prior stamp — return mass as-is."""
    if mass <= 0.0 or mass_ts <= 0.0:
        return max(0.0, mass)
    dt = max(0.0, now - mass_ts)
    return mass * math.exp(-HISTORICAL_LAMBDA * dt)
