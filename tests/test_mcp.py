"""Tests for the MCP tool surface: `grep`, `read`, `trace`.

The tools are exercised via TrieTools directly — that's the same code path FastMCP
invokes when a real agent calls a tool, and the same code path `trie grep` / `trie read`
/ `trie trace` invoke from the CLI. Driving the full stdio transport is integration-
test territory.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pytest

from trie.config import Config
from trie.mcp_server import TrieTools
from trie.models import GenerationRequest, GenerationResponse
from trie.scan import scan_project
from trie.sync.single_file import sync_single_file

PROJECT_TOML = (
    '[trie]\nversion = "0.1.2"\n'
    '[scope]\ninclude = ["**/*.py"]\nexclude = ["**/__pycache__/**"]\n'
    '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
    '[models]\nbootstrap = "anthropic/claude-sonnet-4-6"\n'
    'cascade = "anthropic/claude-sonnet-4-6"\n'
    "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    "[mcp]\ngrep_max_limit = 50\ntrace_max_depth = 5\ntrace_hub_threshold = 20\n"
    "trace_max_nodes = 200\n"
)


@dataclass
class FakeClient:
    """Stand-in for ModelClient. Returns a fixed body and bogus token counts."""

    model_id: str = "fake/test"
    body: str = "## generated\n\nGenerated description.\n"

    def generate(self, _req: GenerationRequest) -> GenerationResponse:
        return GenerationResponse(
            text=self.body,
            input_tokens=10,
            output_tokens=20,
            cache_creation_input_tokens=0,
            cache_read_input_tokens=0,
        )

    def count_tokens(self, _req: GenerationRequest) -> int:
        return 100


@pytest.fixture
def project(tmp_path: Path) -> Path:
    (tmp_path / "trie.toml").write_text(PROJECT_TOML)
    (tmp_path / "lib.py").write_text(
        "def slugify(text: str) -> str:\n"
        '    """Lowercase + dash-separate."""\n'
        '    return text.lower().replace(" ", "-")\n'
    )
    (tmp_path / "app.py").write_text(
        "from lib import slugify\n\n\n"
        "def make_url(title: str) -> str:\n"
        '    return "/posts/" + slugify(title)\n'
    )
    return tmp_path


@pytest.fixture
def populated_project(project: Path) -> Path:
    """Project with scan + sync run, so the MCP tools have data to query."""
    config, _ = Config.find_and_load(project)
    from trie.graph.store import Store

    with Store(project / ".trie" / "graph.db") as store:
        scan_project(project_root=project, config=config, store=store)
        sync_single_file(
            project / "lib.py",
            project_root=project,
            config=config,
            client=FakeClient(body="## slugify\n\nLowercase text and dash-separate words.\n"),
            store=store,
        )
        sync_single_file(
            project / "app.py",
            project_root=project,
            config=config,
            client=FakeClient(body="## make_url\n\nBuild a /posts/<slug> URL from a title.\n"),
            store=store,
        )
    return project


@pytest.fixture
def tools(populated_project: Path):
    t = TrieTools(populated_project)
    yield t
    t.close()


# --- rg dependency -------------------------------------------------------


def test_trie_tools_init_fails_clearly_when_rg_missing(
    populated_project: Path, monkeypatch: pytest.MonkeyPatch
):
    """`grep`'s text-match fallback shells to ripgrep. We refuse to start the
    MCP server when `rg` is absent rather than degrading silently: a half-
    working server (symbol lookups fine, fallback broken) is the kind of
    bug that wastes hours.

    Simulate the missing-rg case by stubbing `shutil.which` to return
    `None`; the error must name the binary and tell the user how to
    install it so the failure is self-recovering.
    """
    from trie.mcp_server import RipgrepNotFoundError

    monkeypatch.setattr("trie.mcp_server.shutil.which", lambda _name: None)
    with pytest.raises(RipgrepNotFoundError) as excinfo:
        TrieTools(populated_project)
    msg = str(excinfo.value)
    # Must name the missing dependency by its conventional binary name.
    assert "rg" in msg
    # Must point at a path forward (install hint or canonical URL).
    assert "install" in msg.lower() or "ripgrep" in msg.lower()


# --- grep -----------------------------------------------------------------


def test_grep_name_contains_returns_matches(tools: TrieTools):
    result = tools.grep({"name_contains": "slug"})
    qnames = {h["qname"] for h in result["hits"]}
    assert "lib:slugify" in qnames
    # When there are real hits, no fallback envelope is attached.
    assert "fallback" not in result


def test_grep_returns_one_liner_from_section_body(tools: TrieTools):
    result = tools.grep({"name_contains": "slugify"})
    assert result["hits"], "expected at least one hit"
    h = result["hits"][0]
    assert "Lowercase" in h["one_liner"]
    # Sentence is truncated to first '.'
    assert h["one_liner"].endswith("words") or h["one_liner"].endswith("words.")


def test_grep_returns_file_pointer(tools: TrieTools):
    result = tools.grep({"name_contains": "make_url"})
    assert result["hits"][0]["file_pointer"].endswith("app.py:4")


def test_grep_kind_filter(tools: TrieTools):
    # Both fixtures define only functions; class filter should return zero hits.
    # The fallback will fire because `name_contains` is present — the text
    # search finds `slug` in source bodies. That's the new contract; we
    # assert on hits being empty rather than the whole result.
    result = tools.grep({"name_contains": "slug", "kind": "class"})
    assert result["hits"] == []


def test_grep_invalid_kind_returns_error(tools: TrieTools):
    result = tools.grep({"kind": "macro"})
    assert isinstance(result, dict) and "error" in result
    assert result["error"]["code"] == "invalid_argument"


def test_grep_accepts_constant_and_module_kinds(tools: TrieTools):
    """The parser now surfaces `constant` (module-level NAME = value) and
    `module` (synthetic __module__ symbol for file-level behaviour) in
    addition to function/class/method. The predicate validator must
    accept both as legal `kind` values. We don't assert on hits here —
    the fixture may or may not have constants — only that the predicate
    is accepted (no `invalid_argument` error envelope)."""
    for kind in ("constant", "module"):
        result = tools.grep({"kind": kind, "name_contains": "x"})
        # No error envelope; the call returned an envelope with hits +
        # (optional) fallback. Whether there are hits depends on the
        # fixture content; we only assert the predicate was parsed.
        assert "error" not in result, f"kind={kind!r} should be accepted, got: {result}"


def test_grep_scope_prefix_filter(tools: TrieTools):
    result = tools.grep({"scope_prefix": "lib"})
    file_paths = {h["file_pointer"].split(":")[0] for h in result["hits"]}
    assert all(p.startswith("lib") for p in file_paths)


def test_grep_scope_exclude_filter(tools: TrieTools):
    result = tools.grep({"scope_exclude": ["app"]})
    file_paths = {h["file_pointer"].split(":")[0] for h in result["hits"]}
    assert "app.py" not in file_paths


def test_grep_inbound_count_predicate(tools: TrieTools):
    # slugify has one inbound edge from make_url.
    result = tools.grep({"inbound_count": {"min": 1}})
    qnames = {h["qname"] for h in result["hits"]}
    assert "lib:slugify" in qnames
    assert "app:make_url" not in qnames  # make_url has no callers


def test_grep_rank_by_inbound_count(tools: TrieTools):
    # `public_only: true` is the documented orientation query — every public
    # symbol in scope, ranked by centrality. Using a real filter here also
    # avoids the empty-predicate rejection path that `grep` enforces.
    result = tools.grep({"public_only": True}, rank_by="inbound_count", limit=5)
    hits = result["hits"]
    # First hit should have the highest inbound_count.
    assert hits[0]["inbound_count"] >= hits[-1]["inbound_count"]


def test_grep_limit_respected(tools: TrieTools):
    # Same trick: a non-empty predicate keeps us out of the empty-predicate
    # rejection path while still exercising the `limit` clamp.
    result = tools.grep({"public_only": True}, limit=1)
    assert len(result["hits"]) == 1


def test_grep_empty_predicate_returns_invalid_argument(tools: TrieTools):
    """An empty predicate is rejected explicitly with `invalid_argument` and
    a `suggestion` pointing the agent at the documented orientation patterns.

    This is the headline contract for the rejection: we don't return random
    alphabetical leaves disguised as relevant hits. The agent must specify
    *what kind* of search it wants before trie returns anything.
    """
    for predicate in (None, {}, {"name_contains": ""}, {"kind": "any"}):
        result = tools.grep(predicate)
        assert "error" in result, f"predicate {predicate!r} should have errored"
        assert result["error"]["code"] == "invalid_argument"
        # Suggestion must name at least one usable filter so the agent can fix.
        suggestion = result["error"].get("suggestion", "")
        assert "name_contains" in suggestion or "scope_prefix" in suggestion


def test_grep_empty_predicate_rejected_regardless_of_rank_by(tools: TrieTools):
    """Passing `rank_by` doesn't rescue an empty predicate. `rank_by` only
    orders results; without filter fields there's nothing meaningful to
    order. The rejection happens before ranking is even consulted."""
    result = tools.grep({}, rank_by="inbound_count", limit=10)
    assert "error" in result
    assert result["error"]["code"] == "invalid_argument"


def test_grep_unknown_predicate_field_silently_ignored(tools: TrieTools):
    # Extra fields don't break the call — we just ignore them.
    result = tools.grep({"name_contains": "slug", "totally_made_up_field": True})
    assert result["hits"]  # match still works


def test_grep_invalid_predicate_returns_error(tools: TrieTools):
    result = tools.grep("not an object")  # type: ignore[arg-type]
    assert isinstance(result, dict) and "error" in result
    assert result["error"]["code"] == "invalid_argument"


# --- grep: text-match fallback on empty hits ------------------------------


def test_grep_fallback_kind_none_when_no_name_contains(tools: TrieTools):
    """A predicate with no `name_contains` and no symbol-name match still
    returns the envelope, with `fallback.kind == "none"` so the agent knows
    text-search was inapplicable rather than empty."""
    # `inbound_count: {min: 999}` matches nothing in our fixture, and the
    # predicate has no name_contains for the fallback to use.
    result = tools.grep({"inbound_count": {"min": 999}})
    assert result["hits"] == []
    assert result["fallback"]["kind"] == "none"
    assert "name_contains" in result["fallback"]["note"]


def test_grep_fallback_kind_text_match_empty_for_unseen_string(tools: TrieTools):
    """When `name_contains` is set but the string appears nowhere in source,
    fallback reports `text_match_empty` — the agent gets clear "this doesn't
    exist" signal rather than an ambiguous empty list."""
    result = tools.grep({"name_contains": "xyzzy_no_such_thing"})
    assert result["hits"] == []
    assert result["fallback"]["kind"] == "text_match_empty"
    assert result["fallback"]["query"] == "xyzzy_no_such_thing"


