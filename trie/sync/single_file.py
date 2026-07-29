from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import UTC, datetime
from hashlib import sha256
from pathlib import Path

from trie import __version__, telemetry
from trie.config import Config
from trie.git_helpers import compute_blob_hash, retrieve_blob
from trie.graph.store import Store
from trie.models import TrieClient
from trie.parse import registry
from trie.parse.python import (
    extract_module_docstring,
    strip_string_literal,
)
from trie.parse.types import Symbol
from trie.scope import discover_files
from trie.sync.generator import FileGenerationContext, GeneratedSection, generate_section
from trie.sync.writer import Section, TriefactFile, extract_one_liner


def backfill_section_records(
    project_root: Path,
    config: Config,
    store: Store,
) -> None:
    """Populate triefact_sections records from existing triefact files.

    Reads every triefact on disk and ensures a ``triefact_sections`` record
    exists for every section. Idempotent — re-runs are safe (upsert is no-op
    for already-recorded sections).
    """
    src_root = (project_root / config.triefacts.source_root).resolve()
    for source_path in discover_files(project_root, config.scope):
        if not source_path.is_relative_to(src_root):
            continue
        if not registry.is_indexable(source_path):
            continue
        triefact_path = _triefact_path_for(source_path, project_root, config)
        if not triefact_path.exists():
            continue
        triefact = TriefactFile.parse(triefact_path.read_text())
        triefact_rel_path = str(triefact_path.relative_to(project_root))
        for qn in triefact.section_qnames():
            section = triefact.get_section(qn)
            if section is not None:
                store.upsert_section_record(
                    triefact_path=triefact_rel_path,
                    symbol_qname=qn,
                    section_fingerprint=section.fingerprint or "",
                    one_liner=extract_one_liner(section.body),
                    # Restore the role tag from the persisted sentinel so a graph.db
                    # rebuild recovers roles from disk without re-running the LLM.
                    role=section.role,
                )


@dataclass(frozen=True)
class FileSyncResult:
    source_path: Path
    triefact_path: Path
    symbols_generated: int
    sections_removed: int
    input_tokens: int
    output_tokens: int
    cache_creation_input_tokens: int
    cache_read_input_tokens: int
    symbols_skipped: int = 0
    """Symbols whose existing sections were left untouched because they were not in
    `symbols_to_regen`. Always 0 when `symbols_to_regen` is None (full-file regen)."""


@dataclass(frozen=True)
class MetadataRefreshResult:
    """Outcome of `refresh_triefact_metadata` for one file.

    `changed` is True when the rewritten triefact bytes differ from the previous
    bytes — useful for callers that want to report "N triefacts updated" without
    re-reading the files."""

    triefact_path: Path
    changed: bool


@dataclass(frozen=True)
class _SymbolJob:
    """One per-symbol unit of work scheduled into the generate-phase thread pool.

    Pure data: the symbol to document plus the optional previous-source / previous-prose
    pair that selects diff-aware vs cold-write mode in `generate_section`. Constructed in
    the plan phase from already-resolved inputs so the pool worker only does the LLM call.
    """

    symbol: Symbol
    previous_source: str | None
    previous_prose: str | None


def _file_fingerprint(text: str) -> str:
    return sha256(text.encode("utf-8")).hexdigest()


def _triefact_path_for(source_path: Path, project_root: Path, config: Config) -> Path:
    src_root = (project_root / config.triefacts.source_root).resolve()
    triefacts_root = project_root / config.triefacts.root
    rel = source_path.resolve().relative_to(src_root)
    return triefacts_root / rel.with_suffix(".md")


def _file_description(source_path: Path) -> str | None:
    """One-line description of the file derived from its module docstring, if any.

    The first non-empty line of the docstring is returned, trimmed. None when the
    file has no module docstring. This is the cheapest possible "what does this file
    do" surface — no LLM call, no hand-curation.
    """
    # Module-docstring extraction is Python-grammar specific. Other languages
    # surface a file description differently (or not at all in this pass).
    backend = registry.get_backend_for_file(source_path)
    if backend is None or backend.name != "python":
        return None
    raw = extract_module_docstring(source_path)
    if raw is None:
        return None
    text = strip_string_literal(raw)
    for line in text.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped
    return None


