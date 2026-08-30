"""Cross-language edge detection: API call sites ↔ route handlers.

Detects HTTP API boundaries between languages — e.g. a TypeScript
``fetch("/api/users")`` calling a FastAPI ``@app.get("/api/users")`` handler —
and produces ``Reference(kind="cross_language_call")`` edges that flow through
the existing graph infrastructure with zero special-casing.

Three-phase post-scan pass:

  Phase A — EXTRACTION (per-file, tree-sitter AST walk):
    TS/TSX/JS → ``XLinkCallSite`` records (fetch, axios) + ``XLinkEndpoint``
    records (Express routes).
    Python → ``XLinkEndpoint`` records (FastAPI, Flask).

  Phase B — MATCHING (cross-file):
    Join call sites to endpoints by URL pattern + HTTP method.
    Apply confidence threshold; produce ``Reference`` objects.

  Phase C — INSERTION:
    Merge into ``pending_refs`` before ``replace_all_edges`` in scan_project().

See the cross-language-edges plan document for the full design rationale.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from pathlib import Path

import tree_sitter_python
import tree_sitter_typescript as tst
from tree_sitter import Language, Node, Parser

from trie.config import Config
from trie.graph.store import Store
from trie.parse.types import Reference

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Tree-sitter setup — reuse the same language objects as the main parsers
# ---------------------------------------------------------------------------

_PY_LANGUAGE = Language(tree_sitter_python.language())
_TS_LANGUAGE = Language(tst.language_typescript())
_TSX_LANGUAGE = Language(tst.language_tsx())

# HTTP methods recognised by the matcher.
_HTTP_METHODS = frozenset({"GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"})

# Wildcard sentinel used during URL normalisation to represent a path parameter.
_PARAM_WILDCARD = "{_PARAM_}"


# ---------------------------------------------------------------------------
# Data types
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class XLinkCallSite:
    """An HTTP API call site detected in a TS/JS file."""

    src_qname: str  # symbol containing the call
    method: str  # "GET", "POST", … or "*" if unknown
    pattern: str  # normalised URL pattern e.g. "/api/users/{_PARAM_}"
    framework: str  # "fetch" or "axios"
    line: int  # 1-based line number


@dataclass(frozen=True)
class XLinkEndpoint:
    """A server-side route handler definition."""

    handler_qname: str  # symbol that handles the route
    method: str  # "GET", "POST", … or "*" for any-method routes
    pattern: str  # normalised URL pattern
    framework: str  # "fastapi", "flask", or "express"
    line: int  # 1-based line number


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_ts_parser(file_path: Path) -> Parser:
    """Create a tree-sitter parser for a TS/JS file.

    Uses the TSX grammar for .tsx and .jsx files, plain TS otherwise
    (TS grammar is a superset of JS).
    """
    parser = Parser()
    name = file_path.name
    parser.language = _TSX_LANGUAGE if name.endswith((".tsx", ".jsx")) else _TS_LANGUAGE
    return parser


def _make_py_parser() -> Parser:
    parser = Parser()
    parser.language = _PY_LANGUAGE
    return parser


def _node_text(node: Node, source: bytes) -> str:
    return source[node.start_byte : node.end_byte].decode("utf-8", errors="replace")


def _module_key_ts(file_path: Path, source_root: Path) -> str:
    """Compute the qname prefix for a TS/JS file — same logic as typescript.py."""
    rel = file_path.relative_to(source_root)
    s = str(rel)
    for ext in (".d.ts", ".tsx", ".ts", ".jsx", ".mjs", ".cjs", ".js"):
        if s.endswith(ext):
            return s[: -len(ext)]
    return str(rel.with_suffix(""))


def _module_key_py(file_path: Path, source_root: Path) -> str:
    """Compute the qname prefix for a Python file — same logic as python.py."""
    rel = file_path.relative_to(source_root)
    return str(rel.with_suffix(""))


def _find_enclosing_symbol(
    line: int,
    symbols: list[tuple[str, int, int]],
) -> str | None:
    """Find the innermost symbol whose line range contains ``line``.

    ``symbols`` is a list of ``(qname, start_line, end_line)`` tuples sorted by
    start_line (as returned by ``Store.symbols_in_file_with_lines``). Returns
    the qname of the tightest enclosing symbol, or None if no match.
    """
    best: str | None = None
    best_span = float("inf")
    for qname, start, end in symbols:
        if start <= line <= end:
            span = end - start
            if span < best_span:
                best = qname
                best_span = span
    return best


def _string_value_from_node(node: Node, source: bytes) -> str | None:
    """Extract the string value from a string or template_string node.

    For plain strings: returns the content without quotes.
    For template strings: returns the static prefix with ${...} replaced by
    parameter wildcards.
    Returns None for nodes that aren't strings.
    """
    if node.type == "string" or node.type == "string_fragment":
        # tree-sitter wraps the content in a string node with quote children
        # The string_fragment child holds the actual content
        if node.type == "string":
            for c in node.named_children:
                if c.type == "string_fragment":
                    return _node_text(c, source)
            # Fallback: strip quotes from the full text
            text = _node_text(node, source)
            if len(text) >= 2 and text[0] in ('"', "'", "`"):
                return text[1:-1]
            return text
        return _node_text(node, source)

    if node.type == "template_string":
        # Template literal: reconstruct from fragments + substitutions
        parts: list[str] = []
        for child in node.children:
            if child.type == "string_fragment":
                parts.append(_node_text(child, source))
            elif child.type == "template_substitution":
                parts.append(_PARAM_WILDCARD)
            # Skip ` and other punctuation
        return "".join(parts)

    return None


def _extract_string_arg(node: Node, source: bytes) -> str | None:
    """Extract a URL string from a call argument node.

    Handles both string literals and template literals.
    """
    if node.type in ("string", "template_string"):
        return _string_value_from_node(node, source)
    # Sometimes wrapped in parentheses or other expressions
    for c in node.named_children:
        result = _extract_string_arg(c, source)
        if result is not None:
            return result
    return None


# ---------------------------------------------------------------------------
# Client-side extractors (TypeScript/JS)
# ---------------------------------------------------------------------------


def _get_arguments_node(call_node: Node) -> Node | None:
    """Get the arguments node from a call expression."""
    return call_node.child_by_field_name("arguments")


def _extract_method_from_options(args_node: Node, source: bytes) -> str:
    """Extract HTTP method from a fetch options object (second argument).

    Looks for ``{method: "POST"}`` in the options object.
    Returns the method string or "*" if not found.
    """
    # The options object is typically the second argument
    named = args_node.named_children
    if len(named) < 2:
        return "GET"  # fetch with no options defaults to GET

    opts = named[1]
    if opts.type != "object":
        return "GET"

    for prop in opts.named_children:
        if prop.type == "pair":
            key_node = prop.child_by_field_name("key")
            val_node = prop.child_by_field_name("value")
            if key_node is None or val_node is None:
                continue
            key_text = _node_text(key_node, source).strip('"').strip("'")
            if key_text == "method":
                val_text = _node_text(val_node, source).strip('"').strip("'")
                upper = val_text.upper()
                if upper in _HTTP_METHODS:
                    return upper
    return "GET"


def extract_fetch_sites(
    tree: Node,
    source: bytes,
    file_symbols: list[tuple[str, int, int]],
) -> list[XLinkCallSite]:
    """Extract ``fetch(url)`` and ``fetch(url, {method: ...})`` call sites."""
    sites: list[XLinkCallSite] = []

    def walk(node: Node) -> None:
        if node.type == "call_expression":
            fn = node.child_by_field_name("function")
            # Handle await fetch(...) — the function is the inner call
            if fn is not None and fn.type == "await_expression":
                # Recurse into the await — the call_expression is inside
                for c in fn.named_children:
                    walk(c)
                return

            if fn is not None and fn.type == "identifier" and _node_text(fn, source) == "fetch":
                args = _get_arguments_node(node)
                if args is not None and args.named_children:
                    url_str = _extract_string_arg(args.named_children[0], source)
                    if url_str is not None:
                        method = _extract_method_from_options(args, source)
                        line = node.start_point[0] + 1
                        sym = _find_enclosing_symbol(line, file_symbols)
                        if sym is not None:
                            sites.append(
                                XLinkCallSite(
                                    src_qname=sym,
                                    method=method,
                                    pattern=url_str,
                                    framework="fetch",
                                    line=line,
                                )
                            )
        for c in node.children:
            walk(c)

    walk(tree)
    return sites


def extract_axios_sites(
    tree: Node,
    source: bytes,
    file_symbols: list[tuple[str, int, int]],
) -> list[XLinkCallSite]:
    """Extract axios call sites.

    Handles:
    - ``axios.get(url)``, ``axios.post(url)``, etc.
    - ``axios({url: ..., method: ...})``
    """
    sites: list[XLinkCallSite] = []

    def walk(node: Node) -> None:
        if node.type == "call_expression":
            fn = node.child_by_field_name("function")
            if fn is None:
                for c in node.children:
                    walk(c)
                return

            args = _get_arguments_node(node)
            if args is None or not args.named_children:
                for c in node.children:
                    walk(c)
                return

            # axios.get(url), axios.post(url), etc.
            if fn.type == "member_expression":
                obj = fn.child_by_field_name("object")
                prop = fn.child_by_field_name("property")
                if obj is not None and prop is not None and _node_text(obj, source) == "axios":
                    method_name = _node_text(prop, source).upper()
                    if method_name in _HTTP_METHODS:
                        url_str = _extract_string_arg(args.named_children[0], source)
                        if url_str is not None:
                            line = node.start_point[0] + 1
                            sym = _find_enclosing_symbol(line, file_symbols)
                            if sym is not None:
                                sites.append(
                                    XLinkCallSite(
                                        src_qname=sym,
                                        method=method_name,
                                        pattern=url_str,
                                        framework="axios",
                                        line=line,
                                    )
                                )

            # axios({url: ..., method: ...})
            elif fn.type == "identifier" and _node_text(fn, source) == "axios":
                first_arg = args.named_children[0]
                if first_arg.type == "object":
                    url_val: str | None = None
                    method_val = "*"
                    for prop in first_arg.named_children:
                        if prop.type == "pair":
                            key_node = prop.child_by_field_name("key")
                            val_node = prop.child_by_field_name("value")
                            if key_node is None or val_node is None:
                                continue
                            key_text = _node_text(key_node, source).strip('"').strip("'")
                            if key_text == "url":
                                url_val = _extract_string_arg(val_node, source)
                            elif key_text == "method":
                                val_text = _node_text(val_node, source).strip('"').strip("'")
                                upper = val_text.upper()
                                if upper in _HTTP_METHODS:
                                    method_val = upper
                    if url_val is not None:
                        line = node.start_point[0] + 1
                        sym = _find_enclosing_symbol(line, file_symbols)
                        if sym is not None:
                            sites.append(
                                XLinkCallSite(
                                    src_qname=sym,
                                    method=method_val,
                                    pattern=url_val,
                                    framework="axios",
                                    line=line,
                                )
                            )

        for c in node.children:
            walk(c)

    walk(tree)
    return sites


# ---------------------------------------------------------------------------
# Server-side extractors (Python)
# ---------------------------------------------------------------------------


def _extract_decorator_route_info(
    decorator_node: Node,
    source: bytes,
) -> tuple[str, str] | None:
    """Extract (method, pattern) from a Python decorator node.

    Handles:
    - ``@app.get("/path")``, ``@app.post("/path")`` etc. (FastAPI + Flask 2.0+)
    - ``@app.route("/path", methods=["GET"])``, ``@bp.route("/path")``

    Returns None if the decorator doesn't look like a route decorator.
    """
    # The decorator node text includes the @
    text = _node_text(decorator_node, source)
    if not text.startswith("@"):
        return None

    # Find the call_expression inside the decorator
    # tree-sitter Python grammar: decorator -> "@" expression
    # The expression is typically a call (e.g. app.get("/path"))
    call_node: Node | None = None
    for c in decorator_node.named_children:
        if c.type == "call":
            call_node = c
            break
    if call_node is None:
        return None

    # Get the function being called
    fn_node = call_node.child_by_field_name("function")
    if fn_node is None:
        return None

    # Must be a dotted call: app.get, app.route, bp.route, etc.
    if fn_node.type != "attribute":
        return None

    attr_node = fn_node.child_by_field_name("attribute")
    if attr_node is None:
        return None
    method_name = _node_text(attr_node, source).lower()

    # Get the arguments
    args_node = call_node.child_by_field_name("arguments")
    if args_node is None:
        return None

    # Extract the URL pattern from the first positional argument
    first_string: str | None = None
    for arg in args_node.named_children:
        if arg.type == "string":
            first_string = _py_string_value(arg, source)
            break

    if first_string is None:
        return None

    # Determine HTTP method
    if method_name in ("get", "post", "put", "delete", "patch", "head", "options"):
        return (method_name.upper(), first_string)

    if method_name == "route":
        # Look for methods= keyword argument
        methods = _extract_methods_kwarg(args_node, source)
        if methods:
            # Return the first method; if multiple, we'll create multiple entries
            return (methods[0], first_string)
        return ("*", first_string)

    return None


def _py_string_value(string_node: Node, source: bytes) -> str | None:
    """Extract the string content from a Python string node."""
    text = _node_text(string_node, source)
    # Handle various quote styles
    for prefix in ('f"', "f'", 'f"""', "f'''", 'r"', "r'", 'b"', "b'"):
        if text.startswith(prefix):
            text = text[len(prefix) :]
            break
    # Strip quotes
    if text.startswith('"""') or text.startswith("'''"):
        return text[3:-3] if len(text) >= 6 else None
    if text.startswith('"') or text.startswith("'"):
        return text[1:-1] if len(text) >= 2 else None
    return None


