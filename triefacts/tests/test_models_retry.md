---
trie_version: 0.1.9
source: tests/test_models_retry.py
file_fingerprint: 9c2ce050365972595913b15d85be1800d591f8e3e81c2f9f0916d296aa819c39
last_synced_at: '2026-07-25T01:56:19Z'
description: Retry-on-rate-limit behaviour of `AnthropicClient`.
defines:
- kind: module
  qualified_name: tests/test_models_retry:__module__
  lines: 1-378
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
  qualified_name: tests/test_models_retry:test_is_retryable_picks_up_connection_errors
  lines: 98-102
- kind: function
  qualified_name: tests/test_models_retry:test_is_retryable_rejects_auth_and_other_4xx
  lines: 105-107
- kind: function
  qualified_name: tests/test_models_retry:test_is_retryable_unwraps_pydantic_ai_model_api_error
  lines: 110-128
- kind: function
  qualified_name: tests/test_models_retry:test_per_thread_models_are_distinct_and_reused
  lines: 131-160
- kind: function
  qualified_name: tests/test_models_retry:test_retry_after_reads_header_when_present
  lines: 163-165
- kind: function
  qualified_name: tests/test_models_retry:test_retry_after_none_when_header_missing_or_unparseable
  lines: 168-170
- kind: function
  qualified_name: tests/test_models_retry:test_backoff_delay_within_cap
  lines: 173-181
- kind: function
  qualified_name: tests/test_models_retry:test_run_with_retry_honours_retry_after_exactly
  lines: 187-205
- kind: function
  qualified_name: tests/test_models_retry:test_run_with_retry_caps_retry_after
  lines: 208-225
- kind: function
  qualified_name: tests/test_models_retry:test_run_with_retry_uses_backoff_when_no_retry_after
  lines: 228-244
- kind: function
  qualified_name: tests/test_models_retry:test_run_with_retry_backs_off_on_overloaded
  lines: 247-262
- kind: function
  qualified_name: tests/test_models_retry:test_run_with_retry_gives_up_after_max_retries
  lines: 265-277
- kind: function
  qualified_name: tests/test_models_retry:test_run_with_retry_propagates_non_retryable_immediately
  lines: 280-291
- kind: function
  qualified_name: tests/test_models_retry:test_count_tokens_retries_on_rate_limit
  lines: 297-309
- kind: function
  qualified_name: tests/test_models_retry:test_trie_client_disables_sdk_internal_retries
  lines: 312-325
- kind: function
  qualified_name: tests/test_models_retry:test_retry_total_seconds_bounds_the_loop
  lines: 328-355
- kind: function
  qualified_name: tests/test_models_retry:test_retry_total_seconds_zero_is_unbounded
  lines: 358-377
incoming_refs: 0
outgoing_refs: 28
---
<!-- trie:section symbol=tests/test_models_retry:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=6230e0b6dac96c666f4c643a238e8932016fce96586b9091c4f78ad67994b7c1 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 role=test-infrastructure -->
Tests retry behavior of `AnthropicClient` against rate limits, server errors, timeouts, and non-retryable exceptions.

- Tests proper handling of `retry-after` headers vs exponential backoff
- Verifies retry loop applies to both `messages.create` and `messages.count_tokens`
- Ensures SDK internal retries are disabled to avoid double-retry
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_fake_response fingerprint=fe8fd6035dcb46c04e29a488aa45d382ac2b3da33fbeaf3f74f28d1db959576b body_fp=cbdf0894098178299b192f1bfc719ee7fe02527b5cce12feec20c8dad57f93f4 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 role=test-infrastructure -->
Builds an httpx.Response object with specified status and optional retry-after header for testing SDK exception handling.

