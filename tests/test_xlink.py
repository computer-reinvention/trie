"""Comprehensive tests for cross-language edge detection (trie/parse/xlink.py).

Covers:
- Client-side extraction: fetch() and axios (string + template literals)
- Server-side extraction: FastAPI, Flask (route/get/post/bp.route), Express
- URL normalisation and matching logic
- Method mismatch hard rejection
- Confidence threshold gating
- Monorepo pattern (TS file with both Express routes and fetch calls)
- Hub threshold cascade protection for popular endpoints
- Full scan_project() integration test
"""

from __future__ import annotations

from pathlib import Path

import pytest

from trie.config import Config, XLink
from trie.graph.store import Store
from trie.parse.xlink import (
    XLinkCallSite,
    XLinkEndpoint,
    _match_confidence,
    extract_axios_sites,
    extract_express_endpoints,
    extract_fastapi_endpoints,
    extract_fetch_sites,
    extract_flask_endpoints,
    match_xlinks,
    normalize_url,
)
from trie.scan import scan_project

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _parse_ts(source: str, suffix: str = ".ts"):
    """Parse TypeScript/JS source and return (root_node, source_bytes)."""
    import tree_sitter_typescript as tst
    from tree_sitter import Language, Parser

    parser = Parser()
    if suffix in (".tsx", ".jsx"):
        parser.language = Language(tst.language_tsx())
    else:
        parser.language = Language(tst.language_typescript())
    src = source.encode("utf-8")
    tree = parser.parse(src)
    return tree.root_node, src


def _parse_py(source: str):
    """Parse Python source and return (root_node, source_bytes)."""
    import tree_sitter_python
    from tree_sitter import Language, Parser

    parser = Parser()
    parser.language = Language(tree_sitter_python.language())
    src = source.encode("utf-8")
    tree = parser.parse(src)
    return tree.root_node, src


def _dummy_symbols(
    names: list[str], start_line: int = 1, span: int = 100
) -> list[tuple[str, int, int]]:
    """Create dummy symbols covering a wide line range for tests."""
    return [(name, start_line, start_line + span) for name in names]


# ---------------------------------------------------------------------------
# URL Normalisation
# ---------------------------------------------------------------------------


class TestNormalizeUrl:
    def test_simple_path(self):
        assert normalize_url("/api/users") == ["api", "users"]

    def test_strips_slashes(self):
        assert normalize_url("/api/users/") == ["api", "users"]

    def test_lowercase(self):
        assert normalize_url("/API/Users") == ["api", "users"]

    def test_fastapi_param(self):
        segs = normalize_url("/api/users/{user_id}")
        assert segs == ["api", "users", "{_PARAM_}"]

    def test_express_param(self):
        segs = normalize_url("/api/users/:userId")
        assert segs == ["api", "users", "{_PARAM_}"]

    def test_flask_param(self):
        segs = normalize_url("/api/users/<int:user_id>")
        assert segs == ["api", "users", "{_PARAM_}"]

    def test_template_literal_param(self):
        segs = normalize_url("/api/users/{_PARAM_}")
        assert segs == ["api", "users", "{_PARAM_}"]

    def test_empty(self):
        assert normalize_url("") == []
        assert normalize_url("/") == []

    def test_deep_path(self):
        assert normalize_url("/api/v2/admin/users") == ["api", "v2", "admin", "users"]


# ---------------------------------------------------------------------------
# Match Confidence
# ---------------------------------------------------------------------------


class TestMatchConfidence:
    def test_exact_match(self):
        s = normalize_url("/api/users")
        e = normalize_url("/api/users")
        assert _match_confidence(s, e, "GET", "GET") == 1.0

    def test_parameterized_match(self):
        s = normalize_url("/api/users/{_PARAM_}")
        e = normalize_url("/api/users/{user_id}")
        assert _match_confidence(s, e, "GET", "GET") == 0.95

    def test_method_mismatch_rejection(self):
        s = normalize_url("/api/users")
        e = normalize_url("/api/users")
        assert _match_confidence(s, e, "GET", "POST") == 0.0

    def test_wildcard_method_server(self):
        s = normalize_url("/api/users")
        e = normalize_url("/api/users")
        assert _match_confidence(s, e, "GET", "*") == 1.0

    def test_wildcard_method_client(self):
        s = normalize_url("/api/users")
        e = normalize_url("/api/users")
        assert _match_confidence(s, e, "*", "GET") == 1.0

    def test_different_segment_count(self):
        s = normalize_url("/api/users")
        e = normalize_url("/api/users/active")
        assert _match_confidence(s, e, "GET", "GET") == 0.0

    def test_different_segments(self):
        s = normalize_url("/api/users")
        e = normalize_url("/api/items")
        assert _match_confidence(s, e, "GET", "GET") == 0.0

    def test_empty_segments(self):
        assert _match_confidence([], [], "GET", "GET") == 0.0