def _extract_methods_kwarg(args_node: Node, source: bytes) -> list[str]:
    """Extract methods from a ``methods=["GET", "POST"]`` keyword argument."""
    methods: list[str] = []
    for arg in args_node.named_children:
        if arg.type == "keyword_argument":
            name_node = arg.child_by_field_name("name")
            val_node = arg.child_by_field_name("value")
            if name_node is None or val_node is None:
                continue
            if _node_text(name_node, source) == "methods" and val_node.type == "list":
                for item in val_node.named_children:
                    if item.type == "string":
                        s = _py_string_value(item, source)
                        if s is not None:
                            methods.append(s.upper())
    return methods


def _extract_decorator_route_info_multi(
    decorator_node: Node,
    source: bytes,
) -> list[tuple[str, str]]:
    """Extract all (method, pattern) pairs from a decorator.

    For ``@app.route("/path", methods=["GET", "POST"])``, returns two entries.
    For ``@app.get("/path")``, returns one.
    """
    result = _extract_decorator_route_info(decorator_node, source)
    if result is None:
        return []

    method, pattern = result
    if method == "*":
        return [("*", pattern)]

    # For route() with multiple methods, re-extract to get all of them
    call_node: Node | None = None
    for c in decorator_node.named_children:
        if c.type == "call":
            call_node = c
            break
    if call_node is None:
        return [(method, pattern)]

    fn_node = call_node.child_by_field_name("function")
    if fn_node is None or fn_node.type != "attribute":
        return [(method, pattern)]

    attr_node = fn_node.child_by_field_name("attribute")
    if attr_node is None:
        return [(method, pattern)]

    method_name = _node_text(attr_node, source).lower()
    if method_name == "route":
        args_node = call_node.child_by_field_name("arguments")
        if args_node is not None:
            methods = _extract_methods_kwarg(args_node, source)
            if methods:
                return [(m, pattern) for m in methods]
        return [("*", pattern)]

    return [(method, pattern)]