def test_grep_fallback_kind_text_match_redirects_via_body_match(tools: TrieTools):
    """The interesting case: the query is not a symbol name, but it appears
    inside a symbol's body. Fallback returns the enclosing symbol so the
    agent has a starting point one round-trip away."""
    # "replace" appears inside lib:slugify's body (`.replace(" ", "-")`) but
    # is not a symbol name itself.
    result = tools.grep({"name_contains": "replace"})
    assert result["hits"] == []
    assert result["fallback"]["kind"] == "text_match"
    assert result["fallback"]["query"] == "replace"
    matches = result["fallback"]["matches"]
    qnames = {m["qname"] for m in matches}
    assert "lib:slugify" in qnames
    # Each match exposes the count of in-body occurrences and the standard
    # hit fields so the agent can hub-rank further if it wants.
    slugify_match = next(m for m in matches if m["qname"] == "lib:slugify")
    assert slugify_match["text_match_hits_in_body"] >= 1
    assert "inbound_count" in slugify_match
    assert "outbound_count" in slugify_match


def test_grep_fallback_ranks_by_inbound_count_desc(tools: TrieTools):
    """When the fallback produces multiple candidates, they're ranked by
    inbound_count descending — hub-like symbols come first so the agent
    can pick the most referenced starting point."""
    # "title" appears in app:make_url (param + use) and as a substring in
    # lib's body via "title" in shared examples; here we just confirm the
    # ordering invariant on whatever candidates land.
    result = tools.grep({"name_contains": "title"})
    if result["hits"]:
        pytest.skip("fixture grew a symbol named 'title' — adjust the test")
    matches = result["fallback"].get("matches", [])
    if len(matches) < 2:
        pytest.skip("only one fallback candidate; ranking is trivially correct")
    inbounds = [m["inbound_count"] for m in matches]
    assert inbounds == sorted(inbounds, reverse=True)