- `retry_after`: When provided, sets the "retry-after" header value
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_rate_limit fingerprint=817d1f499887aef57cd5bba15d5b0e6425ba9d6dfd19bf4589b67b7534d58c2d body_fp=ca4900892d76cda781caae4beeecaa224d32f39be200421b165383700d6abab3 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 role=test-infrastructure -->
Creates a RateLimitError exception with 429 status and optional retry-after header for testing.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_overloaded fingerprint=623c945b55ddebd9607ef7be5d70b96290bd820023bd75445a18f08a49b5617c body_fp=43304d5633c4d7d5119d12ff84b381c7ba1dcf1acc2644228c66939f0a8dbb0b source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 role=test-infrastructure -->
Creates an InternalServerError representing a 529 overloaded server response for testing retry logic.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_auth_error fingerprint=2107cda8409df874e0dc468d7445a1094a779ebe23afebfc673a3e4b0c232a06 body_fp=4043bc5155fa351f85e24890edda86946efabb5488aab9c2d89170baaecfc482 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 role=test-infrastructure -->
Creates an AuthenticationError with a 401 response for testing non-retryable error handling.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_Recorder fingerprint=826822d20981072b453816aaf9b60f912784c91a83a4ac4e87296e36785412fd body_fp=b13516a931c13fbc73b422a1c7d12c4f92733da5f6b2b04a295767d42c3977e5 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 role=test-infrastructure -->
Records sleep durations during retry testing without actually blocking execution.

- `sleeps`: List of sleep durations passed to the `sleep` method for verification
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_Recorder.sleep fingerprint=e45d93e687af0bc59b5bf2e3bd6e8c5c5dbf519386b2560872a90a23f43e8ef9 body_fp=7cc2be47830da0c85d7b1d49910917448871f9dd33b29fd87fb7d0d805abf619 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 role=test-infrastructure -->
Records the sleep duration in `_Recorder.sleeps` list without actually blocking execution.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_frozen_rng fingerprint=21a30f0dca12cc5a6c96c27a311a47b71773540767a177151ea8082a02589cbf body_fp=ff28d8f00435d123e2bd007ad86c835f319096104261522e1bf057cdbc46bf1d source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 role=test-infrastructure -->
Creates a seeded Random instance for deterministic test outcomes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_is_retryable_picks_up_rate_limit_and_5xx_and_timeout fingerprint=57e8cdd19d86cc19a2e20ade35d7eec104a0e39a2510080690d734677e8027dd body_fp=6bd58bc9505959ef161d8b4c54c24fa41f5423bd0ba4f31b3eef9236e2d27f6e source_ref=b6d9ec2215ba7e76948b5257834bfb9312fd1910 role=test -->
Verifies that `_is_retryable` returns True for rate limit, 5xx server errors, and timeout exceptions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_is_retryable_picks_up_connection_errors fingerprint=b84afa39a66ae629bd3f4b4a9ca4b6101e84fe979bae7325a8e82096f1f7affd body_fp=a8b02be901737f72e8aa8515b662e1ccd6fc5ab08b79596a4bd5eb7275bdae7f source_ref=b6d9ec2215ba7e76948b5257834bfb9312fd1910 role=test -->
Tests that `_is_retryable` correctly identifies `APIConnectionError` as retryable.

- Creates an `APIConnectionError` representing transient network failures like DNS lookup or connection refused
- Verifies the error is classified as retryable to prevent sync crashes
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_is_retryable_rejects_auth_and_other_4xx fingerprint=ad1733d7e18cc28b638ccebae3dbd460280fc5547172d8d6b73456101792f9ea body_fp=5d8e0ae7d24399fcea49939c98ddeb21cf3558f66278b976a23349cf6270c1ec source_ref=b6d9ec2215ba7e76948b5257834bfb9312fd1910 role=test -->
Verifies `_is_retryable` returns False for authentication errors and non-API exceptions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_is_retryable_unwraps_pydantic_ai_model_api_error fingerprint=3d88bbfec2cfe3c0211f9ac1e50594a8126e088e50452d10f07d0950f39a9bcc body_fp=9c8baab32cc5644582b792f5c2d6dc53e1c0ba77bbf9f87eade043a979f1e478 source_ref=b6d9ec2215ba7e76948b5257834bfb9312fd1910 role=test -->
Tests that `_is_retryable` correctly handles pydantic-ai's ModelAPIError wrappers around retryable exceptions.