def _build_defines(symbols: list[Symbol]) -> list[dict[str, object]]:
    """List of `{kind, qualified_name, lines}` entries — one per documented symbol.

    Surfaces the symbol roster as an agent-navigable index without re-parsing the
    triefact's section sentinels. Sorted by start_line so the order matches the source.
    """
    return [
        {
            "kind": s.kind,
            "qualified_name": s.qualified_name,
            "lines": f"{s.start_line}-{s.end_line}",
        }
        for s in sorted(symbols, key=lambda x: x.start_line)
    ]


def _resolve_previous_symbols(
    *,
    source_path: Path,
    src_root: Path,
    project_root: Path,
    existing_section_refs: dict[str, str],
) -> dict[str, Symbol]:
    """Look up previous-version Symbols for each qname whose section has a source_ref.

    For each (qname → blob_hash) entry, retrieve the blob from git and re-parse it.
    Returns a dict mapping qname → the matching Symbol from the previous file content,
    skipping qnames that can't be resolved (blob unreachable, file restructured so the
    qname doesn't appear, parse error, etc).

    Groups lookups by unique blob hash so a file with N symbols all stamped against the
    same prior blob results in one git call and one parse, not N. In the common case
    (whole file re-synced after a single edit) the per-symbol overhead collapses to a
    single dict lookup.
    """
    if not existing_section_refs:
        return {}
    # Group qnames by blob_hash to dedupe git calls and parse passes.
    qnames_by_blob: dict[str, list[str]] = {}
    for qname, blob in existing_section_refs.items():
        qnames_by_blob.setdefault(blob, []).append(qname)

    out: dict[str, Symbol] = {}
    for blob_hash, qnames in qnames_by_blob.items():
        previous_text = retrieve_blob(project_root, blob_hash)
        if previous_text is None:
            continue
        try:
            previous_symbols = registry.extract_symbols(
                source_path, source_root=src_root, source_text=previous_text
            )
        except Exception:
            # Tree-sitter can choke on truly malformed previous content (a file that
            # used to be something other than Python, say). Degrade to cold for that
            # blob; the other blobs in this file still have a chance.
            continue
        by_qname = {s.qualified_name: s for s in previous_symbols}
        for q in qnames:
            sym = by_qname.get(q)
            if sym is not None:
                out[q] = sym
    return out


