"""Tests for AGM attention contracts, event store, sync-time fold, and typed edges."""

from __future__ import annotations

import math
from pathlib import Path

import pytest

from trie import attention_store
from trie.attention import (
    EDGE_WEIGHTS,
    EVENT_WEIGHTS,
    HISTORICAL_LAMBDA,
    AttentionEvent,
    classify_synthetic,
    classify_tool,
    display_mass,
    edge_weight,
    is_synthetic_qname,
    live_lambda,
    synthetic_qname,
)
from trie.parse.references import extract_file_data
from trie.sync.attention_fold import fold_historical_mass
from trie.sync.writer import TriefactFile, format_hist_mass, parse_hist_mass

# --- contracts -------------------------------------------------------------


def test_event_weights_canonical():
    assert EVENT_WEIGHTS == {"grep": 10, "read": 40, "trace": 80, "write": 80}


@pytest.mark.parametrize(
    "tool,expected",
    [
        ("trie_read", "read"),
        ("read_source", "read"),
        ("explain_symbol", "read"),
        ("trace", "trace"),
        ("trace_flow", "trace"),
        ("grep", "grep"),
        ("grep_str_all", "grep"),
        ("find_files", "grep"),
        ("patch", "write"),
        ("write_file", "write"),
        ("create_symbol", "write"),
        ("summary", None),
        ("activity", None),
        ("unknown_tool_xyz", None),
    ],
)
def test_classify_tool(tool, expected):
    assert classify_tool(tool) == expected


def test_classify_tool_strips_prefix():
    assert classify_tool("trie_grep") == classify_tool("grep")


def test_classify_synthetic():
    assert classify_synthetic("trie_read_source") == "Filesystem"
    assert classify_synthetic("write_file") == "Filesystem"
    assert classify_synthetic("trie_read") is None


def test_edge_weights_and_fallback():
    assert EDGE_WEIGHTS["calls"] == 1.0
    assert EDGE_WEIGHTS["contains"] == 0.2
    assert edge_weight("inherits") == 0.9
    # unknown kind falls back to calls
    assert edge_weight("depends_on") == EDGE_WEIGHTS["calls"]


def test_display_mass_log_compression():
    assert display_mass(0.0) == 0.0
    assert display_mass(-5.0) == 0.0  # clamps negatives
    assert display_mass(math.e - 1) == pytest.approx(1.0)
    # monotonic but compressing
    assert display_mass(1000) < 1000


def test_live_lambda_matches_halflife():
    # after one half-life the decay factor is 0.5
    lam = live_lambda("grep")
    assert math.exp(-lam * 30.0) == pytest.approx(0.5)


def test_synthetic_qname_roundtrip():
    q = synthetic_qname("Bash")
    assert q == "agm:synthetic/Bash"
    assert is_synthetic_qname(q)
    assert not is_synthetic_qname("trie/x:y")


def test_attention_event_make_fills_weight():
    e = AttentionEvent.make(ts=1.0, event_type="trace", target="a:b", investigation_id="inv")
    assert e.weight == 80
    assert e.investigation_id == "inv"


# --- typed edges -----------------------------------------------------------


def test_typed_edges(tmp_path: Path):
    src = tmp_path / "m.py"
    src.write_text(
        "from abc import ABC\n"
        "\n"
        "def helper(x):\n"
        "    return x + 1\n"
        "\n"
        "class Base:\n"
        "    pass\n"
        "\n"
        "class Worker(Base, ABC):\n"
        "    def run(self):\n"
        "        return helper(1)\n"
    )
    fd = extract_file_data(src, source_root=tmp_path)
    kinds = {(r.src_qname, r.target_qname): r.kind for r in fd.references}
    assert kinds[("m:Worker", "m:Base")] == "inherits"
    assert kinds[("m:Worker", "abc:ABC")] == "implements"
    assert kinds[("m:Worker", "m:Worker.run")] == "contains"
    assert kinds[("m:Worker.run", "m:helper")] == "calls"


def test_call_vs_reference_kind(tmp_path: Path):
    src = tmp_path / "m.py"
    src.write_text(
        "def target():\n    return 1\n\n"
        "def caller():\n    return target()\n\n"
        "def referencer():\n    f = target\n    return f\n"
    )
    fd = extract_file_data(src, source_root=tmp_path)
    kinds = {(r.src_qname, r.target_qname): r.kind for r in fd.references}
    assert kinds[("m:caller", "m:target")] == "calls"
    assert kinds[("m:referencer", "m:target")] == "references"


# --- event store -----------------------------------------------------------


def test_store_record_and_read(tmp_path: Path):
    attention_store.record_event(
        tmp_path, event_type="read", target="a:b", investigation_id="inv1", ts=100.0
    )
    attention_store.record_event(
        tmp_path, event_type="trace", target="a:b", investigation_id="inv2", ts=200.0
    )
    events = attention_store.read_events(tmp_path)
    assert len(events) == 2
    assert {e.event_type for e in events} == {"read", "trace"}


