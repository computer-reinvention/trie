from __future__ import annotations

from pathlib import Path

import pytest

from trie.parse.ts_resolve import TsResolver
from trie.parse.typescript_refs import extract_file_data

FIXTURE = Path(__file__).parent / "fixtures" / "tiny_ts_repo"


@pytest.fixture
def resolver() -> TsResolver:
    return TsResolver.build(FIXTURE)


def _edges(path: Path, resolver: TsResolver) -> set[tuple[str, str, str]]:
    fd = extract_file_data(path, source_root=FIXTURE, resolver=resolver)
    return {(r.src_qname, r.kind, r.target_qname) for r in fd.references}


def test_alias_import_edge(resolver: TsResolver):
    edges = _edges(FIXTURE / "src" / "app.ts", resolver)
    assert ("src/app:App.run", "calls", "src/util:double") in edges


def test_workspace_package_edge(resolver: TsResolver):
    edges = _edges(FIXTURE / "src" / "app.ts", resolver)
    assert ("src/app:App.run", "calls", "packages/core/index:greet") in edges


def test_barrel_reexport_edge(resolver: TsResolver):
    edges = _edges(FIXTURE / "src" / "app.ts", resolver)
    assert ("src/app:App.run", "calls", "src/store/index:makeStore") in edges


def test_inherits_and_implements(resolver: TsResolver):
    edges = _edges(FIXTURE / "src" / "app.ts", resolver)
    assert ("src/app:App", "inherits", "src/base:Base") in edges
    assert ("src/app:App", "implements", "src/base:Runnable") in edges


def test_class_contains_members(resolver: TsResolver):
    edges = _edges(FIXTURE / "src" / "app.ts", resolver)
    assert ("src/app:App", "contains", "src/app:App.run") in edges


def test_ambient_dts_import_edge(resolver: TsResolver):
    # `import { map } from "lang-map"` binds to the ambient module symbol keyed
    # by the literal name (declared in src/types/external.d.ts).
    edges = _edges(FIXTURE / "src" / "app.ts", resolver)
    assert ("src/app:App.run", "calls", "lang-map:map") in edges


def test_unresolved_external_is_candidate_only(resolver: TsResolver):
    # An import from a package the project doesn't define still emits a
    # candidate edge; the store's replace_all_edges drops it. We assert the
    # extractor does NOT resolve it to any project symbol.
    edges = _edges(FIXTURE / "src" / "app.ts", resolver)
    targets = {t for _, _, t in edges}
    assert "nonexistent-package:unknownThing" in targets  # candidate, dropped later
    assert not any(t.startswith("src/") and "unknownThing" in t for t in targets)


def test_intra_file_edges(resolver: TsResolver):
    edges = _edges(FIXTURE / "src" / "util.ts", resolver)
    # compute() calls double() and secretHelper() within the same module.
    assert ("src/util:compute", "calls", "src/util:double") in edges
    assert ("src/util:compute", "calls", "src/util:secretHelper") in edges