def refresh_triefact_metadata(
    source_path: Path,
    *,
    project_root: Path,
    config: Config,
    store: Store | None = None,
) -> MetadataRefreshResult:
    """Refresh a triefact's front matter from the live store; never call the LLM.

    Use case: the reference graph changed (new resolver, new edges) but no source
    file did. Section bodies and section fingerprints are functions of source
    only, so they stay byte-identical. The front matter's `incoming_refs` /
    `outgoing_refs` / `defines` are derived from the live store, so those need a
    refresh to reflect reality.

    What's intentionally NOT touched:

    - Section bodies — written exactly as before.
    - Section fingerprints (the `fingerprint=...` in each section sentinel).
    - `last_synced_at` — semantically reserved for "the LLM ran"; leaving it
      stable preserves the audit trail.
    - `file_fingerprint` — re-derived from the current source, which we re-read.
      In practice this is unchanged when source didn't change; recomputing keeps
      the field honest if the file *did* change between scans without us noticing.

    Returns `MetadataRefreshResult(changed=True)` when the rewritten bytes
    differ from what was on disk. When the triefact doesn't exist (e.g. a source
    file with no triefact yet), this is a no-op returning `changed=False`.
    """
    source_path = source_path.resolve()
    project_root = project_root.resolve()
    src_root = (project_root / config.triefacts.source_root).resolve()
    if not source_path.is_relative_to(src_root):
        raise ValueError(f"Source file {source_path} is not under source_root {src_root}")

    triefact_path = _triefact_path_for(source_path, project_root, config)
    if not triefact_path.exists():
        # No triefact for this source — nothing to refresh. Callers should treat
        # this as "fine, skip" rather than as an error.
        return MetadataRefreshResult(triefact_path=triefact_path, changed=False)

    rel_path = str(source_path.relative_to(src_root))
    source_text = source_path.read_text()
    file_fp = _file_fingerprint(source_text)
    target_symbols = registry.extract_symbols(source_path, source_root=src_root)

    triefact = TriefactFile.parse(triefact_path.read_text())
    previous_bytes = triefact.render().encode("utf-8")

    # Preserve the existing `last_synced_at` if there is one — only set the
    # default when the triefact is unsynced. We never bump it from this path.
    previous_synced_at = (
        triefact.front_matter.get("last_synced_at") if triefact.front_matter else None
    )

    new_front_matter: dict[str, object] = {
        "trie_version": __version__,
        "source": rel_path,
        "file_fingerprint": file_fp,
    }
    if isinstance(previous_synced_at, str):
        new_front_matter["last_synced_at"] = previous_synced_at
    description = _file_description(source_path)
    if description is not None:
        new_front_matter["description"] = description
    if target_symbols:
        new_front_matter["defines"] = _build_defines(target_symbols)
    if store is not None:
        inbound, outbound = store.file_ref_counts(rel_path)
        new_front_matter["incoming_refs"] = inbound
        new_front_matter["outgoing_refs"] = outbound

    triefact.front_matter = new_front_matter
    new_bytes = triefact.render().encode("utf-8")
    changed = new_bytes != previous_bytes
    if changed:
        triefact_path.write_text(triefact.render())

    # Backfill section one-liner records so the graph DB stays in sync with the
    # triefact file on disk. This handles the case where triefact files were
    # generated by an older version that didn't populate triefact_sections, or
    # where section records were lost (e.g. schema migration, DB reset).
    if store is not None:
        triefact_rel_path = str(triefact_path.relative_to(project_root))
        for qn in triefact.section_qnames():
            section = triefact.get_section(qn)
            if section is not None:
                store.upsert_section_record(
                    triefact_path=triefact_rel_path,
                    symbol_qname=qn,
                    section_fingerprint=section.fingerprint or "",
                    one_liner=extract_one_liner(section.body),
                )

    return MetadataRefreshResult(triefact_path=triefact_path, changed=changed)


