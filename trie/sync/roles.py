"""Roles-only sync: (re)infer the architectural role tag for every symbol without
regenerating documentation prose.

The role tag drives how symbols are grouped in the graph view (the system model's
role axis). It is produced by the LLM during a full `trie sync`, persisted in the
triefact section sentinel (`role=`) and mirrored into `triefact_sections.role`.

This module exists for two cases:

  - Backfilling roles onto a tree whose triefacts predate role persistence (the
    sentinels carry no `role=`, so a graph rebuild yields `role_count == 1`).
  - Re-classifying after the role vocabulary or prompt changes, cheaply, without
    paying to rewrite prose.

It reads each file's existing triefact, classifies every parser-surfaced symbol
via `infer_role` (a small role-only LLM call that reuses the cached file context),
stamps the role into the sentinel with `set_section_role`, and updates the store.
Prose bodies and fingerprints are never touched, so the resulting diff is minimal.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path

from trie import telemetry
from trie.config import Config
from trie.graph.store import Store
from trie.models import TrieClient
from trie.parse.python import extract_symbols
from trie.scope import discover_files
from trie.sync.generator import FileGenerationContext, InferredRole, infer_role
from trie.sync.progress import NULL_PROGRESS, ProgressCallback
from trie.sync.single_file import FileSyncResult, _triefact_path_for
from trie.sync.taxonomy import (
    Taxonomy,
    TaxonomyResult,
    derive_taxonomy,
    load_taxonomy,
    save_taxonomy,
)
from trie.sync.writer import TriefactFile, extract_one_liner


@dataclass(frozen=True)
class RolesOnlyResult:
    files_processed: int
    symbols_classified: int
    roles_changed: int
    taxonomy_derived: bool
    taxonomy_size: int
    input_tokens: int
    output_tokens: int
    cache_creation_input_tokens: int
    cache_read_input_tokens: int


def run_roles_only(
    *,
    project_root: Path,
    config: Config,
    store: Store,
    client: TrieClient,
    progress: ProgressCallback | None = None,
    rederive_taxonomy: bool = False,
    only_missing: bool = False,
) -> RolesOnlyResult:
    """Infer and persist the role tag for every symbol with an existing triefact.

    Two passes:
      1. Ensure a role taxonomy exists. Loaded from disk if present, derived via the
         LLM and saved otherwise (or always when `rederive_taxonomy` is True).
      2. Classify symbols against that fixed vocabulary, writing changed roles back
         into both the triefact sentinel and the store.

    `only_missing` restricts pass 2 to sections whose role is currently empty — the
    cheap auto-backfill used by the freshness gate to fill gaps left by new symbols
    or legacy triefacts, without re-classifying the whole tree. When every section
    already has a role and `only_missing` is set, no taxonomy is derived and no LLM
    call is made.

    Files without a triefact are skipped (run a full sync first to generate prose).
    """
    cb: ProgressCallback = progress if progress is not None else NULL_PROGRESS
    src_root = (project_root / config.triefacts.source_root).resolve()
    tok_in = tok_out = cache_create = cache_read = 0

    # Cheap short-circuit for the auto-backfill path: if every symbol already has a
    # role, there is nothing to fill — skip taxonomy derivation and all LLM calls.
    if only_missing and store.count_symbols_missing_role() == 0:
        return RolesOnlyResult(
            files_processed=0,
            symbols_classified=0,
            roles_changed=0,
            taxonomy_derived=False,
            taxonomy_size=0,
            input_tokens=0,
            output_tokens=0,
            cache_creation_input_tokens=0,
            cache_read_input_tokens=0,
        )

    # Pass 1 — taxonomy.
    taxonomy: Taxonomy | None = None if rederive_taxonomy else load_taxonomy(project_root, config)
    taxonomy_derived = False
    if taxonomy is None:
        derived: TaxonomyResult = derive_taxonomy(store=store, client=client)
        taxonomy = derived.taxonomy
        save_taxonomy(project_root, config, taxonomy)
        taxonomy_derived = True
        tok_in += derived.input_tokens
        tok_out += derived.output_tokens
        cache_create += derived.cache_creation_input_tokens
        cache_read += derived.cache_read_input_tokens

    allowed_roles = [(r.name, r.description) for r in taxonomy.roles]

    targets = [
        p
        for p in discover_files(project_root, config.scope)
        if p.is_relative_to(src_root) and _triefact_path_for(p, project_root, config).exists()
    ]
    total = len(targets)

    files_processed = 0
    symbols_classified = 0
    roles_changed = 0

    with telemetry.timed("roles_only", files=total, taxonomy_size=len(allowed_roles)):
        for idx, source_path in enumerate(targets):
            rel_path = str(source_path.relative_to(src_root))
            cb.on_start(rel_path, idx, total)

            triefact_path = _triefact_path_for(source_path, project_root, config)
            triefact = TriefactFile.parse(triefact_path.read_text())
            triefact_rel_path = str(triefact_path.relative_to(project_root))

            symbols = extract_symbols(source_path, source_root=src_root)
            file_ctx = FileGenerationContext(
                file_path=rel_path, source_text=source_path.read_text()
            )

            # Classify symbols that have a section in this triefact. With
            # `only_missing`, skip sections that already carry a role so the
            # auto-backfill only touches (and bills for) the gaps. Parallelise the
            # LLM calls; mutate the triefact + store only on this thread.
            jobs = [
                s
                for s in symbols
                if (sec := triefact.get_section(s.qualified_name)) is not None
                and not (only_missing and sec.role)
            ]
            results: list[InferredRole] = []
            if jobs:
                with ThreadPoolExecutor(max_workers=config.sync.concurrency) as pool:
                    futures = [
                        pool.submit(
                            infer_role,
                            symbol=s,
                            file_ctx=file_ctx,
                            client=client,
                            allowed_roles=allowed_roles,
                            existing_prose=_section_prose(triefact, s.qualified_name),
                        )
                        for s in jobs
                    ]
                    results = [f.result() for f in futures]

            for inferred in results:
                symbols_classified += 1
                tok_in += inferred.input_tokens
                tok_out += inferred.output_tokens
                cache_create += inferred.cache_creation_input_tokens
                cache_read += inferred.cache_read_input_tokens

                section = triefact.get_section(inferred.qualified_name)
                if section is None:
                    continue
                if inferred.role and inferred.role != section.role:
                    triefact.set_section_role(inferred.qualified_name, inferred.role)
                    roles_changed += 1
                store.upsert_section_record(
                    triefact_path=triefact_rel_path,
                    symbol_qname=inferred.qualified_name,
                    section_fingerprint=section.fingerprint or "",
                    one_liner=extract_one_liner(section.body),
                    role=inferred.role,
                    boundary=inferred.boundary,
                )

            triefact_path.write_text(triefact.render())
            files_processed += 1

            cb.on_done(
                rel_path,
                FileSyncResult(
                    source_path=source_path,
                    triefact_path=triefact_path,
                    symbols_generated=len(results),
                    sections_removed=0,
                    input_tokens=tok_in,
                    output_tokens=tok_out,
                    cache_creation_input_tokens=cache_create,
                    cache_read_input_tokens=cache_read,
                ),
                0.0,
            )

    return RolesOnlyResult(
        files_processed=files_processed,
        symbols_classified=symbols_classified,
        roles_changed=roles_changed,
        taxonomy_derived=taxonomy_derived,
        taxonomy_size=len(allowed_roles),
        input_tokens=tok_in,
        output_tokens=tok_out,
        cache_creation_input_tokens=cache_create,
        cache_read_input_tokens=cache_read,
    )


def _section_prose(triefact: TriefactFile, qname: str) -> str | None:
    section = triefact.get_section(qname)
    return section.body if section is not None else None
