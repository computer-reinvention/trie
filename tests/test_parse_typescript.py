from __future__ import annotations

from pathlib import Path

from trie.parse.typescript import extract_symbols

FIXTURE = Path(__file__).parent / "fixtures" / "tiny_ts_repo"


def _by_qname(symbols):
    return {s.qualified_name: s for s in symbols}


def test_function_and_const_kinds():
    syms = _by_qname(extract_symbols(FIXTURE / "src" / "util.ts", source_root=FIXTURE))
    assert syms["src/util:double"].kind == "function"
    assert syms["src/util:double"].is_public is True
    # An un-exported function is private.
    assert syms["src/util:secretHelper"].kind == "function"
    assert syms["src/util:secretHelper"].is_public is False
    # Plain const -> constant; arrow const -> function.
    assert syms["src/util:PI"].kind == "constant"
    assert syms["src/util:compute"].kind == "function"


def test_jsdoc_becomes_docstring():
    syms = _by_qname(extract_symbols(FIXTURE / "src" / "util.ts", source_root=FIXTURE))
    assert "Double a number" in (syms["src/util:double"].docstring or "")


def test_class_method_property_kinds():
    syms = _by_qname(extract_symbols(FIXTURE / "src" / "base.ts", source_root=FIXTURE))
    assert syms["src/base:Base"].kind == "class"
    assert syms["src/base:Base.id"].kind == "property"
    assert syms["src/base:Base.id"].parent_class == "Base"
    assert syms["src/base:Base.describe"].kind == "method"
    assert syms["src/base:Base.describe"].parent_class == "Base"


def test_interface_type_enum_kinds():
    syms = _by_qname(extract_symbols(FIXTURE / "src" / "base.ts", source_root=FIXTURE))
    assert syms["src/base:Runnable"].kind == "interface"
    assert syms["src/base:Identifier"].kind == "type"
    assert syms["src/base:Status"].kind == "enum"


def test_enum_members_are_child_symbols():
    syms = _by_qname(extract_symbols(FIXTURE / "src" / "base.ts", source_root=FIXTURE))
    assert syms["src/base:Status.Active"].kind == "enum_member"
    assert syms["src/base:Status.Active"].parent_class == "Status"
    assert syms["src/base:Status.Inactive"].kind == "enum_member"
    assert syms["src/base:Status.Pending"].kind == "enum_member"


def test_dts_ambient_module_keyed_by_name():
    syms = _by_qname(
        extract_symbols(FIXTURE / "src" / "types" / "external.d.ts", source_root=FIXTURE)
    )
    # The ambient module is a `module` symbol keyed by its literal name.
    assert syms["lang-map:__module__"].kind == "module"
    # Its inner declarations are keyed under the module name.
    assert syms["lang-map:MapReturn"].kind == "interface"
    assert syms["lang-map:map"].kind == "function"
    # A bare `declare const` attributes to the file's own module key.
    assert "src/types/external:BUILD_ID" in syms
    assert syms["src/types/external:BUILD_ID"].kind == "constant"


def test_tsx_parses():
    src = "export const View = (): number => 1\n"
    p = FIXTURE / "src" / "_tmp_view.tsx"
    p.write_text(src)
    try:
        syms = _by_qname(extract_symbols(p, source_root=FIXTURE))
        assert syms["src/_tmp_view:View"].kind == "function"
    finally:
        p.unlink()


def test_fingerprint_stable_under_comment_change():
    base = "export function f(a: number): number { return a + 1 }\n"
    commented = "export function f(a: number): number {\n  // a comment\n  return a + 1\n}\n"
    p1 = FIXTURE / "src" / "_tmp_a.ts"
    p2 = FIXTURE / "src" / "_tmp_b.ts"
    p1.write_text(base)
    p2.write_text(commented)
    try:
        s1 = _by_qname(extract_symbols(p1, source_root=FIXTURE))["src/_tmp_a:f"]
        s2 = _by_qname(extract_symbols(p2, source_root=FIXTURE))["src/_tmp_b:f"]
        assert s1.body_normalized_hash == s2.body_normalized_hash
    finally:
        p1.unlink()
        p2.unlink()


def test_empty_source_yields_no_symbols():
    p = FIXTURE / "src" / "_tmp_empty.ts"
    p.write_text("")
    try:
        assert extract_symbols(p, source_root=FIXTURE) == []
    finally:
        p.unlink()
