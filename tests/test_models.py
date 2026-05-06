from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import MagicMock

from trie.models import AnthropicClient, GenerationRequest


def _make_client(input_tokens: int = 42) -> tuple[AnthropicClient, MagicMock]:
    mock_anth = MagicMock()
    mock_anth.messages.count_tokens.return_value = SimpleNamespace(input_tokens=input_tokens)
    return AnthropicClient("claude-sonnet-4-6", client=mock_anth), mock_anth


def test_count_tokens_returns_input_tokens_from_api():
    client, mock_anth = _make_client(input_tokens=42)
    req = GenerationRequest(system_prompt="sys", cached_context="ctx", request="r")
    assert client.count_tokens(req) == 42
    mock_anth.messages.count_tokens.assert_called_once()


def test_payload_includes_request_block_when_non_empty():
    client, mock_anth = _make_client()
    req = GenerationRequest(system_prompt="sys", cached_context="ctx", request="describe foo")
    client.count_tokens(req)
    payload = mock_anth.messages.count_tokens.call_args.kwargs
    content = payload["messages"][0]["content"]
    assert len(content) == 2
    assert content[0]["text"] == "ctx"
    assert content[1]["text"] == "describe foo"


def test_payload_skips_empty_request_block():
    """build_plan calls count_tokens with request="" to size just the cached prefix.
    Anthropic rejects empty text blocks, so the payload must drop the empty block."""
    client, mock_anth = _make_client()
    req = GenerationRequest(system_prompt="sys", cached_context="ctx", request="")
    client.count_tokens(req)
    payload = mock_anth.messages.count_tokens.call_args.kwargs
    content = payload["messages"][0]["content"]
    assert len(content) == 1
    assert content[0]["text"] == "ctx"
    # cache_control is preserved on the cached_context block
    assert content[0]["cache_control"] == {"type": "ephemeral"}


def test_payload_carries_model_and_system_prompt():
    client, mock_anth = _make_client()
    req = GenerationRequest(system_prompt="be concise", cached_context="ctx", request="r")
    client.count_tokens(req)
    payload = mock_anth.messages.count_tokens.call_args.kwargs
    assert payload["model"] == "claude-sonnet-4-6"
    assert payload["system"][0]["text"] == "be concise"
    assert payload["system"][0]["cache_control"] == {"type": "ephemeral"}