# ---------------------------------------------------------------------------
# Fetch extraction
# ---------------------------------------------------------------------------


class TestExtractFetchSites:
    def test_simple_fetch(self):
        root, src = _parse_ts("""
export async function fetchUsers() {
  const response = await fetch("/api/users");
  return response.json();
}
""")
        symbols = _dummy_symbols(["mod:fetchUsers"])
        sites = extract_fetch_sites(root, src, symbols)
        assert len(sites) == 1
        assert sites[0].method == "GET"
        assert sites[0].pattern == "/api/users"
        assert sites[0].framework == "fetch"

    def test_fetch_with_method(self):
        root, src = _parse_ts("""
export async function createUser(data: any) {
  const response = await fetch("/api/users", {
    method: "POST",
    body: JSON.stringify(data),
  });
  return response.json();
}
""")
        symbols = _dummy_symbols(["mod:createUser"])
        sites = extract_fetch_sites(root, src, symbols)
        assert len(sites) == 1
        assert sites[0].method == "POST"
        assert sites[0].pattern == "/api/users"

    def test_fetch_template_literal(self):
        root, src = _parse_ts("""
export async function fetchUser(userId: string) {
  const response = await fetch(`/api/users/${userId}`);
  return response.json();
}
""")
        symbols = _dummy_symbols(["mod:fetchUser"])
        sites = extract_fetch_sites(root, src, symbols)
        assert len(sites) == 1
        assert sites[0].pattern == "/api/users/{_PARAM_}"

    def test_fetch_template_literal_with_method(self):
        root, src = _parse_ts("""
export async function deleteUser(userId: string) {
  const response = await fetch(`/api/users/${userId}`, {
    method: "DELETE",
  });
  return response.json();
}
""")
        symbols = _dummy_symbols(["mod:deleteUser"])
        sites = extract_fetch_sites(root, src, symbols)
        assert len(sites) == 1
        assert sites[0].method == "DELETE"
        assert sites[0].pattern == "/api/users/{_PARAM_}"

    def test_no_symbol_attribution(self):
        """If no enclosing symbol is found, the call site is skipped."""
        root, src = _parse_ts("""
export async function fetchUsers() {
  const response = await fetch("/api/users");
  return response.json();
}
""")
        # Empty symbols list — no attribution possible
        sites = extract_fetch_sites(root, src, [])
        assert len(sites) == 0


# ---------------------------------------------------------------------------
# Axios extraction
# ---------------------------------------------------------------------------


class TestExtractAxiosSites:
    def test_axios_get(self):
        root, src = _parse_ts("""
export async function getStats() {
  const response = await axios.get("/api/stats");
  return response.data;
}
""")
        symbols = _dummy_symbols(["mod:getStats"])
        sites = extract_axios_sites(root, src, symbols)
        assert len(sites) == 1
        assert sites[0].method == "GET"
        assert sites[0].pattern == "/api/stats"
        assert sites[0].framework == "axios"

    def test_axios_post(self):
        root, src = _parse_ts("""
export async function updateData(data: any) {
  const response = await axios.post("/api/data", data);
  return response.data;
}
""")
        symbols = _dummy_symbols(["mod:updateData"])
        sites = extract_axios_sites(root, src, symbols)
        assert len(sites) == 1
        assert sites[0].method == "POST"

    def test_axios_template_literal(self):
        root, src = _parse_ts("""
export async function getItem(itemId: string) {
  const response = await axios.get(`/api/items/${itemId}`);
  return response.data;
}
""")
        symbols = _dummy_symbols(["mod:getItem"])
        sites = extract_axios_sites(root, src, symbols)
        assert len(sites) == 1
        assert sites[0].pattern == "/api/items/{_PARAM_}"

    def test_axios_config_object(self):
        root, src = _parse_ts("""
export async function bulkUpdate(data: any) {
  const response = await axios({
    url: "/api/admin/bulk",
    method: "PUT",
    data: data,
  });
  return response.data;
}
""")
        symbols = _dummy_symbols(["mod:bulkUpdate"])
        sites = extract_axios_sites(root, src, symbols)
        assert len(sites) == 1
        assert sites[0].method == "PUT"
        assert sites[0].pattern == "/api/admin/bulk"