def extract_fastapi_endpoints(
    tree: Node,
    source: bytes,
    file_symbols: list[tuple[str, int, int]],
) -> list[XLinkEndpoint]:
    """Extract FastAPI route definitions from a Python file's AST.

    Detects ``@app.get("/path")``, ``@app.post("/path")``, etc.
    """
    return _extract_py_decorator_endpoints(tree, source, file_symbols, "fastapi")


def extract_flask_endpoints(
    tree: Node,
    source: bytes,
    file_symbols: list[tuple[str, int, int]],
) -> list[XLinkEndpoint]:
    """Extract Flask route definitions from a Python file's AST.

    Detects ``@app.route("/path", methods=["GET"])``, ``@app.get("/path")``
    (Flask 2.0+), and ``@bp.route("/path")``.
    """
    return _extract_py_decorator_endpoints(tree, source, file_symbols, "flask")


def _extract_py_decorator_endpoints(
    tree: Node,
    source: bytes,
    file_symbols: list[tuple[str, int, int]],
    framework: str,
) -> list[XLinkEndpoint]:
    """Shared extractor for FastAPI and Flask decorator-based routes."""
    endpoints: list[XLinkEndpoint] = []

    def walk(node: Node) -> None:
        if node.type == "decorated_definition":
            # Get the decorators
            for child in node.named_children:
                if child.type == "decorator":
                    routes = _extract_decorator_route_info_multi(child, source)
                    if routes:
                        # Get the function being decorated
                        func_node = node.child_by_field_name("definition")
                        if func_node is not None:
                            func_line = func_node.start_point[0] + 1
                            sym = _find_enclosing_symbol(func_line, file_symbols)
                            if sym is not None:
                                for method, pattern in routes:
                                    endpoints.append(
                                        XLinkEndpoint(
                                            handler_qname=sym,
                                            method=method,
                                            pattern=pattern,
                                            framework=framework,
                                            line=func_line,
                                        )
                                    )

        for c in node.named_children:
            walk(c)

    walk(tree)
    return endpoints


