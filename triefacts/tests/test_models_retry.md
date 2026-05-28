---
trie_version: 0.1.5
source: tests/test_models_retry.py
file_fingerprint: d8d4752517d6e5bf1496ef2c5d557771d28562d3a747f82dda60e3d14e5b946e
last_synced_at: '2026-05-28T01:40:07Z'
description: Retry-on-rate-limit behaviour of `AnthropicClient`.
defines:
- kind: module
  qualified_name: tests/test_models_retry:__module__
  lines: 1-294
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
<!-- trie:section symbol=tests/test_models_retry:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=8a555c6656c6d53a59b2550c0fe3beab7650e1544511034ccc2ff58cb3a3bcde source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `tests/test_models_retry`

Test suite for retry-on-rate-limit behaviour of `AnthropicClient`.

- 429 + `retry-after` header → exact wait, capped at configured ceiling
- 429 without header, 5xx, timeouts → exponential backoff with jitter
- Non-retryable 4xx → propagates immediately, no sleep
- Exhausted `max_retries` → original exception re-raised
- Covers both `messages.create` and `messages.count_tokens` paths
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_fake_response fingerprint=fe8fd6035dcb46c04e29a488aa45d382ac2b3da33fbeaf3f74f28d1db959576b body_fp=2523a2315cbb9ac135368eb27be60100729a1bacf210c805b0bf6ea46f759bd9 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `_fake_response(status: int, *, retry_after: str | None = None) -> httpx.Response`

Build a minimal `httpx.Response` suitable for wrapping in Anthropic SDK exception classes.

- `retry_after`: if provided, sets the `retry-after` response header.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_rate_limit fingerprint=817d1f499887aef57cd5bba15d5b0e6425ba9d6dfd19bf4589b67b7534d58c2d body_fp=814995b2aa4064aa46e2a27a377f6c7765b4477515144fe3cb8c2b48bef9b8b4 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `_rate_limit(retry_after: str | None = None) -> RateLimitError`

Build a `RateLimitError` wrapping a 429 response with an optional `retry-after` header.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_overloaded fingerprint=623c945b55ddebd9607ef7be5d70b96290bd820023bd75445a18f08a49b5617c body_fp=ac90c370c2aa37bf3dff4aa093e9d62580e672023ff49a7831ac84e5f351b1cb source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `_overloaded() -> InternalServerError`

Build an `InternalServerError` wrapping a 529 response for use in retry tests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_auth_error fingerprint=2107cda8409df874e0dc468d7445a1094a779ebe23afebfc673a3e4b0c232a06 body_fp=efa96dc6da908913edd058b86620b1e03c690ab38e3781af6675f115a1e00f53 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `_auth_error() -> AuthenticationError`

Build an `AuthenticationError` wrapping a 401 response for use in tests.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_Recorder fingerprint=826822d20981072b453816aaf9b60f912784c91a83a4ac4e87296e36785412fd body_fp=414eea1af2f0494938dace5c68ab0f6f542aaa1ccd36a2456fe62d02f03c16d9 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `_Recorder`

Test double that records `sleep` calls without blocking.

- `sleeps`: accumulates every delay passed to `sleep`, in order.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_Recorder.sleep fingerprint=e45d93e687af0bc59b5bf2e3bd6e8c5c5dbf519386b2560872a90a23f43e8ef9 body_fp=541b1b44575be7c39d907d3d75bbe22071651c611cd89726cee3a7beb6b9c9e6 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `_Recorder.sleep(self, seconds: float) -> None`

Record a sleep call on `_Recorder` by appending `seconds` to `self.sleeps` without blocking.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_frozen_rng fingerprint=21a30f0dca12cc5a6c96c27a311a47b71773540767a177151ea8082a02589cbf body_fp=6abdb3445796e2b7fc2af723129d070d92887fd0e07a36cd8fe7b044e07c0b96 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `_frozen_rng(seed: int = 0) -> random.Random`

Return a seeded `random.Random` instance for deterministic test runs.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_is_retryable_picks_up_rate_limit_and_5xx_and_timeout fingerprint=57e8cdd19d86cc19a2e20ade35d7eec104a0e39a2510080690d734677e8027dd body_fp=fafdce734a87e9282aeaf175116536c02bdf231817d741c52191c36fa68d127f source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_is_retryable_picks_up_rate_limit_and_5xx_and_timeout()`

Assert that `_is_retryable` returns `True` for `RateLimitError`, `InternalServerError`, and `APITimeoutError`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_is_retryable_rejects_auth_and_other_4xx fingerprint=ad1733d7e18cc28b638ccebae3dbd460280fc5547172d8d6b73456101792f9ea body_fp=523a617f44ae901476975a92f6a24d231a9ee78294d2cc369cd59603deb2f25f source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_is_retryable_rejects_auth_and_other_4xx()`