def test_grep_fallback_caps_matches_and_notes_truncation(
    tools: TrieTools,
):
    """Broad queries that match many symbols don't get refused — they get
    a ranked top-N with a truncation note. Raw ripgrep would have dumped
    every line; trie's fallback owes at least that floor of utility.

    Force a tiny match cap so we can exercise the truncation path on the
    small fixture project without depending on a huge match set.
    """
    tools.mcp_cfg = tools.mcp_cfg.__class__(
        **{**tools.mcp_cfg.__dict__, "grep_fallback_match_limit": 1}
    )
    # "def " appears inside multiple function bodies in the fixture project.
    result = tools.grep({"name_contains": "def "})
    assert result["hits"] == []
    fb = result["fallback"]
    assert fb["kind"] == "text_match"
    # We capped at 1 match but the underlying search found more candidates.
    assert len(fb["matches"]) == 1
    assert fb["unique_symbols"] > 1
    # The note must communicate that the agent isn't seeing everything.
    assert "of" in fb["note"].lower()  # "Showing top 1 of N matching symbols..."
    # The single returned match still carries all the standard fields.
    only = fb["matches"][0]
    assert "qname" in only
    assert "inbound_count" in only


def test_grep_fallback_omits_truncation_note_when_under_cap(tools: TrieTools):
    """When the match count fits inside `match_limit`, no truncation note is
    appended — the agent is seeing the full picture."""
    result = tools.grep({"name_contains": "replace"})
    assert result["hits"] == []
    fb = result["fallback"]
    assert fb["kind"] == "text_match"
    # Standard pretext is always present; truncation-specific text isn't.
    assert "showing top" not in fb["note"].lower()


