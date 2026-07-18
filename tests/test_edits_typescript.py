"""TypeScript parity for the edit/patch pipeline.

Covers the three spots the multi-language PRD §7 planned but the first pass
missed, all surfaced by a real TS patch run:

1. language-aware generation prompt (edit_system_prompt + code fence),
2. language-aware syntax gate (validate_syntax: Python=compile, TS=tsc),
3. language-aware create-symbol file resolution + true new-file creation.

The TS `tsc` gate degrades to "accept" when no `tsc` is installed, so the
gate-decision tests stub `subprocess.run` to stay hermetic.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from trie.parse import registry
from trie.parse.python import PythonBackend
from trie.parse.typescript import TypeScriptBackend

FIXTURE = Path(__file__).parent / "fixtures" / "tiny_ts_repo"


# --- backend metadata: fences + edit prompts are language-correct -----------


def test_python_fence_and_edit_prompt():
    be = PythonBackend()
    assert be.code_fence() == "python"
    assert "Python" in be.edit_system_prompt()


def test_typescript_fence_and_edit_prompt():
    be = TypeScriptBackend()
    assert be.code_fence() == "typescript"
    prompt = be.edit_system_prompt()
    assert "TypeScript" in prompt
    assert "tsc" in prompt  # tells the model to emit tsc-clean code
    # symbol-only body: model must NOT put imports in the body
    assert "ONLY" in prompt and "import" in prompt.lower()


def test_registry_routes_fence_by_extension():
    assert registry.get_backend_for_file(Path("a/b.ts")).code_fence() == "typescript"
    assert registry.get_backend_for_file(Path("a/b.tsx")).code_fence() == "typescript"
    assert registry.get_backend_for_file(Path("a/b.py")).code_fence() == "python"


# --- edit backend wires the right prompt/fence per file ---------------------


def test_edit_backend_uses_ts_prompt_for_ts_file():
    from trie.edits.backends.llm import _fence_for, _system_prompt_for

    assert _fence_for("src/app.ts") == "typescript"
    assert "TypeScript" in _system_prompt_for("src/app.ts")
    # Python fallback when no path.
    assert _fence_for(None) == "python"
    assert "Python" in _system_prompt_for(None)


def test_infer_helpers_use_ts_prompt_for_ts_file():
    from trie.edits.infer import _fence_for, _system_prompt_for

    assert _fence_for("src/app.tsx") == "typescript"
    assert "TypeScript" in _system_prompt_for("src/app.tsx")


def test_build_user_prompt_fences_ts_source():
    from trie.edits.backends.base import EditRequest
    from trie.edits.backends.llm import build_user_prompt

    req = EditRequest(
        qname="src/app:App.run",
        op="modify",
        old_source="run() { return 1 }",
        old_prose="",
        merged_notes=["return 2"],
        merged_reasons=["x"],
        session_note="",
        callees=[],
        callers=[],
        file_path="src/app.ts",
    )
    prompt = build_user_prompt(req)
    assert "```typescript" in prompt
    assert "```python" not in prompt


# --- Python syntax gate unchanged -------------------------------------------


def test_python_validate_syntax():
    be = PythonBackend()
    assert be.validate_syntax("def f():\n    return 1\n", file_path=Path("m.py"))
    assert not be.validate_syntax("def f(:\n", file_path=Path("m.py"))


def test_compile_check_routes_python_by_path():
    from trie.edits.apply import _compile_check

    assert _compile_check("x = 1\n", "m.py")
    assert not _compile_check("def (((:\n", "m.py")
    # No path → legacy Python behaviour.
    assert _compile_check("x = 1\n")


# --- TS syntax gate: TS1xxx rejects, TS2xxx accepts (hermetic via stub) ------


class _FakeProc:
    def __init__(self, out: str) -> None:
        self.stdout = out
        self.stderr = ""
        self.returncode = 2 if out else 0


@pytest.fixture
def ts_backend_with_fake_tsc(monkeypatch):
    be = TypeScriptBackend()
    # Pretend tsc exists so validate_syntax runs its decision logic.
    monkeypatch.setattr("trie.parse.typescript._find_tsc", lambda _p: ["tsc"])
    return be, monkeypatch


def test_ts_gate_rejects_syntax_error(ts_backend_with_fake_tsc):
    be, monkeypatch = ts_backend_with_fake_tsc
    out = "candidate.ts(1,52): error TS1109: Expression expected.\n"
    monkeypatch.setattr("subprocess.run", lambda *a, **k: _FakeProc(out))
    assert not be.validate_syntax("export const x =", file_path=Path("m.ts"))


def test_ts_gate_accepts_when_only_type_errors(ts_backend_with_fake_tsc):
    be, monkeypatch = ts_backend_with_fake_tsc
    # TS2307 = cannot find module (resolution), expected under --noResolve.
    out = "candidate.ts(1,21): error TS2307: Cannot find module './other'.\n"
    monkeypatch.setattr("subprocess.run", lambda *a, **k: _FakeProc(out))
    assert be.validate_syntax(
        "import { foo } from './other'\nexport const x = 1\n", file_path=Path("m.ts")
    )


def test_ts_gate_accepts_clean(ts_backend_with_fake_tsc):
    be, monkeypatch = ts_backend_with_fake_tsc
    monkeypatch.setattr("subprocess.run", lambda *a, **k: _FakeProc(""))
    assert be.validate_syntax("export const x = 1\n", file_path=Path("m.ts"))


def test_ts_gate_degrades_to_accept_without_tsc(monkeypatch):
    be = TypeScriptBackend()
    monkeypatch.setattr("trie.parse.typescript._find_tsc", lambda _p: None)
    # Even syntactically broken TS is accepted when no tsc is available — the
    # overlay diagnostics pass remains the real gate; we never hard-block.
    assert be.validate_syntax("export const x =", file_path=Path("m.ts"))


# --- create-symbol resolves the right suffix (no .py for a .ts module) -------


def test_resolve_create_target_existing_ts_file():
    # src/app.ts exists in the fixture; a new symbol there must resolve to .ts.
    assert registry.resolve_create_target(FIXTURE, "src/app:newHelper") == "src/app.ts"


def test_resolve_create_target_existing_py_file(tmp_path):
    (tmp_path / "pkg").mkdir()
    (tmp_path / "pkg" / "mod.py").write_text("x = 1\n")
    assert registry.resolve_create_target(tmp_path, "pkg/mod:thing") == "pkg/mod.py"


def test_resolve_create_target_new_file_infers_from_sibling(tmp_path):
    # A brand-new module in a dir that already holds .ts files → infer .ts.
    d = tmp_path / "src" / "components"
    d.mkdir(parents=True)
    (d / "Existing.tsx").write_text("export const A = 1\n")
    target = registry.resolve_create_target(tmp_path, "src/components/NewSheet:NewSheet")
    assert target.endswith(".ts") or target.endswith(".tsx")
    assert target.startswith("src/components/NewSheet")


# --- merge_notes resilience (apply must not crash on a bad LLM response) -----


class _RaisingClient:
    """Stand-in TrieClient whose .run always fails, to prove merge degrades."""

    def run(self, *a, **k):
        raise RuntimeError("simulated LLM/schema failure")


def test_merge_notes_single_patch_skips_llm():
    from trie.edits.infer import merge_notes

    # One patch has nothing to merge → return verbatim WITHOUT calling the LLM
    # (a single-patch apply previously crashed on an empty MergeNotesOutput).
    notes, reasons = merge_notes(_RaisingClient(), [{"note": "do X", "reason": "because"}])
    assert notes == ["do X"]
    assert reasons == ["because"]


def test_merge_notes_degrades_on_llm_failure():
    from trie.edits.infer import merge_notes

    # Multiple patches + a failing/garbage LLM response → fall back to raw notes
    # rather than aborting the whole apply.
    patches = [
        {"note": "do X", "reason": "r1"},
        {"note": "do Y", "reason": "r2"},
    ]
    notes, reasons = merge_notes(_RaisingClient(), patches)
    assert notes == ["do X", "do Y"]
    assert reasons == ["r1", "r2"]


# --- class-method placement: new method lands INSIDE the parent body --------


class _FakeDetail:
    def __init__(self, start_line: int, end_line: int) -> None:
        self.start_line = start_line
        self.end_line = end_line


def test_insert_into_parent_brace_language():
    from trie.edits.pipeline import _insert_into_parent

    ts = "export class Engine {\n  stop(): void {}\n}\n"
    parent = _FakeDetail(1, 3)  # class spans lines 1..3
    out = _insert_into_parent(ts, "newMethod(): void {}\n", parent)
    assert out is not None
    # New method is indented inside the class, before the closing brace.
    lines = out.splitlines()
    close_idx = next(i for i, ln in enumerate(lines) if ln.strip() == "}")
    method_idx = next(i for i, ln in enumerate(lines) if "newMethod" in ln)
    assert method_idx < close_idx
    assert lines[method_idx].startswith("    ")  # member-level indent


def test_insert_into_parent_indentation_language():
    from trie.edits.pipeline import _insert_into_parent

    py = "class Engine:\n    def stop(self):\n        pass\n"
    parent = _FakeDetail(1, 3)
    out = _insert_into_parent(py, "def started(self):\n    return True\n", parent)
    assert out is not None
    assert "    def started" in out  # re-indented to member level


def test_place_new_symbol_routes_method_into_class():
    from trie.edits.pipeline import _place_new_symbol

    class _Store:
        def get_symbol_detail(self, qn):
            if qn == "m/engine:Engine":
                return _FakeDetail(1, 3)
            return None

    ts = "export class Engine {\n  stop(): void {}\n}\n"
    out = _place_new_symbol(ts, "fade(): void {}\n", None, _Store(), qname="m/engine:Engine.fade")
    lines = out.splitlines()
    close_idx = next(i for i, ln in enumerate(lines) if ln.strip() == "}")
    assert any("fade" in ln for ln in lines[:close_idx])  # inside the class


# --- large-symbol generation: schema is fine; truncation was the real bug -----


def test_symboledit_validates_large_tsx_source():
    """Pydantic is NOT the bottleneck. A large TSX component (the kind that
    aborted apply with 'Exceeded maximum output retries') validates cleanly
    through SymbolEdit, both as an object and via the JSON path pydantic-ai
    uses for structured output. The real fix is a bigger output-token budget
    (so the model's tool-call JSON isn't truncated mid-string).
    """
    import json

    from trie.models import SymbolEdit

    # ~24KB of TSX with the characters that stress JSON/structured parsing:
    # JSX, template literals/backticks, regex, escaped quotes, unicode, newlines.
    body = "\n".join(
        f"  const re{i} = /\\d+/g; const s{i} = `row {i}: ${{x}}`; "
        f'const q{i} = "say \\"hi\\" — ünïcode";'
        for i in range(400)
    )
    big = (
        "import React from 'react';\n"
        "export function BrowseScreen() {\n"
        f"{body}\n"
        "  return <View><Text>{`\\n${q0}\\t`}</Text></View>;\n"
        "}\n"
    )
    assert len(big) > 20000  # genuinely large

    se = SymbolEdit(source=big, prose="big screen")
    assert se.source == big

    payload = json.dumps({"source": big, "prose": "x"})
    se2 = SymbolEdit.model_validate_json(payload)
    assert se2.source == big


def test_truncated_structured_output_fails_validation():
    """Confirms the actual failure mechanism: a tool-call JSON cut off at the
    token cap is invalid and fails to parse — which is what surfaced as
    'Exceeded maximum output retries' with the old 4096-token cap.
    """
    import json

    from pydantic import ValidationError

    from trie.models import SymbolEdit

    big = "const a = 1;\n" * 1000
    full = json.dumps({"source": big, "prose": "x"})
    truncated = full[: len(full) // 2]  # cut mid-string, as a token cap would
    with pytest.raises(ValidationError):
        SymbolEdit.model_validate_json(truncated)


def test_edit_backend_uses_larger_token_budget_and_retries():
    """The fix: the LLM edit backend is built with the raised output-token cap
    and >1 structured-output retries, so a large symbol's source fits and a
    transient bad parse is re-asked instead of aborting the apply.
    """
    from trie.config import Config
    from trie.edits.backends import make_backend

    class _FakeClient:
        pass

    cfg = Config()
    assert cfg.edits.max_output_tokens >= 8192
    assert cfg.edits.output_retries >= 2
    be = make_backend(cfg, client=_FakeClient())
    assert be._max_tokens == cfg.edits.max_output_tokens
    assert be._output_retries == cfg.edits.output_retries