Assert that `_is_retryable` returns `False` for auth errors and non-API exceptions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_retry_after_reads_header_when_present fingerprint=8a962d853de085e033e2f8972799ca75d5534b32d48aca2c5962f79497c57210 body_fp=e8a22e1bbb1dddae4cd3d4f6aee7a7f8b66c849140d69e811f7e435d9006e849 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_retry_after_reads_header_when_present()`

Assert `_retry_after_seconds` parses integer and fractional `retry-after` header values correctly.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_retry_after_none_when_header_missing_or_unparseable fingerprint=840924acaed456cea64cc1304e5051d92ea6b63661cce9ef689669eb57b0b949 body_fp=b902ec097feba7ce653900ec3340b9b9fbe0b12ed8b5799573562349192008c6 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_retry_after_none_when_header_missing_or_unparseable()`

Assert `_retry_after_seconds` returns `None` when the `retry-after` header is absent or non-numeric.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_backoff_delay_within_cap fingerprint=01fcdc55abf97e3557281070b9ad43c1bcc8b05701af9f4be88ee8b3aef8fef8 body_fp=b3fab47d6546f0b9e3c892f92a6a11b4c2f714a13c19558e6b913f67cf2d63fd source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_backoff_delay_within_cap()`

Assert that `_backoff_delay` always returns a value in `[0.0, cap]` even when the attempt number would naively overflow the cap.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_honours_retry_after_exactly fingerprint=14003a3322d64979d8d605ba62373a1f973903240285043c6ef912db080fa0af body_fp=957028d7ccb0571349131c117d83e672c639f50f3ae13949d41ca1513625e549 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_run_with_retry_honours_retry_after_exactly()`

Assert that `_run_with_retry` sleeps exactly the `retry-after` header value, bypassing jitter.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_caps_retry_after fingerprint=da7b5b845dc1ed536c16b052cdbc62c4a53bdcbdffb39690d9129610c14a8852 body_fp=83d4112ae49cc7cacd7a55b2ec7bdbaeb7e1c5a2473c169a9f1c57e2c5b71da9 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_run_with_retry_caps_retry_after()`

Assert that `_run_with_retry` clamps an excessively large `retry-after` header value to `retry_cap_seconds`.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_uses_backoff_when_no_retry_after fingerprint=10f2bc60c406fba9d3c61e64e5ddcb970900091a2089b53dbe6780fa279acdc0 body_fp=b2ed9cac12e4d4b174b38e930243c046872ab4f21e3c9087e7b14dfca772e54a source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_run_with_retry_uses_backoff_when_no_retry_after()`

Verify `_run_with_retry` uses capped exponential backoff when no `retry-after` header is present.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_backs_off_on_overloaded fingerprint=3cec4f4c645759f9a9756073727e18d70e342d25313642ed06bdaafb168d3516 body_fp=4fc3a12147e83501ddbd882af31693dcf7a174d25720853559ea23b85ed0f52e source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_run_with_retry_backs_off_on_overloaded()`

Assert that `_run_with_retry` applies exponential backoff when a 529 overloaded error is raised.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_gives_up_after_max_retries fingerprint=c4f15661eb0102df7180752f5c2ff0bb83396f79eb0b98358af3ad2d3ae96517 body_fp=6d8a90c8f6eb9e47c9ccc63bade5fb3b60a0d999872a8c0d0ca20108610177b6 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_run_with_retry_gives_up_after_max_retries()`

Assert that `_run_with_retry` re-raises `RateLimitError` and sleeps exactly `max_retries` times after exhausting all attempts.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_propagates_non_retryable_immediately fingerprint=9503d02df17aa8a31ae1080d7f49b5535de0952085b6062231401a67680e32cb body_fp=dde140d8c5ce8c649b4e1b8bc829e45d633eb545f7e53e935f61b0767fc44bc2 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_run_with_retry_propagates_non_retryable_immediately()`

Assert that `_run_with_retry` re-raises non-retryable errors instantly without any sleep.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_anthropic_client_generate_retries_on_rate_limit fingerprint=170f404f9b7f5ef0febe3180973e3405eda6abf43caff56cf1c7cfdc9ebd2969 body_fp=9a1d238c2ab0258398ed484e930fc6a3e02f9a7ab54a68c823b9f6ed19ed0ff2 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_anthropic_client_generate_retries_on_rate_limit()`

Verify that `AnthropicClient.generate` retries the SDK call after a 429 and returns the successful second response.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_anthropic_client_count_tokens_retries_on_rate_limit fingerprint=81431baaa0dab19183f56854549eafcbe79e44a7e52bb3f1c56e96af035186e7 body_fp=3641549e56b7759f64c9bceedd94e34c4d81a6c265d84c56f469e28d47f75f09 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_anthropic_client_count_tokens_retries_on_rate_limit()`

Assert that `AnthropicClient.count_tokens` retries on a 429 rate-limit error before returning the token count.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_anthropic_client_disables_sdk_internal_retries fingerprint=e88632a86840b5880310a262d24f7ff1d9d236bb62c66c744f67f157450c6312 body_fp=3c83c14048bf96f63703563761ae383b61af84314cc1032a52705208459d2913 source_ref=f265d955421abbef1f0ef04061dfebf390adf4eb -->
## `test_anthropic_client_disables_sdk_internal_retries(monkeypatch: pytest.MonkeyPatch)`

Assert that `AnthropicClient` passes `max_retries=0` to the Anthropic SDK constructor when no explicit `client=` is provided.
<!-- trie:end -->