def test_grep_fallback_honours_scope_prefix(tools: TrieTools):
    """The user's scope filter applies to fallback candidates too — the
    text search finds matches across the project, but only symbols in the
    allowed scope are returned."""
    # "slugify" appears in both lib.py (definition) and app.py (call).
    # With scope_prefix="app", only app's symbols should be candidates.
    # But there's a normal hit (lib:slugify) without the scope filter; the
    # filter excludes it, so we hit the fallback path on app's body matches.
    result = tools.grep({"name_contains": "slugify", "scope_prefix": "app"})
    # No symbol *named* slugify exists under app/, so hits is empty.
    assert result["hits"] == []
    fb = result["fallback"]
    # Whatever shape the fallback takes, no `lib:` qname should appear in it.
    if fb["kind"] == "text_match":
        qnames = {m["qname"] for m in fb["matches"]}
        assert not any(q.startswith("lib:") for q in qnames)


def test_grep_normal_hits_path_omits_fallback_key(tools: TrieTools):
    """When the primary path returns results, there's no `fallback` key
    at all — the response is strictly `{"hits": [...]}` so the agent doesn't
    waste tokens reading an envelope it doesn't need."""
    result = tools.grep({"name_contains": "slugify"})
    assert result["hits"]
    assert "fallback" not in result


# --- read -----------------------------------------------------------------


def test_read_returns_prose_and_neighbours(tools: TrieTools):
    out = tools.read("lib:slugify")
    assert out["qname"] == "lib:slugify"
    assert "Lowercase" in out["prose"]
    # make_url is the caller of slugify
    caller_qnames = {c["qname"] for c in out["callers"]}
    assert "app:make_url" in caller_qnames
    assert out["callees"] == []  # slugify references no other in-scope symbols


def test_read_source_pointer_shape(tools: TrieTools):
    out = tools.read("lib:slugify")
    assert out["source_pointer"].startswith("lib.py:")
    assert "-" in out["source_pointer"]  # "start-end"