def extract_express_endpoints(
    tree: Node,
    source: bytes,
    file_symbols: list[tuple[str, int, int]],
) -> list[XLinkEndpoint]:
    """Extract Express.js route definitions from a TS/JS file's AST.

    Detects ``app.get("/path", handler)`` and ``router.get("/path", handler)``.
    """
    endpoints: list[XLinkEndpoint] = []

    def walk(node: Node) -> None:
        if node.type == "call_expression":
            fn = node.child_by_field_name("function")
            if fn is not None and fn.type == "member_expression":
                obj = fn.child_by_field_name("object")
                prop = fn.child_by_field_name("property")
                if obj is not None and prop is not None:
                    obj_text = _node_text(obj, source)
                    method_name = _node_text(prop, source).lower()

                    # Check if this looks like a route definition:
                    # app.get, router.get, app.post, router.post, etc.
                    if method_name in (
                        "get",
                        "post",
                        "put",
                        "delete",
                        "patch",
                        "head",
                        "options",
                    ) and _looks_like_express_receiver(obj_text):
                        args = _get_arguments_node(node)
                        if args is not None and args.named_children:
                            url_str = _extract_string_arg(args.named_children[0], source)
                            if url_str is not None:
                                line = node.start_point[0] + 1
                                sym = _find_enclosing_symbol(line, file_symbols)
                                if sym is not None:
                                    endpoints.append(
                                        XLinkEndpoint(
                                            handler_qname=sym,
                                            method=method_name.upper(),
                                            pattern=url_str,
                                            framework="express",
                                            line=line,
                                        )
                                    )

        for c in node.children:
            walk(c)

    walk(tree)
    return endpoints


