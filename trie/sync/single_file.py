from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from hashlib import sha256
from pathlib import Path

from trie import __version__, telemetry
from trie.config import Config
from trie.graph.store import Store
from trie.models import ModelClient
from trie.parse.python import (
    Symbol,
    extract_module_docstring,
    extract_symbols,
    strip_string_literal,
)
from trie.sync.generator import FileGenerationContext, generate_section
from trie.sync.writer import TriefactFile, extract_one_liner


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
    raw = extract_module_docstring(source_path)
    if raw is None:
        return None
    text = strip_string_literal(raw)
    for line in text.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped
    return None


def _build_defines(public_symbols: list[Symbol]) -> list[dict[str, object]]:
    """List of `{kind, qualified_name, lines}` entries — one per public symbol.

    Surfaces the symbol roster as an agent-navigable index without re-parsing the
    triefact's section sentinels. Sorted by start_line so the order matches the source.
    """
    return [
        {
            "kind": s.kind,
            "qualified_name": s.qualified_name,
            "lines": f"{s.start_line}-{s.end_line}",
        }
        for s in sorted(public_symbols, key=lambda x: x.start_line)
    ]


def sync_single_file(
    source_path: Path,
    *,
    project_root: Path,
    config: Config,
    client: ModelClient,
    dest_triefact_path: Path | None = None,
    store: Store | None = None,
) -> FileSyncResult:
    """Generate or refresh the triefact file for a single Python source file.

    Existing hand-written prose between trie:section sentinels is preserved. Sections for
    public symbols are upserted; sections for symbols no longer in the source are removed.
    Private symbols (leading underscore) are not generated in v0.1.

    If `dest_triefact_path` is provided, the rendered triefact is written there instead of
    the canonical `<triefacts.root>/<source>.md` path. The existing canonical triefact is
    still used as the load source so human prose between sentinels is preserved. This is
    how `trie diff` writes previews to `.trie/preview/` without clobbering the live tree.

    When `store` is provided, the front matter is enriched with cross-file reference
    counts. When omitted, the agent-navigation metadata still lands (defines list,
    description, timestamps), only the ref counts are skipped — useful for callers that
    want to render a triefact without spinning up the SQLite store.
    """
    source_path = source_path.resolve()
    project_root = project_root.resolve()
    src_root = (project_root / config.triefacts.source_root).resolve()

    if not source_path.is_relative_to(src_root):
        raise ValueError(f"Source file {source_path} is not under source_root {src_root}")

    source_text = source_path.read_text()
    file_fp = _file_fingerprint(source_text)
    rel_path = str(source_path.relative_to(src_root))

    with telemetry.timed("sync_file", path=rel_path, model=client.model_id) as tele:
        symbols = extract_symbols(source_path, source_root=src_root)
        public_symbols = [s for s in symbols if s.is_public]

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

        totals = {"in": 0, "out": 0, "cache_create": 0, "cache_read": 0}
        triefact_rel_path = str(canonical_triefact_path.relative_to(project_root))
        for sym in public_symbols:
            gen = generate_section(symbol=sym, file_ctx=file_ctx, client=client)
            triefact.upsert_section(
                qualified_name=sym.qualified_name,
                fingerprint=sym.body_normalized_hash,
                body=gen.body,
            )
            totals["in"] += gen.input_tokens
            totals["out"] += gen.output_tokens
            totals["cache_create"] += gen.cache_creation_input_tokens
            totals["cache_read"] += gen.cache_read_input_tokens
            # Record the section metadata for cheap MCP lookups (one_liner + fingerprint).
            # The store may be omitted (e.g. tests that don't construct a graph), in which
            # case the agent surface degrades to empty one_liners — still functional.
            if store is not None:
                section = triefact.get_section(sym.qualified_name)
                if section is not None:
                    store.upsert_section_record(
                        triefact_path=triefact_rel_path,
                        symbol_qname=sym.qualified_name,
                        section_fingerprint=sym.body_normalized_hash,
                        one_liner=extract_one_liner(section.body),
                    )

        current_qnames = {s.qualified_name for s in public_symbols}
        sections_removed = 0
        for stale_qname in list(triefact.section_qnames()):
            if stale_qname not in current_qnames:
                triefact.remove_section(stale_qname)
                sections_removed += 1

        front_matter: dict[str, object] = {
            "trie_version": __version__,
            "source": rel_path,
            "file_fingerprint": file_fp,
            "last_synced_at": datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        description = _file_description(source_path)
        if description is not None:
            front_matter["description"] = description
        if public_symbols:
            front_matter["defines"] = _build_defines(public_symbols)
        if store is not None:
            inbound, outbound = store.file_ref_counts(rel_path)
            front_matter["incoming_refs"] = inbound
            front_matter["outgoing_refs"] = outbound

        triefact.front_matter = front_matter

        write_path.parent.mkdir(parents=True, exist_ok=True)
        write_path.write_text(triefact.render())

        tele["symbols_generated"] = len(public_symbols)
        tele["sections_removed"] = sections_removed
        tele["input_tokens"] = totals["in"]
        tele["output_tokens"] = totals["out"]
        tele["cache_creation_input_tokens"] = totals["cache_create"]
        tele["cache_read_input_tokens"] = totals["cache_read"]

        return FileSyncResult(
            source_path=source_path,
            triefact_path=write_path,
            symbols_generated=len(public_symbols),
            sections_removed=sections_removed,
            input_tokens=totals["in"],
            output_tokens=totals["out"],
            cache_creation_input_tokens=totals["cache_create"],
            cache_read_input_tokens=totals["cache_read"],
        )