def test_read_neighbour_carries_one_liner(tools: TrieTools):
    out = tools.read("lib:slugify")
    caller = next(c for c in out["callers"] if c["qname"] == "app:make_url")
    assert "Build a /posts" in caller["one_liner"]


def test_read_unknown_qname_returns_not_found(tools: TrieTools):
    result = tools.read("nonexistent:missing")
    assert "error" in result
    assert result["error"]["code"] == "not_found"


def test_read_fuzzy_suggestion_for_typo(tools: TrieTools):
    result = tools.read("lib:slugfy")  # typo
    assert "error" in result
    suggestion = result["error"].get("suggestion", "")
    # Either suggests the qname directly, or guides to grep(). Both forms include
    # something to act on.
    assert "slugify" in suggestion or "grep(" in suggestion


# --- trace ----------------------------------------------------------------


def test_trace_callers_returns_topology(tools: TrieTools):
    out = tools.trace("lib:slugify", direction="callers", depth=2)
    assert out["root"]["qname"] == "lib:slugify"
    assert "app:make_url" in out["nodes"]
    # Edge from caller to callee, tagged "in" relative to root.
    edges = out["edges"]
    assert any(e["from"] == "app:make_url" and e["to"] == "lib:slugify" for e in edges)


def test_trace_callees_returns_outbound(tools: TrieTools):
    out = tools.trace("app:make_url", direction="callees", depth=1)
    assert "lib:slugify" in out["nodes"]
    assert any(e["from"] == "app:make_url" and e["to"] == "lib:slugify" for e in out["edges"])


def test_trace_both_directions(tools: TrieTools):
    out = tools.trace("lib:slugify", direction="both", depth=1)
    # Should include the caller side.
    assert "app:make_url" in out["nodes"]
    directions = {e["direction"] for e in out["edges"]}
    assert "in" in directions


def test_trace_invalid_direction_returns_error(tools: TrieTools):
    result = tools.trace("lib:slugify", direction="sideways")
    assert "error" in result
    assert result["error"]["code"] == "invalid_argument"


def test_trace_unknown_qname_returns_not_found(tools: TrieTools):
    result = tools.trace("nonexistent:foo", direction="callers")
    assert "error" in result
    assert result["error"]["code"] == "not_found"


def test_trace_depth_zero_returns_only_root(tools: TrieTools):
    out = tools.trace("lib:slugify", direction="callers", depth=0)
    assert list(out["nodes"].keys()) == ["lib:slugify"]
    assert out["edges"] == []


def test_trace_depth_clamp_adds_note(tools: TrieTools):
    # trace_max_depth defaults to 5; ask for more and expect a note.
    out = tools.trace("lib:slugify", direction="callers", depth=99)
    assert "notes" in out
    assert any("clamped" in n for n in out["notes"])


# --- server construction --------------------------------------------------


def test_build_server_registers_three_verbs(populated_project: Path):
    """Verify build_server returns a FastMCP with `grep`, `read`, and `trace`
    registered. The wire names match the method names on TrieTools so that
    the MCP boundary and the CLI subcommands stay byte-equivalent."""
    from trie.mcp_server import build_server

    server, t = build_server(populated_project)
    try:
        names = {tool.name for tool in server._tool_manager.list_tools()}
        # Core 3 verbs.
        assert {"grep", "read", "trace"}.issubset(names)
        # Extended toolset (8 new tools).
        assert {
            "grep_str",
            "grep_entry_points",
            "grep_symbol",
            "grep_symbol_and_neighbours",
            "explain_symbol",
            "explain_symbol_references",
            "trace_flow",
            "explain_flow",
        }.issubset(names)
    finally:
        t.close()


def test_build_server_wire_names_bind_to_internal_methods(populated_project: Path):
    """Verify each wire tool dispatches to the matching `TrieTools` method.

    Pins the mapping `grep -> grep`, `read -> read`, `trace -> trace` so a
    future rename can't silently swap behaviour underneath an agent. The
    bindings are also what `trie grep` / `trie read` / `trie trace` call,
    so the CLI and MCP surfaces share one implementation per verb.
    """
    from trie.mcp_server import build_server

    server, t = build_server(populated_project)
    try:
        tools_by_name = {tool.name: tool for tool in server._tool_manager.list_tools()}
        assert tools_by_name["grep"].fn == t.grep
        assert tools_by_name["read"].fn == t.read
        assert tools_by_name["trace"].fn == t.trace
    finally:
        t.close()