def _looks_like_express_receiver(name: str) -> bool:
    """Heuristic: does this identifier look like an Express app or router?

    We accept any simple identifier — the false-positive risk is low because
    we also require the first argument to be a string that looks like a URL path.
    We reject dotted member expressions (e.g. ``this.cache.get``) to avoid
    matching non-Express method calls.
    """
    # Only accept simple identifiers, not dotted paths
    return "." not in name


# ---------------------------------------------------------------------------
# Language-based dispatch
# ---------------------------------------------------------------------------


def extract_ts_call_sites(
    file_path: Path,
    source_root: Path,
    file_symbols: list[tuple[str, int, int]],
) -> list[XLinkCallSite]:
    """Run all client extractors on a TS/TSX/JS file."""
    source = file_path.read_bytes()
    parser = _make_ts_parser(file_path)
    tree = parser.parse(source)

    sites: list[XLinkCallSite] = []
    sites.extend(extract_fetch_sites(tree.root_node, source, file_symbols))
    sites.extend(extract_axios_sites(tree.root_node, source, file_symbols))
    return sites


def extract_ts_endpoints(
    file_path: Path,
    source_root: Path,
    file_symbols: list[tuple[str, int, int]],
) -> list[XLinkEndpoint]:
    """Run Express extractor on a TS/JS file."""
    source = file_path.read_bytes()
    parser = _make_ts_parser(file_path)
    tree = parser.parse(source)

    return extract_express_endpoints(tree.root_node, source, file_symbols)


