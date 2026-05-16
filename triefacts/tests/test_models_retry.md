---
trie_version: 0.1.0
source: tests/test_models_retry.py
file_fingerprint: d8d4752517d6e5bf1496ef2c5d557771d28562d3a747f82dda60e3d14e5b946e
last_synced_at: '2026-05-16T11:23:41Z'
description: Retry-on-rate-limit behaviour of `AnthropicClient`.
defines:
- kind: function
  qualified_name: tests/test_models_retry:_fake_response
  lines: 42-48
- kind: function
  qualified_name: tests/test_models_retry:_rate_limit
  lines: 51-56
- kind: function
  qualified_name: tests/test_models_retry:_overloaded
  lines: 59-64
- kind: function
  qualified_name: tests/test_models_retry:_auth_error
  lines: 67-72
- kind: class
  qualified_name: tests/test_models_retry:_Recorder
  lines: 76-82
- kind: method
  qualified_name: tests/test_models_retry:_Recorder.sleep
  lines: 81-82
- kind: function
  qualified_name: tests/test_models_retry:_frozen_rng
  lines: 85-86
- kind: function
  qualified_name: tests/test_models_retry:test_is_retryable_picks_up_rate_limit_and_5xx_and_timeout
  lines: 92-95
- kind: function
  qualified_name: tests/test_models_retry:test_is_retryable_rejects_auth_and_other_4xx
  lines: 98-100
- kind: function
  qualified_name: tests/test_models_retry:test_retry_after_reads_header_when_present
  lines: 103-105
- kind: function
  qualified_name: tests/test_models_retry:test_retry_after_none_when_header_missing_or_unparseable
  lines: 108-110
- kind: function
  qualified_name: tests/test_models_retry:test_backoff_delay_within_cap
  lines: 113-121
- kind: function
  qualified_name: tests/test_models_retry:test_run_with_retry_honours_retry_after_exactly
  lines: 127-145
- kind: function
  qualified_name: tests/test_models_retry:test_run_with_retry_caps_retry_after
  lines: 148-165
- kind: function
  qualified_name: tests/test_models_retry:test_run_with_retry_uses_backoff_when_no_retry_after
  lines: 168-184
- kind: function
  qualified_name: tests/test_models_retry:test_run_with_retry_backs_off_on_overloaded
  lines: 187-202
- kind: function
  qualified_name: tests/test_models_retry:test_run_with_retry_gives_up_after_max_retries
  lines: 205-217
- kind: function
  qualified_name: tests/test_models_retry:test_run_with_retry_propagates_non_retryable_immediately
  lines: 220-231
- kind: function
  qualified_name: tests/test_models_retry:test_anthropic_client_generate_retries_on_rate_limit
  lines: 237-261
- kind: function
  qualified_name: tests/test_models_retry:test_anthropic_client_count_tokens_retries_on_rate_limit
  lines: 264-277
- kind: function
  qualified_name: tests/test_models_retry:test_anthropic_client_disables_sdk_internal_retries
  lines: 280-293
incoming_refs: 0
outgoing_refs: 25
---
<!-- trie:section symbol=tests/test_models_retry:_fake_response fingerprint=fe8fd6035dcb46c04e29a488aa45d382ac2b3da33fbeaf3f74f28d1db959576b body_fp=7c106ccfb06f3aa86dc8d376b116788eaf61f0a3c3e7333e331a2be3e5d57bbf source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `_fake_response(status: int, *, retry_after: str | None = None) -> httpx.Response`

Build a minimal `httpx.Response` with an optional `retry-after` header for wrapping in SDK exception classes.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models_retry:_rate_limit fingerprint=817d1f499887aef57cd5bba15d5b0e6425ba9d6dfd19bf4589b67b7534d58c2d body_fp=3bc7701315e38919e6d6c987e41d71d8176b41ab481a46999725b2927b6486fd source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `_rate_limit(retry_after: str | None = None) -> RateLimitError`

Construct a `RateLimitError` wrapping a 429 response, optionally with a `retry-after` header.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models_retry:_overloaded fingerprint=623c945b55ddebd9607ef7be5d70b96290bd820023bd75445a18f08a49b5617c body_fp=88cc520f6d91e71f57a6e13385dc1ddadf095ea1364d3c702d09617d414f93e0 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `_overloaded() -> InternalServerError`

