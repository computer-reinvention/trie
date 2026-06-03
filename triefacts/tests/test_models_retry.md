---
trie_version: 0.1.5
source: tests/test_models_retry.py
file_fingerprint: f0d1f70f36554ed3bbd1ef5abee2442c8173badb35fe4516ea95320fe2c7bcb4
last_synced_at: '2026-06-03T20:58:12Z'
description: Retry-on-rate-limit behaviour of `AnthropicClient`.
defines:
- kind: module
  qualified_name: tests/test_models_retry:__module__
  lines: 1-265
- kind: function
  qualified_name: tests/test_models_retry:_fake_response
  lines: 41-47
- kind: function
  qualified_name: tests/test_models_retry:_rate_limit
  lines: 50-55
- kind: function
  qualified_name: tests/test_models_retry:_overloaded
  lines: 58-63
- kind: function
  qualified_name: tests/test_models_retry:_auth_error
  lines: 66-71
- kind: class
  qualified_name: tests/test_models_retry:_Recorder
  lines: 75-81
- kind: method
  qualified_name: tests/test_models_retry:_Recorder.sleep
  lines: 80-81
- kind: function
  qualified_name: tests/test_models_retry:_frozen_rng
  lines: 84-85
- kind: function
  qualified_name: tests/test_models_retry:test_is_retryable_picks_up_rate_limit_and_5xx_and_timeout
  lines: 91-94
- kind: function
  qualified_name: tests/test_models_retry:test_is_retryable_rejects_auth_and_other_4xx
  lines: 97-99
- kind: function
  qualified_name: tests/test_models_retry:test_retry_after_reads_header_when_present
  lines: 102-104
- kind: function
  qualified_name: tests/test_models_retry:test_retry_after_none_when_header_missing_or_unparseable
  lines: 107-109
- kind: function
  qualified_name: tests/test_models_retry:test_backoff_delay_within_cap
  lines: 112-120
- kind: function
  qualified_name: tests/test_models_retry:test_run_with_retry_honours_retry_after_exactly
  lines: 126-144
- kind: function
  qualified_name: tests/test_models_retry:test_run_with_retry_caps_retry_after
  lines: 147-164
- kind: function
  qualified_name: tests/test_models_retry:test_run_with_retry_uses_backoff_when_no_retry_after
  lines: 167-183
- kind: function
  qualified_name: tests/test_models_retry:test_run_with_retry_backs_off_on_overloaded
  lines: 186-201
- kind: function
  qualified_name: tests/test_models_retry:test_run_with_retry_gives_up_after_max_retries
  lines: 204-216
- kind: function
  qualified_name: tests/test_models_retry:test_run_with_retry_propagates_non_retryable_immediately
  lines: 219-230
- kind: function
  qualified_name: tests/test_models_retry:test_count_tokens_retries_on_rate_limit
  lines: 236-248
- kind: function
  qualified_name: tests/test_models_retry:test_trie_client_disables_sdk_internal_retries
  lines: 251-264
incoming_refs: 0
outgoing_refs: 21
---
<!-- trie:section symbol=tests/test_models_retry:__module__ fingerprint=a6284e6d3d43bdfbf0da732945adb2b4f31147c92bea47aee100d7f556c22d00 body_fp=16d3a50873b1e714e26129ace70e0ba2a0ca4938e6fb07c2c1df2f1179adaca8 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 -->
Tests retry behaviour for AnthropicClient against rate limits, server errors, and timeouts.

- Rate limits with retry-after headers trigger exact delays
- Rate limits without headers use exponential backoff with jitter
- 5xx errors including 529 overloaded trigger exponential backoff
- Timeouts trigger exponential backoff
- Non-retryable 4xx errors propagate immediately without delays
- After max_retries attempts the original exception propagates
- Retry protection applies to both message generation and token counting
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_fake_response fingerprint=fe8fd6035dcb46c04e29a488aa45d382ac2b3da33fbeaf3f74f28d1db959576b body_fp=f3ed167fec4ada7ba503d93a7769360b9a7bcc46549f8b9dfe6fb05e363e670f source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 -->
Builds an httpx.Response for testing SDK exception classes.