def extract_py_endpoints(
    file_path: Path,
    source_root: Path,
    file_symbols: list[tuple[str, int, int]],
) -> list[XLinkEndpoint]:
    """Run FastAPI + Flask extractors on a Python file."""
    source = file_path.read_bytes()
    parser = _make_py_parser()
    tree = parser.parse(source)

    endpoints: list[XLinkEndpoint] = []
    endpoints.extend(extract_fastapi_endpoints(tree.root_node, source, file_symbols))
    endpoints.extend(extract_flask_endpoints(tree.root_node, source, file_symbols))
    return endpoints


# ---------------------------------------------------------------------------
# URL normalisation and matching
# ---------------------------------------------------------------------------


def normalize_url(pattern: str) -> list[str]:
    """Normalise a URL pattern into segments for comparison.

    - Strip leading/trailing slashes
    - Lowercase
    - Split on ``/``
    - Replace parameter patterns (``{id}``, ``:id``, ``<type:id>``, ``{_PARAM_}``)
      with the wildcard sentinel
    """
    pattern = pattern.strip("/").lower()
    if not pattern:
        return []

    segments: list[str] = []
    for seg in pattern.split("/"):
        if not seg:
            continue
        # Parameter patterns: {id} (FastAPI/OpenAPI), :id (Express),
        # <type:id> (Flask), or already-wildcarded from template literals
        if (
            (seg.startswith("{") and seg.endswith("}"))
            or seg.startswith(":")
            or (seg.startswith("<") and seg.endswith(">"))
            or seg == _PARAM_WILDCARD
        ):
            segments.append(_PARAM_WILDCARD)
        else:
            segments.append(seg)

    return segments


def _match_confidence(
    site_segments: list[str],
    endpoint_segments: list[str],
    site_method: str,
    endpoint_method: str,
) -> float:
    """Compute match confidence between a call site and an endpoint.

    Returns 0.0 for hard rejections (method mismatch, different segment count).
    """
    # Method agreement check
    if site_method != "*" and endpoint_method != "*" and site_method != endpoint_method:
        return 0.0  # Hard rejection

    # Segment count must match
    if len(site_segments) != len(endpoint_segments):
        return 0.0

    if not site_segments:
        return 0.0

    # Compare segments
    all_exact = True
    for s_seg, e_seg in zip(site_segments, endpoint_segments, strict=True):
        if s_seg == _PARAM_WILDCARD or e_seg == _PARAM_WILDCARD:
            all_exact = False
            continue
        if s_seg != e_seg:
            return 0.0

    return 1.0 if all_exact else 0.95