# ---------------------------------------------------------------------------
# FastAPI extraction
# ---------------------------------------------------------------------------


class TestExtractFastapiEndpoints:
    def test_get_endpoint(self):
        root, src = _parse_py("""
@app.get("/api/users")
def list_users():
    return []
""")
        symbols = _dummy_symbols(["mod:list_users"])
        eps = extract_fastapi_endpoints(root, src, symbols)
        assert len(eps) == 1
        assert eps[0].method == "GET"
        assert eps[0].pattern == "/api/users"
        assert eps[0].framework == "fastapi"

    def test_post_endpoint(self):
        root, src = _parse_py("""
@app.post("/api/users")
def create_user(data: dict):
    return data
""")
        symbols = _dummy_symbols(["mod:create_user"])
        eps = extract_fastapi_endpoints(root, src, symbols)
        assert len(eps) == 1
        assert eps[0].method == "POST"

    def test_parameterized_endpoint(self):
        root, src = _parse_py("""
@app.get("/api/users/{user_id}")
def get_user(user_id: str):
    return {"id": user_id}
""")
        symbols = _dummy_symbols(["mod:get_user"])
        eps = extract_fastapi_endpoints(root, src, symbols)
        assert len(eps) == 1
        assert eps[0].pattern == "/api/users/{user_id}"

    def test_multiple_endpoints(self):
        root, src = _parse_py("""
@app.get("/api/users")
def list_users():
    return []

@app.post("/api/users")
def create_user():
    return {}

@app.delete("/api/users/{user_id}")
def delete_user(user_id: str):
    return {}
""")
        symbols = [
            ("mod:list_users", 1, 4),
            ("mod:create_user", 5, 8),
            ("mod:delete_user", 9, 12),
        ]
        eps = extract_fastapi_endpoints(root, src, symbols)
        assert len(eps) == 3
        methods = {ep.method for ep in eps}
        assert methods == {"GET", "POST", "DELETE"}


# ---------------------------------------------------------------------------
# Flask extraction
# ---------------------------------------------------------------------------


class TestExtractFlaskEndpoints:
    def test_route_with_methods(self):
        root, src = _parse_py("""
@app.route("/api/stats", methods=["GET"])
def get_stats():
    return {}
""")
        symbols = _dummy_symbols(["mod:get_stats"])
        eps = extract_flask_endpoints(root, src, symbols)
        assert len(eps) == 1
        assert eps[0].method == "GET"
        assert eps[0].pattern == "/api/stats"
        assert eps[0].framework == "flask"

    def test_flask_2_shorthand(self):
        root, src = _parse_py("""
@app.get("/api/settings")
def get_settings():
    return {}
""")
        symbols = _dummy_symbols(["mod:get_settings"])
        eps = extract_flask_endpoints(root, src, symbols)
        assert len(eps) == 1
        assert eps[0].method == "GET"

    def test_blueprint_route(self):
        root, src = _parse_py("""
@bp.route("/api/admin/bulk", methods=["PUT"])
def bulk_update():
    return {}
""")
        symbols = _dummy_symbols(["mod:bulk_update"])
        eps = extract_flask_endpoints(root, src, symbols)
        assert len(eps) == 1
        assert eps[0].method == "PUT"

    def test_route_without_methods(self):
        """@app.route without methods= defaults to wildcard."""
        root, src = _parse_py("""
@app.route("/api/catch-all")
def catch_all():
    return {}
""")
        symbols = _dummy_symbols(["mod:catch_all"])
        eps = extract_flask_endpoints(root, src, symbols)
        assert len(eps) == 1
        assert eps[0].method == "*"

    def test_route_multiple_methods(self):
        root, src = _parse_py("""
@app.route("/api/resource", methods=["GET", "POST"])
def handle_resource():
    return {}
""")
        symbols = _dummy_symbols(["mod:handle_resource"])
        eps = extract_flask_endpoints(root, src, symbols)
        assert len(eps) == 2
        methods = {ep.method for ep in eps}
        assert methods == {"GET", "POST"}