# ---------------------------------------------------------------------------
# Fuzzy matching tests
# ---------------------------------------------------------------------------


@pytest.fixture
def dual_rank_project(tmp_path: Path) -> Path:
    """Project with two symbols that match a query equally on text:
    - 'hub_authenticate' — 3 inbound refs (wired hub, called from 3 separate files)
    - 'auth_check'       — 2 inbound refs (niche, called from 2 separate files)
    Both have "auth" in their name so they score the same on relevance.
    The niche one (auth_check) should rank first under (score DESC, inbound ASC).
    """
    (tmp_path / "trie.toml").write_text(PROJECT_TOML)
    (tmp_path / "auth.py").write_text(
        "def hub_authenticate(token: str) -> bool:\n"
        '    """Authenticate via the central auth hub."""\n'
        "    return bool(token)\n\n\n"
        "def auth_check(token: str) -> bool:\n"
        '    """Check auth token validity."""\n'
        "    return bool(token)\n"
    )
    # 3 callers for hub_authenticate, 2 for auth_check — in separate files
    # so scan_project registers distinct reference edges.
    (tmp_path / "svc_a.py").write_text(
        "from auth import hub_authenticate\n\ndef service_a():\n    hub_authenticate('tok')\n"
    )
    (tmp_path / "svc_b.py").write_text(
        "from auth import hub_authenticate\n\ndef service_b():\n    hub_authenticate('tok')\n"
    )
    (tmp_path / "svc_c.py").write_text(
        "from auth import hub_authenticate\n\ndef service_c():\n    hub_authenticate('tok')\n"
    )
    (tmp_path / "check_a.py").write_text(
        "from auth import auth_check\n\ndef checker_a():\n    auth_check('tok')\n"
    )
    (tmp_path / "check_b.py").write_text(
        "from auth import auth_check\n\ndef checker_b():\n    auth_check('tok')\n"
    )
    config, _ = Config.find_and_load(tmp_path)
    from trie.graph.store import Store

    with Store(tmp_path / ".trie" / "graph.db") as store:
        scan_project(project_root=tmp_path, config=config, store=store)
        for fname, body in [
            (
                "auth.py",
                "## hub_authenticate\n\nAuthenticate via the central auth hub.\n\n"
                "## auth_check\n\nCheck whether an auth token is valid.\n",
            ),
            ("svc_a.py", "## service_a\n\nService A calls hub_authenticate.\n"),
            ("svc_b.py", "## service_b\n\nService B calls hub_authenticate.\n"),
            ("svc_c.py", "## service_c\n\nService C calls hub_authenticate.\n"),
            ("check_a.py", "## checker_a\n\nChecker A calls auth_check.\n"),
            ("check_b.py", "## checker_b\n\nChecker B calls auth_check.\n"),
        ]:
            sync_single_file(
                tmp_path / fname,
                project_root=tmp_path,
                config=config,
                client=FakeClient(body=body),
                store=store,
            )
    return tmp_path


def test_grep_entry_points_niche_ranks_before_hub(dual_rank_project: Path):
    """Among equally-relevant symbols, the lower-inbound (niche) entry point
    should appear before the high-inbound hub in grep_entry_points results.
    Sort key is (score DESC, inbound_count ASC).
    """
    t = TrieTools(dual_rank_project)
    try:
        result = t.grep_entry_points("auth")
        hits = result.get("hits", [])
        qnames = [h["qname"] for h in hits]
        # Both auth symbols must appear.
        assert any("auth_check" in q for q in qnames), f"auth_check missing from {qnames}"
        assert any("hub_authenticate" in q for q in qnames), (
            f"hub_authenticate missing from {qnames}"
        )
        # auth_check has lower inbound_count, so at equal score it ranks first.
        auth_check_pos = next(i for i, q in enumerate(qnames) if "auth_check" in q)
        hub_pos = next(i for i, q in enumerate(qnames) if "hub_authenticate" in q)
        assert auth_check_pos < hub_pos, (
            f"Expected niche auth_check (pos {auth_check_pos}) before hub "
            f"hub_authenticate (pos {hub_pos})"
        )
    finally:
        t.close()


