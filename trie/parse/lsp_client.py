"""A minimal Language Server Protocol client over stdio.

Language servers (pyright, typescript-language-server, gopls, rust-analyzer, …)
all speak the same JSON-RPC-over-stdio protocol: spawn the process, exchange an
`initialize`/`initialized` handshake, `textDocument/didOpen` a file, then ask
positional questions like `textDocument/definition`. This client implements just
that slice — enough for a `ReferenceResolver` to resolve method/member calls to
their definitions — and nothing else.

Design notes:
  - A background reader thread drains stdout and dispatches framed messages by
    id, so request/response correlation works without blocking on unrelated
    server notifications (diagnostics, progress) or server→client requests.
  - Server→client requests (e.g. `client/registerCapability`,
    `workspace/configuration`) are answered with benign stubs so the server
    doesn't stall waiting on us.
  - The client is deliberately synchronous from the caller's view:
    `request(...)` blocks until the matching response arrives or the timeout
    elapses. Resolvers run per-file and want a straight-line call.
  - Every failure mode (missing binary, crash, timeout, malformed frame) raises
    `LspError`; callers treat that as "no resolver" and fall back to
    tree-sitter, never failing a scan.
"""

from __future__ import annotations

import contextlib
import json
import os
import subprocess
import threading
from pathlib import Path
from typing import Any


class LspError(RuntimeError):
    """Any LSP client failure — spawn, transport, timeout, or protocol."""


class LspClient:
    """Synchronous LSP client bound to one server process and workspace root."""

    def __init__(
        self,
        command: list[str],
        root: Path,
        *,
        timeout: float = 20.0,
    ) -> None:
        self._command = command
        self._root = root.resolve()
        self._timeout = timeout
        self._proc: subprocess.Popen[bytes] | None = None
        self._reader: threading.Thread | None = None
        self._lock = threading.Lock()
        self._next_id = 0
        self._pending: dict[int, threading.Event] = {}
        self._results: dict[int, dict[str, Any]] = {}
        self._alive = False

    # -- lifecycle ---------------------------------------------------------

    def start(self) -> None:
        """Spawn the server and complete the initialize handshake."""
        try:
            self._proc = subprocess.Popen(
                self._command,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                cwd=str(self._root),
            )
        except (OSError, ValueError) as exc:
            raise LspError(f"failed to spawn {self._command!r}: {exc}") from exc

        self._alive = True
        self._reader = threading.Thread(target=self._read_loop, daemon=True)
        self._reader.start()

        self._request(
            "initialize",
            {
                "processId": os.getpid(),
                "rootUri": self._root.as_uri(),
                "workspaceFolders": [{"uri": self._root.as_uri(), "name": self._root.name}],
                "capabilities": {
                    "textDocument": {
                        "definition": {"linkSupport": True},
                    }
                },
            },
        )
        self._notify("initialized", {})

    def shutdown(self) -> None:
        """Best-effort graceful shutdown; always terminates the process."""
        proc = self._proc
        if proc is None:
            return
        try:
            if self._alive:
                self._request("shutdown", None, timeout=3.0)
                self._notify("exit", {})
        except LspError:
            pass
        finally:
            self._alive = False
            try:
                proc.terminate()
                proc.wait(timeout=3.0)
            except Exception:
                with contextlib.suppress(Exception):
                    proc.kill()
            self._proc = None

    # -- document + queries -----------------------------------------------

    def did_open(self, path: Path, language_id: str, text: str) -> None:
        self._notify(
            "textDocument/didOpen",
            {
                "textDocument": {
                    "uri": path.resolve().as_uri(),
                    "languageId": language_id,
                    "version": 1,
                    "text": text,
                }
            },
        )

    def definition(self, path: Path, line: int, character: int) -> list[dict[str, Any]]:
        """`textDocument/definition` at a 0-based (line, character).

        Normalises the result (which may be a single Location, a list, or
        LocationLinks) to a list of Location-shaped dicts with `uri` and
        `range`.
        """
        resp = self._request(
            "textDocument/definition",
            {
                "textDocument": {"uri": path.resolve().as_uri()},
                "position": {"line": line, "character": character},
            },
        )
        result = resp.get("result")
        return _normalise_locations(result)

    # -- transport ---------------------------------------------------------

    def _request(self, method: str, params: Any, *, timeout: float | None = None) -> dict[str, Any]:
        if not self._alive or self._proc is None:
            raise LspError("client not running")
        with self._lock:
            self._next_id += 1
            rid = self._next_id
            event = threading.Event()
            self._pending[rid] = event
        self._send({"jsonrpc": "2.0", "id": rid, "method": method, "params": params})
        if not event.wait(timeout if timeout is not None else self._timeout):
            with self._lock:
                self._pending.pop(rid, None)
            raise LspError(f"timeout waiting for {method}")
        with self._lock:
            result = self._results.pop(rid, None)
        if result is None:
            raise LspError(f"no result for {method}")
        if "error" in result:
            raise LspError(f"{method} error: {result['error']}")
        return result

    def _notify(self, method: str, params: Any) -> None:
        if not self._alive:
            return
        self._send({"jsonrpc": "2.0", "method": method, "params": params})

    def _send(self, msg: dict[str, Any]) -> None:
        proc = self._proc
        if proc is None or proc.stdin is None:
            raise LspError("client not running")
        data = json.dumps(msg).encode("utf-8")
        header = f"Content-Length: {len(data)}\r\n\r\n".encode("ascii")
        try:
            proc.stdin.write(header + data)
            proc.stdin.flush()
        except (BrokenPipeError, OSError) as exc:
            self._alive = False
            raise LspError(f"send failed: {exc}") from exc

    def _read_loop(self) -> None:
        proc = self._proc
        assert proc is not None and proc.stdout is not None
        stream = proc.stdout
        try:
            while self._alive:
                header = b""
                while b"\r\n\r\n" not in header:
                    ch = stream.read(1)
                    if not ch:
                        raise LspError("server closed stdout")
                    header += ch
                fields = dict(
                    line.split(": ", 1)
                    for line in header.decode("ascii").strip().split("\r\n")
                    if ": " in line
                )
                length = int(fields.get("Content-Length", "0"))
                body = b""
                while len(body) < length:
                    chunk = stream.read(length - len(body))
                    if not chunk:
                        raise LspError("server closed mid-message")
                    body += chunk
                self._dispatch(json.loads(body.decode("utf-8")))
        except Exception:
            # Reader death → wake any waiters so they time out cleanly.
            self._alive = False
            with self._lock:
                for ev in self._pending.values():
                    ev.set()

    def _dispatch(self, msg: dict[str, Any]) -> None:
        mid = msg.get("id")
        if mid is not None and ("result" in msg or "error" in msg):
            # Response to one of our requests.
            with self._lock:
                event = self._pending.pop(mid, None)
                if event is not None:
                    self._results[mid] = msg
                    event.set()
            return
        if mid is not None and "method" in msg:
            # Server→client request; answer with a benign stub so it proceeds.
            self._send({"jsonrpc": "2.0", "id": mid, "result": None})
            return
        # Otherwise a notification (diagnostics, progress, log) — ignore.


def _normalise_locations(result: Any) -> list[dict[str, Any]]:
    if result is None:
        return []
    items = result if isinstance(result, list) else [result]
    out: list[dict[str, Any]] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        if "targetUri" in item:  # LocationLink
            out.append({"uri": item["targetUri"], "range": item.get("targetRange", {})})
        elif "uri" in item:  # Location
            out.append({"uri": item["uri"], "range": item.get("range", {})})
    return out


__all__ = ["LspClient", "LspError"]