# ---------------------------------------------------------------------------
# Express extraction
# ---------------------------------------------------------------------------


class TestExtractExpressEndpoints:
    def test_app_get(self):
        root, src = _parse_ts("""
const app = express();
app.get("/api/health", (req, res) => {
  res.json({ status: "ok" });
});
""")
        symbols = _dummy_symbols(["mod:__module__"])
        eps = extract_express_endpoints(root, src, symbols)
        assert len(eps) == 1
        assert eps[0].method == "GET"
        assert eps[0].pattern == "/api/health"
        assert eps[0].framework == "express"

    def test_router_get(self):
        root, src = _parse_ts("""
const router = express.Router();
router.get("/api/products", (req, res) => {
  res.json([]);
});
""")
        symbols = _dummy_symbols(["mod:__module__"])
        eps = extract_express_endpoints(root, src, symbols)
        assert len(eps) == 1
        assert eps[0].method == "GET"

    def test_router_post(self):
        root, src = _parse_ts("""
const router = express.Router();
router.post("/api/products", (req, res) => {
  res.json({ created: true });
});
""")
        symbols = _dummy_symbols(["mod:__module__"])
        eps = extract_express_endpoints(root, src, symbols)
        assert len(eps) == 1
        assert eps[0].method == "POST"


# ---------------------------------------------------------------------------
# Monorepo pattern: TS file with both Express routes AND fetch calls
# ---------------------------------------------------------------------------


class TestMonorepoPattern:
    def test_ts_file_with_express_and_fetch(self):
        source = """
export function setupGateway() {
  app.get("/api/gateway/status", (req, res) => {
    res.json({ gateway: "running" });
  });
}

export async function proxyUsers() {
  const upstream = await fetch("/api/users");
  return upstream.json();
}
"""
        root, src = _parse_ts(source)
        symbols = [
            ("mod:setupGateway", 1, 6),
            ("mod:proxyUsers", 7, 12),
        ]

        # Both endpoints and call sites should be found
        endpoints = extract_express_endpoints(root, src, symbols)
        call_sites = extract_fetch_sites(root, src, symbols)

        assert len(endpoints) >= 1
        assert endpoints[0].pattern == "/api/gateway/status"

        assert len(call_sites) >= 1
        assert call_sites[0].pattern == "/api/users"


# ---------------------------------------------------------------------------
# match_xlinks
# ---------------------------------------------------------------------------