- `retry_after`: when provided, sets the "retry-after" header value
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_rate_limit fingerprint=817d1f499887aef57cd5bba15d5b0e6425ba9d6dfd19bf4589b67b7534d58c2d body_fp=415be7b0f2697ab5fb6e51e22981c524ec56e90caa9eec0aaaa6f2afc91dda84 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 -->
Creates a RateLimitError for testing with optional retry-after header.

- `retry_after`: if provided, sets the retry-after header value in the fake response
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_overloaded fingerprint=623c945b55ddebd9607ef7be5d70b96290bd820023bd75445a18f08a49b5617c body_fp=6f64ca785d2a61336a71486ce1f826bb4e2fb57d6f207a4dd8ae117134acb404 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 -->
Creates an InternalServerError with a 529 status code for testing server overload scenarios.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_auth_error fingerprint=2107cda8409df874e0dc468d7445a1094a779ebe23afebfc673a3e4b0c232a06 body_fp=4d489c8ddde733d37eca492f972dba51bdf9cdfab032a880e9a96babaeda74d5 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 -->
Creates an AuthenticationError with a 401 status code for testing non-retryable error scenarios.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_Recorder fingerprint=826822d20981072b453816aaf9b60f912784c91a83a4ac4e87296e36785412fd body_fp=a9826ae208a39bac818d1384ced952f0cbc02a841deae3e6c069a4a716ba85f0 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 -->
Test utility class that records sleep call durations without actually sleeping.

- `sleeps`: List accumulating all sleep durations passed to the sleep method
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_Recorder.sleep fingerprint=e45d93e687af0bc59b5bf2e3bd6e8c5c5dbf519386b2560872a90a23f43e8ef9 body_fp=eaca0c5527333cc4cd860ce3391b4c5bdbedaf31a49d4d40985d7159920e36aa source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 -->
Records sleep call duration in `_Recorder.sleeps` list without actually sleeping.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:_frozen_rng fingerprint=21a30f0dca12cc5a6c96c27a311a47b71773540767a177151ea8082a02589cbf body_fp=e3969914ed0960726bb22db6060bbb8994c884596107029ff31bf53a55c521b4 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 -->
Creates a seeded random.Random instance for deterministic test outcomes.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_is_retryable_picks_up_rate_limit_and_5xx_and_timeout fingerprint=57e8cdd19d86cc19a2e20ade35d7eec104a0e39a2510080690d734677e8027dd body_fp=1529e937785c070e50e935d2f5ba9132981c7cb14fa8de10319415919818e2b0 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 -->
Tests that `_is_retryable` returns True for rate limit errors, 5xx server errors, and timeout exceptions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_is_retryable_rejects_auth_and_other_4xx fingerprint=ad1733d7e18cc28b638ccebae3dbd460280fc5547172d8d6b73456101792f9ea body_fp=cb0968836ef734d93a684dd7f55e0523636dd408244ed31ea80bcefad6b6d662 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 -->
Tests that `_is_retryable` returns False for authentication errors and non-API exceptions.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_retry_after_reads_header_when_present fingerprint=8a962d853de085e033e2f8972799ca75d5534b32d48aca2c5962f79497c57210 body_fp=99a0187f3284ac5c12f5e2f1948bdc0d6d5b8031ac4c2554b0de08135f8a2b26 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 -->
Verifies that `_retry_after_seconds` correctly parses numeric retry-after headers into float delays.

- Tests both integer ("3") and decimal ("0.5") header values
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_retry_after_none_when_header_missing_or_unparseable fingerprint=840924acaed456cea64cc1304e5051d92ea6b63661cce9ef689669eb57b0b949 body_fp=d0a911cb11bcb8a5fb630a1c3860d0e8d2e68402fbbffcb6ce03f02027279381 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 -->
Verifies that `_retry_after_seconds` returns None when the retry-after header is missing or contains invalid data.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_backoff_delay_within_cap fingerprint=01fcdc55abf97e3557281070b9ad43c1bcc8b05701af9f4be88ee8b3aef8fef8 body_fp=69e25f691ede906571d5f6def7cf677b2482d17b1ac36ae907a4c89c1c5d69b0 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 -->
Verifies that _backoff_delay respects the retry_cap_seconds limit even for high attempt numbers.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_honours_retry_after_exactly fingerprint=14003a3322d64979d8d605ba62373a1f973903240285043c6ef912db080fa0af body_fp=1a2edde4c2e042e0995f5403f0ba8dca89e600fd6a0b32b2799823d80efd7f8b source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 -->
Tests that `_run_with_retry` respects retry-after header values exactly without applying jitter.

