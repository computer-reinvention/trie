from __future__ import annotations

from types import SimpleNamespace
from typing import Any
from unittest.mock import MagicMock

from pydantic_ai import CachePoint

from trie.config import Sync
from trie.models import SectionBody, TrieClient


def _make_client(input_tokens: int = 42) -> tuple[TrieClient, MagicMock]:
    mock_anth = MagicMock()
    mock_anth.messages.count_tokens.return_value = SimpleNamespace(input_tokens=input_tokens)
    client = TrieClient("anthropic/claude-sonnet-4-6", sync_cfg=Sync(max_retries=0))
    client._raw_client = mock_anth
    return client, mock_anth


def test_count_tokens_returns_input_tokens_from_api():
    client, mock_anth = _make_client(input_tokens=42)
    assert client.count_tokens(system_prompt="sys", user_prompt="r") == 42
    mock_anth.messages.count_tokens.assert_called_once()


def test_payload_includes_system_prompt():
    client, mock_anth = _make_client()
    client.count_tokens(system_prompt="be concise", user_prompt="describe foo")
    payload = mock_anth.messages.count_tokens.call_args.kwargs
    assert payload["model"] == "claude-sonnet-4-6"
    assert payload["system"][0]["text"] == "be concise"


def test_payload_omits_system_key_when_empty():
    client, mock_anth = _make_client()
    client.count_tokens(system_prompt="", user_prompt="msg")
    payload = mock_anth.messages.count_tokens.call_args.kwargs
    assert "system" not in payload


def test_payload_carries_model_and_user_message():
    client, mock_anth = _make_client()
    client.count_tokens(system_prompt="sys", user_prompt="hello")
    payload = mock_anth.messages.count_tokens.call_args.kwargs
    assert payload["model"] == "claude-sonnet-4-6"
    assert payload["messages"] == [{"role": "user", "content": "hello"}]


def test_empty_user_prompt_gets_nonwhitespace_placeholder():
    # The Anthropic API rejects empty or whitespace-only user content, but the
    # plan-time cost preview passes an empty prompt to measure only the cached
    # prefix. The client must substitute a non-whitespace placeholder.
    for prompt in ("", "   ", "\n\t"):
        client, mock_anth = _make_client()
        client.count_tokens(system_prompt="sys", user_prompt=prompt)
        payload = mock_anth.messages.count_tokens.call_args.kwargs
        content = payload["messages"][0]["content"]
        assert content.strip(), f"placeholder must be non-whitespace, got {content!r}"


# ---------------------------------------------------------------------------
# Prompt caching wiring. Caching was silently lost in the pydantic-ai
# migration, billing the full prefix on every per-symbol call. These tests
# pin the breakpoints so the regression can't return.
# ---------------------------------------------------------------------------


def _mock_agent(mocker):
    """Patch trie.models.Agent so the async ``run`` returns a canned result and
    records the user input / model_settings it was called with.

    ``run`` is driven via ``loop.run_until_complete`` in production, so the mock
    must be an async function (returning a coroutine), not a plain MagicMock.
    """
    fake_result = SimpleNamespace(
        output=SectionBody(body="## body", role="logic", boundary="internal"),
        usage=SimpleNamespace(
            input_tokens=10,
            output_tokens=5,
            details={"cache_creation_input_tokens": 0, "cache_read_input_tokens": 0},
        ),
    )
    calls: dict[str, Any] = {}

    async def fake_run(user_input, **kwargs):
        calls["args"] = (user_input,)
        calls["kwargs"] = kwargs
        return fake_result

    agent_instance = MagicMock()
    agent_instance.run = fake_run
    agent_cls = mocker.patch("trie.models.Agent", return_value=agent_instance)
    return agent_cls, calls


def test_run_without_cache_prefix_sends_bare_string(mocker):
    _, calls = _mock_agent(mocker)
    client = TrieClient("anthropic/claude-sonnet-4-6", sync_cfg=Sync(max_retries=0))
    client.run(SectionBody, system_prompt="sys", user_prompt="hello")

    user_input = calls["args"][0]
    assert user_input == "hello"


def test_run_with_cache_prefix_inserts_cachepoint(mocker):
    _, calls = _mock_agent(mocker)
    client = TrieClient("anthropic/claude-sonnet-4-6", sync_cfg=Sync(max_retries=0))
    client.run(
        SectionBody,
        system_prompt="sys",
        user_prompt="describe foo",
        cache_prefix="FILE SOURCE",
    )

    user_input = calls["args"][0]
    assert isinstance(user_input, list)
    assert user_input[0] == "FILE SOURCE"
    assert isinstance(user_input[1], CachePoint)
    assert user_input[2] == "describe foo"


def test_run_caches_system_instructions(mocker):
    _, calls = _mock_agent(mocker)
    client = TrieClient("anthropic/claude-sonnet-4-6", sync_cfg=Sync(max_retries=0))
    client.run(SectionBody, system_prompt="sys", user_prompt="hello")

    settings = calls["kwargs"]["model_settings"]
    # AnthropicModelSettings is a TypedDict — a plain dict at runtime.
    assert settings["anthropic_cache_instructions"] is True
    assert settings["max_tokens"] == 1024
