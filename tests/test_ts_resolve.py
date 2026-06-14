from __future__ import annotations

from pathlib import Path

import pytest

from trie.parse.ts_resolve import TsResolver

FIXTURE = Path(__file__).parent / "fixtures" / "tiny_ts_repo"


@pytest.fixture
def resolver() -> TsResolver:
    return TsResolver.build(FIXTURE)


def test_relative_import(resolver: TsResolver):
    from_file = FIXTURE / "src" / "store" / "index.ts"
    assert resolver.resolve("./make", from_file) == "src/store/make"


def test_tsconfig_alias(resolver: TsResolver):
    from_file = FIXTURE / "src" / "app.ts"
    assert resolver.resolve("@/util", from_file) == "src/util"
    assert resolver.resolve("@/base", from_file) == "src/base"


def test_alias_to_barrel_index(resolver: TsResolver):
    from_file = FIXTURE / "src" / "app.ts"
    # @/store resolves to the directory barrel src/store/index.ts.
    assert resolver.resolve("@/store", from_file) == "src/store/index"


def test_workspace_package(resolver: TsResolver):
    from_file = FIXTURE / "src" / "app.ts"
    assert resolver.resolve("@oc/core", from_file) == "packages/core/index"


def test_ambient_dts_resolution_is_left_to_store(resolver: TsResolver):
    # The resolver doesn't know ambient module names (they're not files); a bare
    # "lang-map" specifier resolves to None here. The reference extractor binds
    # the specifier text directly so the store can match the ambient symbol.
    from_file = FIXTURE / "src" / "app.ts"
    assert resolver.resolve("lang-map", from_file) is None


def test_external_unresolved(resolver: TsResolver):
    from_file = FIXTURE / "src" / "app.ts"
    assert resolver.resolve("nonexistent-package", from_file) is None
    assert resolver.resolve("react", from_file) is None


def test_resolution_is_memoized(resolver: TsResolver):
    from_file = FIXTURE / "src" / "app.ts"
    first = resolver.resolve("@/util", from_file)
    assert ("@/util", str(from_file)) in resolver._cache
    assert resolver.resolve("@/util", from_file) == first
