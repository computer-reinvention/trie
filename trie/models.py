from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from anthropic import Anthropic

from trie import telemetry


@dataclass(frozen=True)
class GenerationRequest:
    """A single LLM call. `cached_context` is intended to be reused across calls within
    the same file via Anthropic prompt caching; `request` is the small per-symbol delta."""

    system_prompt: str
    cached_context: str
    request: str
    max_tokens: int = 1024


@dataclass(frozen=True)
class GenerationResponse:
    text: str
    input_tokens: int
    output_tokens: int
    cache_creation_input_tokens: int
    cache_read_input_tokens: int


class ModelClient(Protocol):
    model_id: str

    def generate(self, req: GenerationRequest) -> GenerationResponse: ...

    def count_tokens(self, req: GenerationRequest) -> int: ...


class AnthropicClient:
    def __init__(self, model_id: str, *, client: Anthropic | None = None) -> None:
        self.model_id = model_id
        self._client = client or Anthropic()

    def _payload(self, req: GenerationRequest) -> dict:
        content: list[dict] = [
            {
                "type": "text",
                "text": req.cached_context,
                "cache_control": {"type": "ephemeral"},
            },
        ]
        # Anthropic rejects empty text content blocks. `build_plan` calls count_tokens
        # with `request=""` to get just the cached-prefix size, so skip the block when
        # it's empty rather than sending an invalid payload.
        if req.request:
            content.append({"type": "text", "text": req.request})
        return {
            "model": self.model_id,
            "system": [
                {
                    "type": "text",
                    "text": req.system_prompt,
                    "cache_control": {"type": "ephemeral"},
                },
            ],
            "messages": [{"role": "user", "content": content}],
        }

    def generate(self, req: GenerationRequest) -> GenerationResponse:
        with telemetry.timed("model_call", model=self.model_id, kind="generate") as tele:
            resp = self._client.messages.create(max_tokens=req.max_tokens, **self._payload(req))
            text = "".join(block.text for block in resp.content if block.type == "text")
            usage = resp.usage
            tele["input_tokens"] = usage.input_tokens
            tele["output_tokens"] = usage.output_tokens
            tele["cache_creation_input_tokens"] = (
                getattr(usage, "cache_creation_input_tokens", 0) or 0
            )
            tele["cache_read_input_tokens"] = getattr(usage, "cache_read_input_tokens", 0) or 0
            return GenerationResponse(
                text=text,
                input_tokens=usage.input_tokens,
                output_tokens=usage.output_tokens,
                cache_creation_input_tokens=getattr(usage, "cache_creation_input_tokens", 0) or 0,
                cache_read_input_tokens=getattr(usage, "cache_read_input_tokens", 0) or 0,
            )

    def count_tokens(self, req: GenerationRequest) -> int:
        """Return the number of input tokens for `req` per the Anthropic count_tokens API.

        Free, but rate-limited separately from message creation. Counts the same payload
        the generator would actually send (system + cached context + per-symbol request),
        so the result reflects real prompt size rather than a char-count heuristic.
        """
        with telemetry.timed("model_call", model=self.model_id, kind="count_tokens") as tele:
            resp = self._client.messages.count_tokens(**self._payload(req))
            tele["input_tokens"] = resp.input_tokens
            return resp.input_tokens


def make_client(model_id: str) -> ModelClient:
    """Construct a model client from a "provider/model" id string.

    v0.1 only supports the `anthropic/` provider; other providers (deepseek, qwen via
    OpenAI-compatible base URLs) are deferred.
    """
    if "/" not in model_id:
        raise ValueError(f"model_id must be of the form 'provider/model', got {model_id!r}")
    provider, model_name = model_id.split("/", 1)
    if provider == "anthropic":
        return AnthropicClient(model_name)
    raise NotImplementedError(
        f"provider {provider!r} not implemented in v0.1. "
        "Use 'anthropic/<model>' or extend trie.models.make_client."
    )