- Tests message-based matching for connection errors
- Tests __cause__ chain unwrapping for wrapped anthropic exceptions
- Verifies non-retryable errors remain non-retryable when wrapped
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_per_thread_models_are_distinct_and_reused fingerprint=8d223b1bbd94023b408c389bf435b8f82b4f09420d56812fd38db9b00df4e288 body_fp=e757240910fa9b0821f116037fc3052396546a73b41f92a73a89c33a49a3cfb0 source_ref=b6d9ec2215ba7e76948b5257834bfb9312fd1910 role=test -->
Tests that TrieClient creates distinct models per thread but reuses within threads.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_retry_after_reads_header_when_present fingerprint=8a962d853de085e033e2f8972799ca75d5534b32d48aca2c5962f79497c57210 body_fp=a87690f558ffe11f70c34dec1565177c138b6a32af0c708170bc583bc22a5051 source_ref=b6d9ec2215ba7e76948b5257834bfb9312fd1910 role=test -->
Tests that `_retry_after_seconds` correctly parses numeric retry-after header values from rate limit errors.

- Verifies both integer ("3") and decimal ("0.5") string values are converted to floats
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_retry_after_none_when_header_missing_or_unparseable fingerprint=840924acaed456cea64cc1304e5051d92ea6b63661cce9ef689669eb57b0b949 body_fp=71d2695bdbebd97b498de9d6462d0e61242c8d49a3ed6b20288a47683a5de9d0 source_ref=b6d9ec2215ba7e76948b5257834bfb9312fd1910 role=test -->
Tests that `_retry_after_seconds` returns `None` when the retry-after header is missing or contains unparseable values.

- Returns `None` when `retry_after` parameter is `None`
- Returns `None` when `retry_after` contains non-numeric string
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_backoff_delay_within_cap fingerprint=01fcdc55abf97e3557281070b9ad43c1bcc8b05701af9f4be88ee8b3aef8fef8 body_fp=77e88ad67321c5f8af6bc5a9cfea054d1c5a2d65e74705b06a795b1966f0522c source_ref=b6d9ec2215ba7e76948b5257834bfb9312fd1910 role=test -->
Tests that `_backoff_delay` respects the retry cap even when attempt count would exceed it.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_honours_retry_after_exactly fingerprint=14003a3322d64979d8d605ba62373a1f973903240285043c6ef912db080fa0af body_fp=b76723507d54309e704bcb9a0c8907bd3cbace6609f713cc8bd4abab241d1084 source_ref=b6d9ec2215ba7e76948b5257834bfb9312fd1910 role=test -->
Verifies `_run_with_retry` respects the retry-after header value exactly without applying jitter.

- Tests that a 429 with retry-after="7" causes exactly 7.0 seconds of sleep
- Confirms the function succeeds after one retry and two total attempts
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_caps_retry_after fingerprint=da7b5b845dc1ed536c16b052cdbc62c4a53bdcbdffb39690d9129610c14a8852 body_fp=a56214a92a4fffc2664b7b0cd5225ca37e8b56fd07f771aec5537c687598e93f source_ref=b6d9ec2215ba7e76948b5257834bfb9312fd1910 role=test -->
Tests that retry-after headers exceeding retry_cap_seconds are clamped to the configured maximum delay.

