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


# --- performance regression guards ------------------------------------------
#
# Scan on a React Native project once took 43s because (a) config-file
# discovery rglob'd through all of node_modules and (b) a fresh resolver was
# built for every parsed file. These tests pin the behavioural fixes; timing
# assertions would flake, so we assert traversal and construction counts.


def test_config_discovery_never_descends_into_vendor_dirs(tmp_path):
    from trie.parse.ts_resolve import _iter_config_files

    (tmp_path / "tsconfig.json").write_text("{}")
    nested = tmp_path / "packages" / "app"
    nested.mkdir(parents=True)
    (nested / "package.json").write_text('{"name": "app"}')

    # Vendor + hidden trees that must never be traversed, let alone matched.
    for bad in ("node_modules/dep", ".git/objects", "build/out", "dist/js"):
        d = tmp_path / bad
        d.mkdir(parents=True)
        (d / "package.json").write_text('{"name": "vendored"}')
        (d / "tsconfig.json").write_text("{}")

    tsconfigs = _iter_config_files(tmp_path, "tsconfig*.json")
    pkgs = _iter_config_files(tmp_path, "package.json")

    assert tsconfigs == [tmp_path / "tsconfig.json"]
    assert pkgs == [nested / "package.json"]


def test_extract_file_data_builds_one_resolver_per_source_root(tmp_path, mocker):
    import trie.parse.typescript_refs as tsr
    from trie.parse.ts_resolve import TsResolver

    for name in ("a", "b", "c"):
        (tmp_path / f"{name}.ts").write_text(f"export const {name} = 1;\n")

    tsr._RESOLVER_CACHE.clear()
    spy = mocker.spy(TsResolver, "build")
    for name in ("a", "b", "c"):
        tsr.extract_file_data(tmp_path / f"{name}.ts", source_root=tmp_path)

    assert spy.call_count == 1, (
        f"TsResolver.build ran {spy.call_count}x for one source root — the "
        "per-scan sharing contract regressed (43s scan bug)"
    )