def sync_single_file(
    source_path: Path,
    *,
    project_root: Path,
    config: Config,
    client: TrieClient,
    dest_triefact_path: Path | None = None,
    store: Store | None = None,
    symbols_to_regen: set[str] | None = None,
    force: bool = False,
) -> FileSyncResult:
    """Generate or refresh the triefact file for a single Python source file.

    Existing hand-written prose between trie:section sentinels is preserved. Sections are
    upserted for every parser-surfaced symbol that's targeted for regeneration; sections
    for symbols no longer in the source are removed.

    `symbols_to_regen` controls which symbols actually hit the LLM:
      - `None` → regenerate every symbol the parser surfaces. This is the explicit-force
        path, used by `trie sync --file X` and bootstrap. The caller is asking for a
        full rewrite of this file.
      - A set of qnames → regenerate only the listed symbols. Every other symbol's
        existing section is passed through byte-identically (no LLM call, no rewrite).
        This is the symbol-level path: combined with per-symbol staleness from
        `check_project` and per-symbol cascade from `compute_cascade`, the caller can
        target exactly the symbols whose source changed or whose dependencies did,
        leaving the rest of a possibly-large file untouched.

    Qnames in `symbols_to_regen` that don't appear in the current source are silently
    ignored (the symbol was renamed or removed; its orphan section is handled by the
    file-level orphan sweep below).

    If `dest_triefact_path` is provided, the rendered triefact is written there instead of
    the canonical `<triefacts.root>/<source>.md` path. The existing canonical triefact is
    still used as the load source so human prose between sentinels is preserved. This is
    how `trie diff` writes previews to `.trie/preview/` without clobbering the live tree.

    When `store` is provided, the front matter is enriched with cross-file reference
    counts. When omitted, the agent-navigation metadata still lands (defines list,
    description, timestamps), only the ref counts are skipped — useful for callers that
    want to render a triefact without spinning up the SQLite store.

    Per-symbol generation runs through a thread pool bounded by `config.sync.concurrency`
    (default 4). The plan/generate/apply split means the triefact and store are only
    mutated on the calling thread; only `generate_section` (a network round-trip) runs
    in parallel. Setting concurrency to 1 yields fully deterministic serial execution.

    `force` skips the diff-aware path entirely for every symbol: previous source and
    previous prose are ignored so all sections are regenerated cold. Use this when the
    existing prose is known to be wrong and you want a fresh LLM pass regardless of
    whether the source has changed.
    """
    source_path = source_path.resolve()
    project_root = project_root.resolve()
    src_root = (project_root / config.triefacts.source_root).resolve()

    if not source_path.is_relative_to(src_root):
        raise ValueError(f"Source file {source_path} is not under source_root {src_root}")

    source_text = source_path.read_text()
    file_fp = _file_fingerprint(source_text)
    rel_path = str(source_path.relative_to(src_root))

    with telemetry.timed(
        "sync_file", path=rel_path, model=getattr(client, "full_model_id", "")
    ) as tele:
        # Every parser-surfaced symbol gets a section. The `is_public` flag (leading
        # underscore by convention) is kept as descriptive metadata on Symbol but is
        # NOT used as a filter — stale prose is stale regardless of author intent,
        # and the cascade walks edges to/from every symbol uniformly.
        target_symbols = registry.extract_symbols(source_path, source_root=src_root)

        canonical_triefact_path = _triefact_path_for(source_path, project_root, config)
        write_path = (
            dest_triefact_path if dest_triefact_path is not None else canonical_triefact_path
        )
        triefact = (
            TriefactFile.parse(canonical_triefact_path.read_text())
            if canonical_triefact_path.exists()
            else TriefactFile.empty()
        )

        file_ctx = FileGenerationContext(file_path=rel_path, source_text=source_text)

        # Diff-aware regen wiring. The blob hash for the *current* file is stamped
        # into every section we (re)generate so the next sync can retrieve "what
        # this prose was written against." Existing sections whose `source_ref` is
        # populated drive lookups for previous-source bodies via git.
        current_blob = compute_blob_hash(source_path)
        existing_sections: dict[str, Section] = {
            qn: triefact.get_section(qn)  # type: ignore[misc]
            for qn in triefact.section_qnames()
            if triefact.get_section(qn) is not None
        }
        existing_refs = {
            qn: sec.source_ref
            for qn, sec in existing_sections.items()
            if sec.source_ref is not None
        }
        previous_symbols = _resolve_previous_symbols(
            source_path=source_path,
            src_root=src_root,
            project_root=project_root,
            existing_section_refs=existing_refs,
        )

        totals = {"in": 0, "out": 0, "cache_create": 0, "cache_read": 0}
        mode_counts: dict[str, int] = {"cold": 0, "diff_aware": 0}
        triefact_rel_path = str(canonical_triefact_path.relative_to(project_root))
        symbols_generated = 0
        symbols_skipped = 0

        # Phase 1 — plan. Walk the symbol list once and partition into skips (no LLM
        # work) and jobs (need a generate_section call). The skip path eagerly does
        # its store-record refresh because it's a cheap, idempotent SQLite write that
        # doesn't fight the parallel phase. Each job carries everything the generator
        # needs so phase 2 is a pure function over the job list.
        jobs: list[_SymbolJob] = []
        for sym in target_symbols:
            qn = sym.qualified_name
            # Symbol-level regen gate: when `symbols_to_regen` is supplied, anything
            # not in the set is a pass-through. Its existing section stays in
            # `triefact.chunks` untouched (we never call `upsert_section` for it),
            # so render emits byte-identical bytes for it. Front-matter timestamps
            # still update because the *file* was looked at.
            if symbols_to_regen is not None and qn not in symbols_to_regen:
                symbols_skipped += 1
                if store is not None:
                    existing_section = existing_sections.get(qn)
                    if existing_section is not None:
                        store.upsert_section_record(
                            triefact_path=triefact_rel_path,
                            symbol_qname=qn,
                            section_fingerprint=existing_section.fingerprint,
                            one_liner=extract_one_liner(existing_section.body),
                        )
                continue

            prev_sym = previous_symbols.get(qn)
            prev_section = existing_sections.get(qn)
            # Diff-aware path requires: previous symbol *source* (signature + body, from
            # the git blob), and previous *prose* (from the existing section). Either
            # missing → cold-write. We reconstruct signature+body the same way generator
            # does for current_source so the two blocks are directly comparable.
            # `force=True` bypasses the diff-aware path entirely: both are set to None
            # so every symbol gets a fresh cold-write regardless of history.
            if force:
                prev_source = None
                prev_prose = None
            else:
                prev_source = (
                    f"{prev_sym.signature}:\n{prev_sym.body_text}" if prev_sym is not None else None
                )
                prev_prose = prev_section.body if prev_section is not None else None
            jobs.append(
                _SymbolJob(symbol=sym, previous_source=prev_source, previous_prose=prev_prose)
            )

        # Phase 2 — generate. The per-symbol LLM call is pure network I/O; threads
        # are sufficient. Every call shares the same `file_ctx`, which is sent as a
        # cached prefix (system prompt + file source). Anthropic's prompt cache is
        # keyed on that prefix, so after it's written once, every subsequent symbol
        # in the file reads it instead of re-billing the full prefix.
        #
        # CRITICAL: the cache write must land before the parallel fan-out, or every
        # concurrent request races to write its own copy of the cache (each billed
        # at the 1.25x cache-creation rate) and only the stragglers get a read. We
        # therefore generate the FIRST symbol serially to warm the cache, then
        # parallelise the rest — guaranteeing one write and N-1 reads per file.
        #
        # `concurrency=1` collapses to serial execution (a 1-thread pool is still a
        # pool but adds no parallelism), useful for deterministic eval runs and for
        # disabling the path entirely without a code change.
        concurrency = max(1, config.sync.concurrency)
        generated: list[tuple[Symbol, GeneratedSection]] = []
        if jobs:

            def _gen(job: _SymbolJob) -> GeneratedSection:
                return generate_section(
                    symbol=job.symbol,
                    file_ctx=file_ctx,
                    client=client,
                    previous_source=job.previous_source,
                    previous_prose=job.previous_prose,
                )

            if concurrency > 1 and len(jobs) > 1:
                # Warm the prompt cache with the first symbol, serially.
                generated.append((jobs[0].symbol, _gen(jobs[0])))
                rest = jobs[1:]
                with ThreadPoolExecutor(max_workers=concurrency) as pool:
                    futures = [pool.submit(_gen, job) for job in rest]
                    for job, fut in zip(rest, futures, strict=True):
                        generated.append((job.symbol, fut.result()))
            else:
                # Serial path (concurrency=1 or a single symbol): no fan-out, so
                # the cache warms naturally on the first call.
                for job in jobs:
                    generated.append((job.symbol, _gen(job)))

        # Phase 3 — apply. All mutation of `triefact` and `store` happens on this
        # thread; neither is safe to touch concurrently. We process generated
        # sections in source order so the resulting `chunks` layout is identical to
        # the pre-parallelisation serial path.
        for sym, gen in generated:
            qn = sym.qualified_name
            mode_counts[gen.mode] += 1
            # Role stability: `role` is a fresh LLM classification every run and is
            # non-deterministic — the same unchanged symbol can flip between two
            # valid labels across syncs, creating pure regeneration churn (a role
            # change with an identical body_fp and source_ref) that slips past the
            # intent gate. When the regenerated prose is byte-identical to the
            # previous section's prose, the symbol genuinely didn't change, so we
            # carry the previous role forward instead of the freshly-classified
            # one. A real body change still re-classifies.
            prev_section = existing_sections.get(qn)
            effective_role = gen.role
            if prev_section is not None and prev_section.body == gen.body and prev_section.role:
                # Body unchanged → keep the previously-assigned role verbatim.
                # (Boundary is not persisted in the section sentinel, so only the
                # role is stabilised here; the store record below uses gen.boundary.)
                effective_role = prev_section.role
            triefact.upsert_section(
                qualified_name=qn,
                fingerprint=sym.body_normalized_hash,
                body=gen.body,
                source_ref=current_blob,
                role=effective_role,
            )
            symbols_generated += 1
            totals["in"] += gen.input_tokens
            totals["out"] += gen.output_tokens
            totals["cache_create"] += gen.cache_creation_input_tokens
            totals["cache_read"] += gen.cache_read_input_tokens
            if store is not None:
                section = triefact.get_section(qn)
                if section is not None:
                    store.upsert_section_record(
                        triefact_path=triefact_rel_path,
                        symbol_qname=qn,
                        section_fingerprint=sym.body_normalized_hash,
                        one_liner=extract_one_liner(section.body),
                        role=effective_role,
                        boundary=gen.boundary,
                    )

        current_qnames = {s.qualified_name for s in target_symbols}
        sections_removed = 0
        for stale_qname in list(triefact.section_qnames()):
            if stale_qname not in current_qnames:
                triefact.remove_section(stale_qname)
                sections_removed += 1

        # Re-sort section chunks into source-line order so the triefact mirrors the
        # source file layout.  Symbols added incrementally across multiple syncs
        # would otherwise accumulate at the end of the file regardless of where
        # they appear in source.
        start_line_by_qname = {s.qualified_name: s.start_line for s in target_symbols}
        triefact.sort_sections(start_line_by_qname)

        front_matter: dict[str, object] = {
            "trie_version": __version__,
            "source": rel_path,
            "file_fingerprint": file_fp,
            "last_synced_at": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        description = _file_description(source_path)
        if description is not None:
            front_matter["description"] = description
        if target_symbols:
            front_matter["defines"] = _build_defines(target_symbols)
        if store is not None:
            inbound, outbound = store.file_ref_counts(rel_path)
            front_matter["incoming_refs"] = inbound
            front_matter["outgoing_refs"] = outbound

        triefact.front_matter = front_matter

        write_path.parent.mkdir(parents=True, exist_ok=True)
        write_path.write_text(triefact.render())

        # Post-write backfill: ensure every section in the triefact has a
        # triefact_sections record. The skip and generate paths above already
        # handle this per-symbol, but this catch-all guarantees consistency
        # across edge cases (e.g. symbols added mid-sync, store passed late).
        if store is not None:
            for qn in triefact.section_qnames():
                section = triefact.get_section(qn)
                if section is not None:
                    store.upsert_section_record(
                        triefact_path=triefact_rel_path,
                        symbol_qname=qn,
                        section_fingerprint=section.fingerprint or "",
                        one_liner=extract_one_liner(section.body),
                        # Preserve the role tag from the persisted sentinel so the
                        # catch-all doesn't blank a role set by the generate path.
                        role=section.role,
                    )

        tele["symbols_generated"] = symbols_generated
        tele["symbols_skipped"] = symbols_skipped
        tele["sections_removed"] = sections_removed
        tele["input_tokens"] = totals["in"]
        tele["output_tokens"] = totals["out"]
        tele["cache_creation_input_tokens"] = totals["cache_create"]
        tele["cache_read_input_tokens"] = totals["cache_read"]
        tele["regen_mode_cold"] = mode_counts["cold"]
        tele["regen_mode_diff_aware"] = mode_counts["diff_aware"]
        tele["has_blob_ref"] = current_blob is not None

        return FileSyncResult(
            source_path=source_path,
            triefact_path=write_path,
            symbols_generated=symbols_generated,
            sections_removed=sections_removed,
            input_tokens=totals["in"],
            output_tokens=totals["out"],
            cache_creation_input_tokens=totals["cache_create"],
            cache_read_input_tokens=totals["cache_read"],
            symbols_skipped=symbols_skipped,
        )