- Uses a mocked function that raises `RateLimitError` with `retry-after="7"` on first call
- Verifies the sleep duration matches the header value precisely (7.0 seconds)
- Confirms the function succeeds on the second attempt
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_caps_retry_after fingerprint=da7b5b845dc1ed536c16b052cdbc62c4a53bdcbdffb39690d9129610c14a8852 body_fp=e082f5598bdc92db2e2eb8e322f3855a5e5dad14caade529a744c776a24475f8 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 -->
Tests that excessive retry-after headers are clamped to the configured maximum delay.

- Simulates server returning retry-after=9999 seconds but caps delay at 2.0 seconds
- Verifies protection against malicious or buggy upstream servers that could pin workers
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_uses_backoff_when_no_retry_after fingerprint=10f2bc60c406fba9d3c61e64e5ddcb970900091a2089b53dbe6780fa279acdc0 body_fp=3f24f18e79d55ff1b4fccd55faab50858a6164dc9ad805ce1e18d260dd87cdf5 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 -->
Tests that `_run_with_retry` uses exponential backoff when rate-limited without retry-after header.

- Verifies backoff delays fall within configured cap bounds
- Confirms retry attempts occur before eventual success
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_backs_off_on_overloaded fingerprint=3cec4f4c645759f9a9756073727e18d70e342d25313642ed06bdaafb168d3516 body_fp=4e9e2b6cf831fdbb3e0a3d0968b2d6f56995ead7d4014a215b5f347b914b7b60 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 -->
Tests that `_run_with_retry` applies exponential backoff with jitter when facing a 529 overloaded error.

- Simulates one 529 error followed by success
- Verifies exactly one sleep occurs within the configured cap bounds
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_gives_up_after_max_retries fingerprint=c4f15661eb0102df7180752f5c2ff0bb83396f79eb0b98358af3ad2d3ae96517 body_fp=f41f94a402a2d2ac81ac5b0da608db726e745b04ae9079bb5977c1f83ad1a363 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 -->
Verifies that `_run_with_retry` propagates the original exception after exhausting max_retries attempts.

- Creates a function that always raises RateLimitError with retry-after of 0
- Configures max_retries=2, expects 2 sleep calls before giving up
- Asserts the RateLimitError is raised and exactly 2 retry delays occurred
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_run_with_retry_propagates_non_retryable_immediately fingerprint=9503d02df17aa8a31ae1080d7f49b5535de0952085b6062231401a67680e32cb body_fp=753c1e5b589f440189344143aafa4517e11b14ff7d848493ebe5faa4f1f28572 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 -->
Verifies that `_run_with_retry` propagates non-retryable exceptions immediately without any sleep delays.

- Uses AuthenticationError as the non-retryable error type
- Asserts no sleep calls are recorded when the exception is non-retryable
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_count_tokens_retries_on_rate_limit fingerprint=fe50e5e6a9dd7a4d2c7beea67c571e08c7c8d43d55c786363d5329ffdd6b20ed body_fp=4f69be7a97d40d00e1a5bede2a4acce10ec97b8059f6db3bd1ad4947c224dd60 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 -->
Verifies that TrieClient.count_tokens retries on rate limit errors during plan-time token counting.
<!-- trie:end -->
<!-- trie:section symbol=tests/test_models_retry:test_trie_client_disables_sdk_internal_retries fingerprint=57bed553715f6bf5438ecc76ca930cd69fb6526f471cbbddb3e343bb1bf51044 body_fp=98d31cabf3cc887b9bbcd8b3ea890fff4ee95484347d3e3098235c1b71a8f628 source_ref=85a5a52974f5f74ebaec7d5758ff3fb98966a251 -->
Verifies that TrieClient passes `max_retries=0` to the Anthropic SDK client to disable duplicate retry layers.
<!-- trie:end -->