from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path

from trie import __version__
from trie.config import Config
from trie.models import ModelClient
from trie.parse.python import extract_symbols
from trie.sync.generator import FileGenerationContext, generate_section
from trie.sync.writer import TriefactFile


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


def sync_single_file(
    source_path: Path,
    *,
    project_root: Path,
    config: Config,
    client: ModelClient,
    dest_triefact_path: Path | None = None,
) -> FileSyncResult:
    """Generate or refresh the triefact file for a single Python source file.

    Existing hand-written prose between trie:section sentinels is preserved. Sections for
    public symbols are upserted; sections for symbols no longer in the source are removed.
    Private symbols (leading underscore) are not generated in v0.1.

    If `dest_triefact_path` is provided, the rendered triefact is written there instead of
    the canonical `<triefacts.root>/<source>.md` path. The existing canonical triefact is
    still used as the load source so human prose between sentinels is preserved. This is
    how `trie diff` writes previews to `.trie/preview/` without clobbering the live tree.
    """
    source_path = source_path.resolve()
    project_root = project_root.resolve()
    src_root = (project_root / config.triefacts.source_root).resolve()

    if not source_path.is_relative_to(src_root):
        raise ValueError(f"Source file {source_path} is not under source_root {src_root}")

    source_text = source_path.read_text()
    file_fp = _file_fingerprint(source_text)
    rel_path = str(source_path.relative_to(src_root))

    symbols = extract_symbols(source_path, source_root=src_root)
    public_symbols = [s for s in symbols if s.is_public]

    canonical_triefact_path = _triefact_path_for(source_path, project_root, config)
    write_path = dest_triefact_path if dest_triefact_path is not None else canonical_triefact_path
    triefact = (
        TriefactFile.parse(canonical_triefact_path.read_text())
        if canonical_triefact_path.exists()
        else TriefactFile.empty()
    )

    file_ctx = FileGenerationContext(file_path=rel_path, source_text=source_text)

    totals = {"in": 0, "out": 0, "cache_create": 0, "cache_read": 0}
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

    current_qnames = {s.qualified_name for s in public_symbols}
    sections_removed = 0
    for stale_qname in list(triefact.section_qnames()):
        if stale_qname not in current_qnames:
            triefact.remove_section(stale_qname)
            sections_removed += 1

    triefact.front_matter = {
        "trie_version": __version__,
        "source": rel_path,
        "file_fingerprint": file_fp,
    }

    write_path.parent.mkdir(parents=True, exist_ok=True)
    write_path.write_text(triefact.render())

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