def match_xlinks(
    sites: list[XLinkCallSite],
    endpoints: list[XLinkEndpoint],
    threshold: float,
) -> list[Reference]:
    """Match call sites to endpoints and produce Reference objects.

    Each call site is matched against every endpoint. Only matches with
    confidence >= threshold produce edges. Method mismatch is a hard rejection
    (confidence 0.0).
    """
    refs: list[Reference] = []
    seen: set[tuple[str, str]] = set()

    # Pre-normalise endpoint patterns
    endpoint_data: list[tuple[XLinkEndpoint, list[str]]] = [
        (ep, normalize_url(ep.pattern)) for ep in endpoints
    ]

    for site in sites:
        site_segments = normalize_url(site.pattern)

        for ep, ep_segments in endpoint_data:
            confidence = _match_confidence(site_segments, ep_segments, site.method, ep.method)
            if confidence < threshold:
                if confidence > 0.0:
                    logger.debug(
                        "XLink below threshold: %s -> %s (confidence=%.2f, threshold=%.2f)",
                        site.src_qname,
                        ep.handler_qname,
                        confidence,
                        threshold,
                    )
                continue

            # Avoid duplicate edges
            pair = (site.src_qname, ep.handler_qname)
            if pair in seen:
                continue
            seen.add(pair)

            refs.append(
                Reference(
                    src_qname=site.src_qname,
                    target_qname=ep.handler_qname,
                    kind="cross_language_call",
                )
            )

    return refs


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------


def xlink_resolve(
    *,
    store: Store,
    config: Config,
    source_root: Path,
    discovered_files: dict[str, Path],
) -> dict[str, list[Reference]]:
    """Run cross-language edge detection on all discovered files.

    This is the single entry point called from ``scan_project()``. It:
    1. Iterates over discovered files, dispatching to the appropriate extractors
       based on file extension.
    2. Matches call sites to endpoints.
    3. Returns a dict of ``{file_path: [Reference, ...]}`` suitable for merging
       into ``pending_refs``.

    Args:
        store: The graph store (used to look up existing symbols for qname attribution).
        config: Project configuration (for confidence threshold and scan_paths).
        source_root: Resolved source root path.
        discovered_files: Map of ``{relative_path: absolute_path}`` for all
            discovered files.
    """
    threshold = config.xlink.confidence_threshold
    scan_paths = config.xlink.scan_paths

    all_sites: list[XLinkCallSite] = []
    all_endpoints: list[XLinkEndpoint] = []

    for rel_path, abs_path in discovered_files.items():
        # Optional scan_paths filtering
        if scan_paths:
            from fnmatch import fnmatch

            if not any(fnmatch(rel_path, pat) for pat in scan_paths):
                continue

        # Get symbols for this file from the store (for qname attribution)
        file_symbols = store.symbols_in_file_with_lines(rel_path)
        if not file_symbols:
            continue

        name = abs_path.name
        suffix = abs_path.suffix

        # Language-based dispatch
        if suffix == ".py":
            # Python files: extract server endpoints (FastAPI + Flask)
            all_endpoints.extend(extract_py_endpoints(abs_path, source_root, file_symbols))
        elif name.endswith((".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs")):
            # TypeScript/JavaScript files: extract both client call sites AND
            # Express endpoints (a TS file can have both in a monorepo)
            all_sites.extend(extract_ts_call_sites(abs_path, source_root, file_symbols))
            all_endpoints.extend(extract_ts_endpoints(abs_path, source_root, file_symbols))

    if not all_sites or not all_endpoints:
        return {}

    # Phase B: Match call sites to endpoints
    refs = match_xlinks(all_sites, all_endpoints, threshold)

    if not refs:
        return {}

    # Group references by their source file (derived from src_qname's module part)
    result: dict[str, list[Reference]] = {}
    for ref in refs:
        # The module part of the qname is the file path minus extension
        module = ref.src_qname.split(":", 1)[0]
        # Find the actual file path from discovered_files
        src_file = _find_file_for_module(module, discovered_files)
        if src_file is not None:
            result.setdefault(src_file, []).append(ref)

    return result


def _find_file_for_module(module: str, discovered_files: dict[str, Path]) -> str | None:
    """Find the file path in discovered_files that corresponds to a module key.

    The module key is the file path minus its extension (e.g. "src/components/UserList").
    We need to find the actual file (e.g. "src/components/UserList.tsx").
    """
    # Try common extensions
    for ext in (".py", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs"):
        candidate = module + ext
        if candidate in discovered_files:
            return candidate
    return None