- Simulates malicious 9999-second retry-after header that gets clamped to 2.0 seconds
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_uses_backoff_when_no_retry_after fingerprint=10f2bc60c406fba9d3c61e64e5ddcb970900091a2089b53dbe6780fa279acdc0 body_fp=7e5e15cf98808fbc4b8c2b27e6adbdb8bd47a7e8956f7cbab4acbd91ca24e2a8 source_ref=b6d9ec2215ba7e76948b5257834bfb9312fd1910 role=test -->
Tests that `_run_with_retry` uses exponential backoff with jitter when rate limit responses lack retry-after headers.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_backs_off_on_overloaded fingerprint=3cec4f4c645759f9a9756073727e18d70e342d25313642ed06bdaafb168d3516 body_fp=c5a6d0339c3185833b107ee1b472dc0c92f3dc24a8b57a944cca47bdfbfee20b source_ref=b6d9ec2215ba7e76948b5257834bfb9312fd1910 role=test -->
Verifies that `_run_with_retry` applies exponential backoff with jitter when encountering 5xx server overload errors.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_gives_up_after_max_retries fingerprint=c4f15661eb0102df7180752f5c2ff0bb83396f79eb0b98358af3ad2d3ae96517 body_fp=356fb1ed512440e68175da0f7f5e8c0e9d47235d10d39112c7714233dd4ecda3 source_ref=b6d9ec2215ba7e76948b5257834bfb9312fd1910 role=test -->
Verifies _run_with_retry respects max_retries and propagates the original exception after exhausting attempts.

- Creates scenario where call always fails with rate limit
- Confirms 2 retries means 2 sleep calls (3 total attempts)
- Validates original RateLimitError propagates after limit reached
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_propagates_non_retryable_immediately fingerprint=9503d02df17aa8a31ae1080d7f49b5535de0952085b6062231401a67680e32cb body_fp=9a36162247989afbdc01e54877c5c180ae80131041136948cd7c8da5454ca775 source_ref=b6d9ec2215ba7e76948b5257834bfb9312fd1910 role=test -->
Verifies that `_run_with_retry` immediately propagates non-retryable errors without sleeping or retrying.

- Sets up a function that always raises `AuthenticationError` (non-retryable)
- Confirms the error propagates without any recorded sleep calls
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_count_tokens_retries_on_rate_limit fingerprint=fe50e5e6a9dd7a4d2c7beea67c571e08c7c8d43d55c786363d5329ffdd6b20ed body_fp=79fe91b06b09ee9d10e4437d03335a2a8fbda8214307c3692cc6e5bc74b413c4 source_ref=b6d9ec2215ba7e76948b5257834bfb9312fd1910 role=test -->
Verifies that TrieClient.count_tokens retries on rate limit errors during token counting.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_trie_client_disables_sdk_internal_retries fingerprint=57bed553715f6bf5438ecc76ca930cd69fb6526f471cbbddb3e343bb1bf51044 body_fp=195842083fcb86d3e841ce8b0790cc8e83afeb288fb172a10f9ac85ec8893d79 source_ref=b6d9ec2215ba7e76948b5257834bfb9312fd1910 role=test -->
Verifies that TrieClient passes `max_retries=0` to the Anthropic SDK to disable its internal retry layer.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_retry_total_seconds_bounds_the_loop fingerprint=ef693c670abe4792072ca3f67a7c5d38b67a2b1b49aeacacd31daa77161247a6 body_fp=b0c2618056d7bf1918eb5c3c4ef94ba32fb565df668c17fc6b06e9a4959c2c4c source_ref=642bbe46cefd8feb139704cd6fe30e494544ec76 role=test -->
Assert that `_run_with_retry` stops retrying once `retry_total_seconds` wall-clock budget is exceeded, regardless of remaining attempt count.

- Monkeypatches `trie.models.time.monotonic` to advance 6 s per call, budget set to 10 s; expects exactly 2 calls before `APITimeoutError` propagates.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_retry_total_seconds_zero_is_unbounded fingerprint=5328b52d5e0e10699af66b12676c3cbaa99efff8d938f19d7c312df902965312 body_fp=730f7fab0f6eba603f6b0dbc24f1b6a778e4c1053e0ccadccf626d16b1b8a7cd source_ref=642bbe46cefd8feb139704cd6fe30e494544ec76 role=test -->
Assert that `retry_total_seconds=0.0` disables the wall-clock budget, allowing all `max_retries` attempts to complete.
<!-- trie:end -->