Build an `InternalServerError` wrapping a synthetic HTTP 529 response.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models_retry:_auth_error fingerprint=2107cda8409df874e0dc468d7445a1094a779ebe23afebfc673a3e4b0c232a06 body_fp=600e8f292b04687ca1e6f6e7b681bc69542a7fe192cd6528d8676ceaa351aecb source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `_auth_error() -> AuthenticationError`

Build an `AuthenticationError` wrapping a fake 401 response for use in tests.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models_retry:_Recorder fingerprint=826822d20981072b453816aaf9b60f912784c91a83a4ac4e87296e36785412fd body_fp=6aa79e71b56e73b17431bf94e08983b075ef7ed8790db5ee982546f666716948 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `_Recorder`

Record sleep calls without blocking, for asserting retry backoff behaviour.

- `sleeps`: accumulates every `seconds` value passed to `sleep`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models_retry:_Recorder.sleep fingerprint=e45d93e687af0bc59b5bf2e3bd6e8c5c5dbf519386b2560872a90a23f43e8ef9 body_fp=f3b0c09e8f1f8b4490ab25b26d9f42bb041800b2e1696f1fba0fe13cded02bcb source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `_Recorder.sleep(self, seconds: float) -> None`

Record a sleep call by appending `seconds` to `self.sleeps` without actually sleeping.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models_retry:_frozen_rng fingerprint=21a30f0dca12cc5a6c96c27a311a47b71773540767a177151ea8082a02589cbf body_fp=8618a10d949c80cb5d6df2f439d4f3a4ff6acb8fd60f89d4de533b0c173c9e6f source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `_frozen_rng(seed: int = 0) -> random.Random`

Return a seeded `random.Random` instance for deterministic test RNG.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models_retry:test_is_retryable_picks_up_rate_limit_and_5xx_and_timeout fingerprint=57e8cdd19d86cc19a2e20ade35d7eec104a0e39a2510080690d734677e8027dd body_fp=ef41ef1de64b5faba26aed70bd06abe2fdb49d2f6522d455818070b7d6430891 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_is_retryable_picks_up_rate_limit_and_5xx_and_timeout()`

Assert that `_is_retryable` returns `True` for 429, 5xx, and timeout errors.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models_retry:test_is_retryable_rejects_auth_and_other_4xx fingerprint=ad1733d7e18cc28b638ccebae3dbd460280fc5547172d8d6b73456101792f9ea body_fp=5d8b68b16f6a0ec68fb79daf01656be24bc9d47f1d5c30f88bca35d1c9c54c52 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_is_retryable_rejects_auth_and_other_4xx()`

Assert that `_is_retryable` returns `False` for authentication errors and non-API exceptions.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models_retry:test_retry_after_reads_header_when_present fingerprint=8a962d853de085e033e2f8972799ca75d5534b32d48aca2c5962f79497c57210 body_fp=1de4aa9366680f6b779d078b2ec74da065daa527bc2ed0e53b662e993fb984ab source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_retry_after_reads_header_when_present()`

Assert that `_retry_after_seconds` correctly parses numeric `retry-after` header values into floats.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models_retry:test_retry_after_none_when_header_missing_or_unparseable fingerprint=840924acaed456cea64cc1304e5051d92ea6b63661cce9ef689669eb57b0b949 body_fp=b902ec097feba7ce653900ec3340b9b9fbe0b12ed8b5799573562349192008c6 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_retry_after_none_when_header_missing_or_unparseable()`

Assert `_retry_after_seconds` returns `None` when the `retry-after` header is absent or non-numeric.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models_retry:test_backoff_delay_within_cap fingerprint=01fcdc55abf97e3557281070b9ad43c1bcc8b05701af9f4be88ee8b3aef8fef8 body_fp=87d2a33187ce7e3318d24149ee29712654fe365c766c341eb4bbf3650d041662 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_backoff_delay_within_cap()`

Verify that `_backoff_delay` never returns a value outside `[0.0, cap]` even when the attempt index would naively exceed the cap.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_honours_retry_after_exactly fingerprint=14003a3322d64979d8d605ba62373a1f973903240285043c6ef912db080fa0af body_fp=957028d7ccb0571349131c117d83e672c639f50f3ae13949d41ca1513625e549 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_run_with_retry_honours_retry_after_exactly()`