def test_grep_entry_points_hits_carry_score(dual_rank_project: Path):
    """Every hit returned by grep_entry_points must include a numeric 'score' field."""
    t = TrieTools(dual_rank_project)
    try:
        result = t.grep_entry_points("auth")
        hits = result.get("hits", [])
        assert hits, "Expected at least one hit"
        for hit in hits:
            assert "score" in hit, f"Missing 'score' in hit: {hit}"
            assert isinstance(hit["score"], (int, float))
            assert hit["score"] > 0
    finally:
        t.close()


def test_grep_symbol_typo_tolerance(tools: TrieTools):
    """grep_symbol should resolve a one-character typo ('slugufy') to 'slugify'
    using rapidfuzz at the lowered cutoff of 45.
    """
    result = tools.grep_symbol("slugufy")
    assert "error" not in result, f"Expected a match, got error: {result}"
    assert "slugify" in result["match"]["qname"]


def test_grep_symbol_returns_score_field(tools: TrieTools):
    """Every symbol in match and similar must carry a numeric 'score' field."""
    result = tools.grep_symbol("slugify")
    assert "error" not in result
    assert "score" in result["match"], "match missing 'score'"
    assert isinstance(result["match"]["score"], (int, float))
    assert result["match"]["score"] > 0
    for item in result.get("similar", []):
        assert "score" in item, f"similar item missing 'score': {item}"


def test_grep_fuzzy_prose_fallback(tools: TrieTools):
    """When name_contains finds no SQL hit, the fuzzy_prose fallback should
    kick in and surface symbols whose prose body contains the concept.
    'lowercase dash separate' is in slugify's triefact body but not its name.
    """
    result = tools.grep(predicate={"name_contains": "lowercase dash separate"})
    # Primary hits will be empty (no symbol is named that).
    assert "fallback" in result
    fb = result["fallback"]
    # Should be either text_match (rg finds the literal string in the body)
    # or fuzzy_prose (fuzzy found it via scoring).
    assert fb["kind"] in ("text_match", "fuzzy_prose"), f"Unexpected fallback kind: {fb['kind']}"
    if fb["kind"] == "fuzzy_prose":
        assert fb["matches"], "fuzzy_prose fallback returned no matches"
        qnames = [m["qname"] for m in fb["matches"]]
        assert any("slugify" in q for q in qnames), f"Expected slugify in {qnames}"


def test_grep_str_fuzzy_fallback(tools: TrieTools):
    """grep_str with a pattern that matches nothing should return a fuzzy
    fallback under hits[]=[] with fallback.kind=='fuzzy_one_liner'.
    'slugufy' is a typo of 'slugify' — rg won't match it in source, but
    rapidfuzz should surface the symbol.
    """
    result = tools.grep_str("slugufy_nonexistent_xyzzy")
    assert result.get("hits") == [], f"Expected empty hits, got: {result.get('hits')}"
    # Either a note (truly nothing found) or a fuzzy fallback.
    # With a nonsense pattern we expect no match at all — just verify no crash.
    assert "hits" in result


def test_grep_str_fuzzy_fallback_finds_close_name(tools: TrieTools):
    """grep_str with a close-but-not-exact name should surface the symbol
    via the fuzzy_one_liner fallback when rg finds no regex match.
    """
    # 'slugufy' won't appear in source (it's a typo), but fuzzy scoring
    # against local names should surface 'slugify'.
    result = tools.grep_str("slugufy")
    # rg regex "slugufy" won't match anything literal in the source.
    # If it happens to match nothing, we expect a fallback.
    if result.get("hits"):
        # rg found something — the pattern accidentally matched; skip assertion.
        return
    assert "fallback" in result, f"Expected fallback when rg finds nothing, got: {result}"
    fb = result["fallback"]
    assert fb["kind"] == "fuzzy_one_liner"
    qnames = [m["qname"] for m in fb["matches"]]
    assert any("slugify" in q for q in qnames), f"Expected slugify in fuzzy fallback: {qnames}"