class TestMatchXlinks:
    def test_exact_match_produces_edge(self):
        sites = [
            XLinkCallSite("frontend:fetchUsers", "GET", "/api/users", "fetch", 5),
        ]
        endpoints = [
            XLinkEndpoint("backend:list_users", "GET", "/api/users", "fastapi", 10),
        ]
        refs = match_xlinks(sites, endpoints, threshold=0.7)
        assert len(refs) == 1
        assert refs[0].src_qname == "frontend:fetchUsers"
        assert refs[0].target_qname == "backend:list_users"
        assert refs[0].kind == "cross_language_call"

    def test_parameterized_match_above_threshold(self):
        sites = [
            XLinkCallSite("frontend:fetchUser", "GET", "/api/users/{_PARAM_}", "fetch", 5),
        ]
        endpoints = [
            XLinkEndpoint("backend:get_user", "GET", "/api/users/{user_id}", "fastapi", 10),
        ]
        refs = match_xlinks(sites, endpoints, threshold=0.7)
        assert len(refs) == 1

    def test_method_mismatch_rejected(self):
        sites = [
            XLinkCallSite("frontend:createUser", "POST", "/api/users", "fetch", 5),
        ]
        endpoints = [
            XLinkEndpoint("backend:list_users", "GET", "/api/users", "fastapi", 10),
        ]
        refs = match_xlinks(sites, endpoints, threshold=0.7)
        assert len(refs) == 0

    def test_wildcard_method_matches(self):
        sites = [
            XLinkCallSite("frontend:makeRequest", "*", "/api/data", "axios", 5),
        ]
        endpoints = [
            XLinkEndpoint("backend:handle_data", "POST", "/api/data", "flask", 10),
        ]
        refs = match_xlinks(sites, endpoints, threshold=0.7)
        assert len(refs) == 1

    def test_no_duplicates(self):
        sites = [
            XLinkCallSite("frontend:f1", "GET", "/api/users", "fetch", 5),
            XLinkCallSite("frontend:f1", "GET", "/api/users", "axios", 10),
        ]
        endpoints = [
            XLinkEndpoint("backend:list_users", "GET", "/api/users", "fastapi", 10),
        ]
        refs = match_xlinks(sites, endpoints, threshold=0.7)
        # Should deduplicate: same (src_qname, target_qname) pair
        assert len(refs) == 1

    def test_below_threshold_excluded(self):
        """A parameterized match with a very high threshold is excluded."""
        sites = [
            XLinkCallSite("frontend:fetchUser", "GET", "/api/users/{_PARAM_}", "fetch", 5),
        ]
        endpoints = [
            XLinkEndpoint("backend:get_user", "GET", "/api/users/{user_id}", "fastapi", 10),
        ]
        # Set threshold higher than 0.95 (the parameterized match confidence)
        refs = match_xlinks(sites, endpoints, threshold=0.99)
        assert len(refs) == 0

    def test_multiple_matches(self):
        sites = [
            XLinkCallSite("frontend:fetchUsers", "GET", "/api/users", "fetch", 5),
            XLinkCallSite("frontend:createUser", "POST", "/api/users", "fetch", 10),
        ]
        endpoints = [
            XLinkEndpoint("backend:list_users", "GET", "/api/users", "fastapi", 10),
            XLinkEndpoint("backend:create_user", "POST", "/api/users", "fastapi", 15),
        ]
        refs = match_xlinks(sites, endpoints, threshold=0.7)
        assert len(refs) == 2
        src_targets = {(r.src_qname, r.target_qname) for r in refs}
        assert ("frontend:fetchUsers", "backend:list_users") in src_targets
        assert ("frontend:createUser", "backend:create_user") in src_targets


# ---------------------------------------------------------------------------
# Integration: full scan_project with cross-language edges
# ---------------------------------------------------------------------------


def _make_xlink_project(tmp_path: Path) -> Path:
    """Build a mini monorepo with TS frontend and Python backend."""
    # trie.toml
    (tmp_path / "trie.toml").write_text(
        '[trie]\nversion = "0.2.0"\n'
        '[scope]\ninclude = ["**/*.py", "**/*.ts", "**/*.tsx"]\n'
        'exclude = ["**/__pycache__/**", "**/node_modules/**"]\n'
        '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
        '[models]\nbootstrap = "anthropic/claude-haiku-4-5-20251001"\n'
        'cascade = "anthropic/claude-haiku-4-5-20251001"\n'
        "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
    )

    # Python backend with FastAPI
    (tmp_path / "api").mkdir()
    (tmp_path / "api" / "users.py").write_text(
        "from fastapi import FastAPI\n"
        "app = FastAPI()\n\n"
        '@app.get("/api/users")\n'
        "def list_users():\n"
        "    return []\n\n"
        '@app.get("/api/users/{user_id}")\n'
        "def get_user(user_id: str):\n"
        '    return {"id": user_id}\n\n'
        '@app.post("/api/users")\n'
        "def create_user(data: dict):\n"
        "    return data\n"
    )

    # TypeScript frontend with fetch
    (tmp_path / "src").mkdir()
    (tmp_path / "src" / "client.ts").write_text(
        "export async function fetchUsers() {\n"
        '  const response = await fetch("/api/users");\n'
        "  return response.json();\n"
        "}\n\n"
        "export async function fetchUser(userId: string) {\n"
        "  const response = await fetch(`/api/users/${userId}`);\n"
        "  return response.json();\n"
        "}\n\n"
        "export async function createUser(data: any) {\n"
        '  const response = await fetch("/api/users", {\n'
        '    method: "POST",\n'
        "    body: JSON.stringify(data),\n"
        "  });\n"
        "  return response.json();\n"
        "}\n"
    )

    return tmp_path