def test_store_coalesces_within_window(tmp_path: Path):
    attention_store.record_event(
        tmp_path, event_type="read", target="a:b", investigation_id="inv1", ts=100.0
    )
    attention_store.record_event(
        tmp_path, event_type="read", target="a:b", investigation_id="inv1", ts=102.0
    )
    events = attention_store.read_events(tmp_path)
    assert len(events) == 1
    assert events[0].weight == EVENT_WEIGHTS["read"] * 2


def test_store_distinct_investigations(tmp_path: Path):
    for inv, ts in [("inv1", 100.0), ("inv2", 200.0), ("inv1", 300.0)]:
        attention_store.record_event(
            tmp_path, event_type="read", target="a:b", investigation_id=inv, ts=ts
        )
    assert attention_store.investigations_touching_symbol_since(tmp_path, "a:b") == {
        "inv1",
        "inv2",
    }
    assert attention_store.investigations_touching_symbol_since(tmp_path, "a:b", since=250.0) == {
        "inv1"
    }


def test_store_fold_watermark(tmp_path: Path):
    assert attention_store.get_last_fold_ts(tmp_path) == 0.0
    attention_store.set_last_fold_ts(tmp_path, 1234.0)
    assert attention_store.get_last_fold_ts(tmp_path) == 1234.0


def test_store_missing_db_is_empty(tmp_path: Path):
    # reading before any write must not raise
    assert attention_store.read_events(tmp_path / "nope") == []
    assert attention_store.investigations_touching_symbol_since(tmp_path / "nope", "x") == set()


# --- sentinel round-trip ---------------------------------------------------


def test_hist_mass_parse_format():
    assert parse_hist_mass("5.5@123") == (5.5, 123.0)
    assert parse_hist_mass(None) == (0.0, 0.0)
    assert parse_hist_mass("garbage") == (0.0, 0.0)
    assert format_hist_mass(2.34, 1739000000.7) == "2.3@1739000000"


def test_legacy_sentinel_no_hist_mass():
    legacy = "<!-- trie:section symbol=a:b fingerprint=ff body_fp=bb role=util -->\nBody.\n<!-- trie:end -->"
    tf = TriefactFile.parse(legacy)
    sec = tf.get_section("a:b")
    assert sec.historical_mass == 0.0
    # zero mass is not rendered (legacy stays clean)
    assert "hist_mass" not in tf.render()


def test_hist_mass_roundtrip_preserves_role():
    legacy = "<!-- trie:section symbol=a:b fingerprint=ff body_fp=bb role=util -->\nBody.\n<!-- trie:end -->"
    tf = TriefactFile.parse(legacy)
    tf.set_section_historical_mass("a:b", 3.0, 1739000000.0)
    out = tf.render()
    assert "hist_mass=3.0@1739000000" in out
    again = TriefactFile.parse(out)
    sec = again.get_section("a:b")
    assert sec.historical_mass == 3.0
    assert sec.role == "util"


def test_upsert_preserves_existing_hist_mass():
    legacy = "<!-- trie:section symbol=a:b fingerprint=ff body_fp=bb -->\nBody.\n<!-- trie:end -->"
    tf = TriefactFile.parse(legacy)
    tf.set_section_historical_mass("a:b", 5.0, 1739000000.0)
    # regenerating prose must not wipe mass
    tf.upsert_section(qualified_name="a:b", fingerprint="ff2", body="New body.")
    sec = tf.get_section("a:b")
    assert sec.historical_mass == 5.0


# --- fold ------------------------------------------------------------------


def test_fold_accrues_recurrence(tmp_path: Path):
    attention_store.record_event(
        tmp_path, event_type="read", target="a:b", investigation_id="inv1", ts=1000.0
    )
    attention_store.record_event(
        tmp_path, event_type="trace", target="a:b", investigation_id="inv2", ts=1001.0
    )
    attention_store.record_event(
        tmp_path, event_type="grep", target="c:d", investigation_id="inv1", ts=1002.0
    )
    tf = TriefactFile.parse(
        "<!-- trie:section symbol=a:b fingerprint=f1 body_fp=b1 -->\nA.\n<!-- trie:end -->\n\n"
        "<!-- trie:section symbol=c:d fingerprint=f2 body_fp=b2 -->\nC.\n<!-- trie:end -->"
    )
    changed = fold_historical_mass(tf, project_root=tmp_path, now=1010.0, since=0.0)
    assert changed == 2
    assert tf.get_section("a:b").historical_mass == 2.0  # two distinct investigations
    assert tf.get_section("c:d").historical_mass == 1.0  # one


def test_fold_decays_existing(tmp_path: Path):
    tf = TriefactFile.parse(
        "<!-- trie:section symbol=a:b fingerprint=f1 body_fp=b1 hist_mass=2.0@1000 -->\nA.\n<!-- trie:end -->"
    )
    # no new events; 7 days later -> pure decay
    seven_days = 7 * 24 * 3600
    fold_historical_mass(tf, project_root=tmp_path, now=1000.0 + seven_days, since=1000.0)
    expected = 2.0 * math.exp(-HISTORICAL_LAMBDA * seven_days)
    assert tf.get_section("a:b").historical_mass == pytest.approx(expected, rel=1e-6)