Assert that `_run_with_retry` sleeps exactly the `retry-after` header value, bypassing jitter.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_caps_retry_after fingerprint=da7b5b845dc1ed536c16b052cdbc62c4a53bdcbdffb39690d9129610c14a8852 body_fp=02554da764781689c783c260805b2ddd59809620ae61e45b96d059df439b4130 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_run_with_retry_caps_retry_after()`

Verify that an excessively large `retry-after` header value is clamped to `retry_cap_seconds`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_uses_backoff_when_no_retry_after fingerprint=10f2bc60c406fba9d3c61e64e5ddcb970900091a2089b53dbe6780fa279acdc0 body_fp=5b663c4b36ff8b9e2f1bd644a59a00fc4c1ab0bebe9413fcd6fbe1bc8f3b7f4c source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_run_with_retry_uses_backoff_when_no_retry_after()`

Verify that `_run_with_retry` applies exponential-backoff jitter when a 429 response carries no `retry-after` header.

- Asserts exactly 2 sleeps occur for 2 failures before success.
- Asserts each sleep is within `[0.0, retry_cap_seconds]`.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_backs_off_on_overloaded fingerprint=3cec4f4c645759f9a9756073727e18d70e342d25313642ed06bdaafb168d3516 body_fp=a192d1f941411a70a778c0e159a53b6c4568811ecec796380be015495efc7927 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_run_with_retry_backs_off_on_overloaded()`

Verify that a 529 overloaded error triggers one exponential-backoff sleep within the configured cap.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_gives_up_after_max_retries fingerprint=c4f15661eb0102df7180752f5c2ff0bb83396f79eb0b98358af3ad2d3ae96517 body_fp=9e49e25d13abd62bcc0c50dda1c3ec2237a724742b6ea0d2e96e8156a925e7d1 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_run_with_retry_gives_up_after_max_retries()`

Assert that `_run_with_retry` raises the original exception and sleeps exactly `max_retries` times after exhausting all attempts.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_propagates_non_retryable_immediately fingerprint=9503d02df17aa8a31ae1080d7f49b5535de0952085b6062231401a67680e32cb body_fp=e192d5f01a773f8bd63260ae09f0182dd65a1b876f56898a2e633cf42719d427 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_run_with_retry_propagates_non_retryable_immediately()`

Verify that non-retryable errors (e.g. `AuthenticationError`) raise immediately with zero sleep calls.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models_retry:test_anthropic_client_generate_retries_on_rate_limit fingerprint=170f404f9b7f5ef0febe3180973e3405eda6abf43caff56cf1c7cfdc9ebd2969 body_fp=487f37eb5f2ed2f783a18be1366be9504f541389e9f774e40d45bfb6d1659f32 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_anthropic_client_generate_retries_on_rate_limit()`

Verify that `AnthropicClient.generate` retries a 429 response and returns the successful second call's text.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models_retry:test_anthropic_client_count_tokens_retries_on_rate_limit fingerprint=81431baaa0dab19183f56854549eafcbe79e44a7e52bb3f1c56e96af035186e7 body_fp=1548ed4c71ccf707c9e5b0fa809f123ffca657bd080c6d54641f53eb64a42ae5 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_anthropic_client_count_tokens_retries_on_rate_limit()`

Verify that `AnthropicClient.count_tokens` retries on a 429 and returns the token count from the successful second call.
<!-- trie:end -->

<!-- trie:section symbol=tests/test_models_retry:test_anthropic_client_disables_sdk_internal_retries fingerprint=e88632a86840b5880310a262d24f7ff1d9d236bb62c66c744f67f157450c6312 body_fp=fbd6a4b5335c901c2ba4ad2248b324eb935a4290693b7595ddcc0b65f87446f4 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_anthropic_client_disables_sdk_internal_retries(monkeypatch: pytest.MonkeyPatch)`

Assert that `AnthropicClient` passes `max_retries=0` to the Anthropic SDK constructor when no explicit client is provided.
<!-- trie:end -->