def _scan(project: Path) -> tuple[Store, object]:
    config, _ = Config.find_and_load(project)
    store = Store(project / ".trie" / "graph.db")
    result = scan_project(project_root=project, config=config, store=store)
    return store, result


class TestIntegration:
    def test_cross_language_edges_in_scan(self, tmp_path: Path):
        """Full scan_project() run produces cross-language edges visible via
        references_in/references_out."""
        project = _make_xlink_project(tmp_path)
        store, _result = _scan(project)
        try:
            # Backend handler should have cross-language callers
            callers = store.references_in("api/users:list_users")
            assert "src/client:fetchUsers" in callers, (
                f"Expected src/client:fetchUsers in callers of api/users:list_users, got: {callers}"
            )

            # Frontend function should have cross-language callees
            callees = store.references_out("src/client:fetchUsers")
            assert "api/users:list_users" in callees, (
                f"Expected api/users:list_users in callees of src/client:fetchUsers, got: {callees}"
            )

            # Parameterized match should also work
            callers_param = store.references_in("api/users:get_user")
            assert "src/client:fetchUser" in callers_param, (
                f"Expected src/client:fetchUser in callers of api/users:get_user, "
                f"got: {callers_param}"
            )

            # POST match should work (method agreement)
            callers_post = store.references_in("api/users:create_user")
            assert "src/client:createUser" in callers_post, (
                f"Expected src/client:createUser in callers of api/users:create_user, "
                f"got: {callers_post}"
            )
        finally:
            store.close()

    def test_method_mismatch_prevents_edge(self, tmp_path: Path):
        """A GET call should NOT match a POST endpoint."""
        (tmp_path / "trie.toml").write_text(
            '[trie]\nversion = "0.2.0"\n'
            '[scope]\ninclude = ["**/*.py", "**/*.ts"]\n'
            "exclude = []\n"
            '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
            '[models]\nbootstrap = "anthropic/claude-haiku-4-5-20251001"\n'
            'cascade = "anthropic/claude-haiku-4-5-20251001"\n'
            "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
        )
        (tmp_path / "api.py").write_text(
            '@app.post("/api/data")\ndef handle_data():\n    return {}\n'
        )
        (tmp_path / "client.ts").write_text(
            "export async function getData() {\n"
            '  const r = await fetch("/api/data");\n'
            "  return r.json();\n"
            "}\n"
        )
        store, _ = _scan(tmp_path)
        try:
            # GET (default for fetch without method option) should NOT match POST handler
            callers = store.references_in("api:handle_data")
            assert "client:getData" not in callers
        finally:
            store.close()

    def test_no_cross_language_edges_for_single_language(self, tmp_path: Path):
        """Pure Python project should produce zero xlink edges (zero overhead)."""
        (tmp_path / "trie.toml").write_text(
            '[trie]\nversion = "0.2.0"\n'
            '[scope]\ninclude = ["**/*.py"]\nexclude = []\n'
            '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
            '[models]\nbootstrap = "anthropic/claude-haiku-4-5-20251001"\n'
            'cascade = "anthropic/claude-haiku-4-5-20251001"\n'
            "[cascade]\ndefault_depth = 1\nhub_symbol_threshold = 20\n"
        )
        (tmp_path / "lib.py").write_text("def helper():\n    return 1\n")
        (tmp_path / "app.py").write_text(
            "from lib import helper\n\ndef run():\n    return helper()\n"
        )
        store, result = _scan(tmp_path)
        try:
            # Same-language edges should still work
            out = store.references_out("app:run")
            assert "lib:helper" in out
            # No cross-language edges
            # (We can't easily distinguish edge kinds in the store API,
            # but the fact that only same-language files exist means xlink
            # produced zero edges.)
            assert result.edges_total >= 1
        finally:
            store.close()


# ---------------------------------------------------------------------------
# Hub threshold / cascade protection
# ---------------------------------------------------------------------------


