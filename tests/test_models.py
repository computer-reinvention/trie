from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import MagicMock

from trie.config import Sync
from trie.models import TrieClient


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