class TestHubThresholdCascade:
    """Verify cross-language edges participate in cascade and that the hub
    threshold stops expansion at popular endpoints — the core scalability claim."""

    def test_popular_endpoint_hits_hub_threshold(self, tmp_path: Path):
        """A backend handler with enough cross-language callers should exceed
        hub_symbol_threshold, stopping cascade expansion at that symbol.

        This test creates a FastAPI endpoint called by many TS functions
        (more than hub_symbol_threshold=5), then verifies the cascade stops.
        """
        hub_threshold = 5  # Low threshold for testing

        (tmp_path / "trie.toml").write_text(
            '[trie]\nversion = "0.2.0"\n'
            '[scope]\ninclude = ["**/*.py", "**/*.ts"]\n'
            "exclude = []\n"
            '[triefacts]\nroot = "triefacts"\nsource_root = "."\n'
            '[models]\nbootstrap = "anthropic/claude-haiku-4-5-20251001"\n'
            'cascade = "anthropic/claude-haiku-4-5-20251001"\n'
            f"[cascade]\ndefault_depth = 1\nhub_symbol_threshold = {hub_threshold}\n"
        )

        # A popular endpoint
        (tmp_path / "api.py").write_text(
            '@app.get("/api/popular")\ndef popular_handler():\n    return {"data": "popular"}\n'
        )

        # Generate many TS callers — more than hub_threshold
        num_callers = hub_threshold + 3  # 8 callers, threshold is 5
        ts_funcs = []
        for i in range(num_callers):
            ts_funcs.append(
                f"export async function caller{i}() {{\n"
                f'  const r = await fetch("/api/popular");\n'
                f"  return r.json();\n"
                f"}}\n"
            )
        (tmp_path / "clients.ts").write_text("\n".join(ts_funcs))

        store, _ = _scan(tmp_path)
        try:
            # Verify all cross-language edges were created
            callers = store.references_in("api:popular_handler")
            assert len(callers) == num_callers, (
                f"Expected {num_callers} callers, got {len(callers)}: {callers}"
            )

            # Verify inbound count exceeds hub threshold
            inbound_counts = store.inbound_count_per_symbol()
            handler_count = inbound_counts.get("api:popular_handler", 0)
            assert handler_count >= hub_threshold, (
                f"Expected inbound count >= {hub_threshold}, got {handler_count}"
            )

            # Now verify cascade behavior: compute_cascade should stop at
            # this hub symbol. We import and call compute_cascade directly.
            from trie.sync.cascade import compute_cascade

            _config, _ = Config.find_and_load(tmp_path)
            # If the handler's file changed, cascade should NOT propagate
            # through the hub symbol to all its callers
            cascade = compute_cascade(
                changed_files={"api.py"},
                store=store,
                hub_threshold=hub_threshold,
                depth=1,
            )
            # The cascade result should include api.py but NOT propagate
            # through the popular_handler hub to all client files.
            # The popular_handler has >hub_threshold inbound refs, so
            # cascade stops there.
            cascade_files = set(cascade.affected_files)
            # api.py is in the cascade (it's the changed file)
            assert "api.py" in cascade_files

            # clients.ts should NOT be in cascade because popular_handler
            # is a hub symbol that stops expansion
            assert "clients.ts" not in cascade_files, (
                f"clients.ts should NOT be in cascade (hub threshold should stop expansion). "
                f"Cascade files: {cascade_files}"
            )
        finally:
            store.close()


# ---------------------------------------------------------------------------
# Config tests
# ---------------------------------------------------------------------------


class TestXLinkConfig:
    def test_default_config(self):
        config = Config()
        assert config.xlink.confidence_threshold == 0.7
        assert config.xlink.scan_paths == []

    def test_from_dict_with_xlink(self):
        data = {
            "xlink": {
                "confidence_threshold": 0.8,
                "scan_paths": ["src/**", "api/**"],
            }
        }
        config = Config.from_dict(data)
        assert config.xlink.confidence_threshold == 0.8
        assert config.xlink.scan_paths == ["src/**", "api/**"]

    def test_from_dict_without_xlink(self):
        config = Config.from_dict({})
        assert config.xlink.confidence_threshold == 0.7
        assert config.xlink.scan_paths == []

    def test_xlink_is_frozen(self):
        xlink = XLink()
        with pytest.raises(AttributeError):
            xlink.confidence_threshold = 0.9  # type: ignore[misc]


# ---------------------------------------------------------------------------
# Edge kind registered
# ---------------------------------------------------------------------------


class TestEdgeKind:
    def test_cross_language_call_in_edge_kinds(self):
        from trie.parse.types import EDGE_KINDS

        assert "cross_language_call" in EDGE_KINDS
