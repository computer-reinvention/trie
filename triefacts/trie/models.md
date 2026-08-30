---
trie_version: 0.3.0
source: trie/models.py
file_fingerprint: 8cac0e0f4921770d8f4dded3bb5333e9db92ec1507e62858421f458ab5ea60de
last_synced_at: '2026-08-30T03:25:40Z'
defines:
- kind: module
  qualified_name: trie/models:__module__
  lines: 1-770
- kind: function
  qualified_name: trie/models:_sdk
  lines: 26-80
  signature: def _sdk() -> SimpleNamespace
- kind: class
  qualified_name: trie/models:_LoopHolder
  lines: 106-132
  signature: class _LoopHolder
- kind: method
  qualified_name: trie/models:_LoopHolder.__init__
  lines: 109-120
  signature: 'def __init__( self, loop: asyncio.AbstractEventLoop, model: AnthropicModel, aclient: AsyncAnthropic, ) -> None'
- kind: method
  qualified_name: trie/models:_LoopHolder.__del__
  lines: 122-132
  signature: 'def __del__(self) -> None: # Close the async client on its own loop (closing its connection pool) # before closing the loop itself. Best-effort throughout: thread teardown # must never raise.'
- kind: constant
  qualified_name: trie/models:_thread_local
  lines: 135-135
- kind: function
  qualified_name: trie/models:_thread_holder
  lines: 138-154
  signature: 'def _thread_holder(make_model: Callable[[], tuple[AnthropicModel, AsyncAnthropic]]) -> _LoopHolder'
- kind: constant
  qualified_name: trie/models:_inflight_lock
  lines: 169-169
- kind: constant
  qualified_name: trie/models:_inflight_sem
  lines: 170-170
- kind: constant
  qualified_name: trie/models:_inflight_bound
  lines: 171-171
- kind: function
  qualified_name: trie/models:configure_inflight_limit
  lines: 174-185
  signature: 'def configure_inflight_limit(bound: int) -> None'
- kind: function
  qualified_name: trie/models:_inflight_slot
  lines: 189-199
  signature: def _inflight_slot() -> Iterator[None]
- kind: class
  qualified_name: trie/models:SectionBody
  lines: 208-245
  signature: class SectionBody(BaseModel)
- kind: class
  qualified_name: trie/models:ProposedRole
  lines: 248-263
  signature: class ProposedRole(BaseModel)
- kind: class
  qualified_name: trie/models:RoleTaxonomy
  lines: 266-283
  signature: class RoleTaxonomy(BaseModel)
- kind: class
  qualified_name: trie/models:RoleTag
  lines: 286-305
  signature: class RoleTag(BaseModel)
- kind: class
  qualified_name: trie/models:MergeNotesOutput
  lines: 308-312
  signature: class MergeNotesOutput(BaseModel)
- kind: class
  qualified_name: trie/models:SymbolEdit
  lines: 315-319
  signature: class SymbolEdit(BaseModel)
- kind: class
  qualified_name: trie/models:SymbolProse
  lines: 322-326
  signature: class SymbolProse(BaseModel)
- kind: class
  qualified_name: trie/models:FileEdit
  lines: 329-333
  signature: class FileEdit(BaseModel)
- kind: class
  qualified_name: trie/models:CallerDecision
  lines: 336-342
  signature: class CallerDecision(BaseModel)
- kind: class
  qualified_name: trie/models:BatchFilterOutput
  lines: 345-355
  signature: class BatchFilterOutput(BaseModel)
- kind: class
  qualified_name: trie/models:FixupOutput
  lines: 358-361
  signature: class FixupOutput(BaseModel)
- kind: class
  qualified_name: trie/models:ModelResult
  lines: 369-400
  signature: class ModelResult
- kind: method
  qualified_name: trie/models:ModelResult.__init__
  lines: 376-378
  signature: 'def __init__(self, output: BaseModel, usage: Usage) -> None'
- kind: method
  qualified_name: trie/models:ModelResult.output
  lines: 381-382
  signature: def output(self) -> Any
- kind: method
  qualified_name: trie/models:ModelResult.input_tokens
  lines: 385-386
  signature: def input_tokens(self) -> int
- kind: method
  qualified_name: trie/models:ModelResult.output_tokens
  lines: 389-390
  signature: def output_tokens(self) -> int
- kind: method
  qualified_name: trie/models:ModelResult.cache_creation_input_tokens
  lines: 393-395
  signature: def cache_creation_input_tokens(self) -> int
- kind: method
  qualified_name: trie/models:ModelResult.cache_read_input_tokens
  lines: 398-400
  signature: def cache_read_input_tokens(self) -> int
- kind: function
  qualified_name: trie/models:_retry_after_seconds
  lines: 409-419
  signature: 'def _retry_after_seconds(exc: APIStatusError) -> float | None'
- kind: function
  qualified_name: trie/models:_is_retryable
  lines: 422-445
  signature: "def _is_retryable(exc: BaseException) -> bool: # Direct anthropic exceptions: APIConnectionError covers transient network # failures (DNS lookup failure, connection refused, reset) and is the parent # of APITimeoutError; RateLimitError/InternalServerError cover 429/529. # # pydantic-ai wraps the underlying anthropic exception in its own # ModelAPIError, so a transient connection drop arrives as a ModelAPIError # (\"Connection error.\") that does NOT isinstance-match the anthropic types \u2014 # which is why these were surfaced immediately as a per-file failure instead # of being retried. We therefore (a) walk the __cause__/__context__ chain for # a retryable anthropic exception, and (b) treat a bare ModelAPIError whose # message names a connection/timeout as retryable."
- kind: function
  qualified_name: trie/models:_backoff_delay
  lines: 448-450
  signature: 'def _backoff_delay(*, attempt: int, base: float, cap: float, rng: random.Random) -> float'
- kind: function
  qualified_name: trie/models:_run_with_retry
  lines: 453-523
  signature: 'def _run_with_retry( fn: Callable[[], T], *, cfg: Sync, kind: str, model_id: str, sleep: Callable[[float], None] = time.sleep, rng: random.Random | None = None, ) -> T'
- kind: constant
  qualified_name: trie/models:T
  lines: 526-526
- kind: constant
  qualified_name: trie/models:_MODEL_ID_ALIASES
  lines: 538-538
- kind: function
  qualified_name: trie/models:_pydantic_ai_model_id
  lines: 541-543
  signature: 'def _pydantic_ai_model_id(full_model_id: str) -> str'
- kind: function
  qualified_name: trie/models:_anthropic_model_name
  lines: 546-550
  signature: 'def _anthropic_model_name(full_model_id: str) -> str'
- kind: class
  qualified_name: trie/models:TrieClient
  lines: 553-753
  signature: class TrieClient
- kind: method
  qualified_name: trie/models:TrieClient.__init__
  lines: 566-592
  signature: 'def __init__( self, full_model_id: str, *, sync_cfg: Sync | None = None, ) -> None'
- kind: method
  qualified_name: trie/models:TrieClient._make_thread_model
  lines: 594-609
  signature: def _make_thread_model(self) -> tuple[AnthropicModel, AsyncAnthropic]
- kind: method
  qualified_name: trie/models:TrieClient.run
  lines: 611-700
  signature: 'def run( self, output_type: type[BaseModel] | type[str], system_prompt: str, user_prompt: str, *, max_tokens: int = 1024, cache_prefix: str | None = None, output_retries: int = 3, ) -> ModelResult'
- kind: method
  qualified_name: trie/models:TrieClient.run_text
  lines: 702-728
  signature: 'def run_text( self, system_prompt: str, user_prompt: str, *, max_tokens: int = 1024, cache_prefix: str | None = None, ) -> ModelResult'
- kind: method
  qualified_name: trie/models:TrieClient.count_tokens
  lines: 730-753
  signature: 'def count_tokens(self, system_prompt: str, user_prompt: str) -> int'
- kind: function
  qualified_name: trie/models:make_client
  lines: 756-769
  signature: 'def make_client(model_id: str, *, sync_cfg: Sync | None = None) -> TrieClient'
incoming_refs: 77
outgoing_refs: 6
---
<!-- trie:section symbol=trie/models:__module__ fingerprint=a9e20ed43937afa6db103dcfbc91e2a9f61f87c6473a000608d6c241be4cd999 body_fp=9b387fda13f0c60ba17cbe1d813fca36e81accdb48ac1477cbbc51fd87ee73ba source_ref=6d3009ea34c12a4e21d988bbf83b56661c4fb7c8 role=orchestration -->
Provides LLM client infrastructure with structured output models and retry logic for trie documentation generation.

- SectionBody, SymbolEdit, FileEdit: Pydantic models for structured LLM outputs
- TrieClient: Agent factory wrapping pydantic-ai with prompt caching and retry handling
- ModelResult: Wrapper combining structured output with token usage counters
- Per-thread event loop management to prevent file descriptor leaks in parallel execution
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_sdk fingerprint=6b4bd67242eb8fd45dd0d79668d1dc5dc6160487c0cc0d4948c6d504513e182e body_fp=b491662589a6b641583330b6397bfef446207b767b0025f2adfa6e917c1ddb6a source_ref=575363a50a7e61687de06389efdf5cfdbd9ccdaa role=io -->
## `def _sdk() -> SimpleNamespace`

Lazily import and cache the entire LLM SDK stack (`anthropic`, `pydantic_ai`) on first call, avoiding ~1.2 s startup cost for read-only commands.

- Returns a `SimpleNamespace` exposing all SDK symbols needed by `TrieClient` and retry helpers, including `Timeout` (added; used to construct per-request timeouts).
- `httpx` is no longer imported or exposed; `Timeout` from `anthropic` replaces it for timeout construction.
- `retryable_anthropic`: tuple of exception types that warrant a retry (`RateLimitError`, `InternalServerError`, `APITimeoutError`, `APIConnectionError`).
- Falls back to `pydantic_ai.usage.Usage` if `RunUsage` is not present (older installs).
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_LoopHolder fingerprint=a91a24e87d936ceec14e77ded9ebc277f599635b24a137524812f52805f6ed01 body_fp=6f856625722a2832bc209a53c84a26c52977f656dba269c932a8cd54d390c7be source_ref=cf43f636b926264d14e4819c6c4e6e236424e130 role=model -->
## `class _LoopHolder`

Holds an asyncio event loop, AnthropicModel, and AsyncAnthropic client, closing them on garbage collection to prevent resource leaks.

- `__del__`: closes the async client and event loop when the holder is garbage collected
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_LoopHolder.__init__ fingerprint=12e93120e6c98338a86383c66fc4ec9a16af6c719f6713a1b87f79bbb566d08f body_fp=68f13cfddef738acb4ec098f212381060ed47236b4a6403a35304fb773e3f2b7 source_ref=cf43f636b926264d14e4819c6c4e6e236424e130 role=model -->
## `def __init__( self, loop: asyncio.AbstractEventLoop, model: AnthropicModel, aclient: AsyncAnthropic, ) -> None`

Stores the given event loop, model, and async client in the `_LoopHolder` instance for later cleanup.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_LoopHolder.__del__ fingerprint=d78e9d23413419838950290c956e3c4405803866c015d8c79c1d943c5c094d15 body_fp=4e76fb34e43391772c408aa44f6db138e54cab39a8c124bfd2d93049502b5c01 source_ref=cf43f636b926264d14e4819c6c4e6e236424e130 role=model -->
## `def __del__(self) -> None: # Close the async client on its own loop (closing its connection pool) # before closing the loop itself. Best-effort throughout: thread teardown # must never raise.`

Closes the _LoopHolder's async client and event loop during finalisation if they exist and aren't already closed.

- Closes the AsyncAnthropic client first to clean up its connection pool before closing the loop
- Swallows all exceptions to prevent teardown of worker threads from raising
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_thread_local fingerprint=75569d7b1b6c68e79f0dea5d5361a3b4eee93cb9a73570765a3f2ede6ca769e0 body_fp=fd490c0b1ea42acca479054ee3666f11d574aa7e09d1b8f93db04b5035d45872 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Thread-local storage for per-thread event loops to prevent file descriptor leaks in parallel execution.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_thread_holder fingerprint=570b0740f4f3a7b4739581452e005f0f259298489dea20e2efc79ad031b91eba body_fp=481ed76d990adeaf4fbc88beb32b5fb46fb474e24f40f775c07cb2a2398660ae source_ref=ed7528610d689f316f521122951d852adcfc8a59 role=util -->
## `def _thread_holder(make_model: Callable[[], tuple[AnthropicModel, AsyncAnthropic]]) -> _LoopHolder`

Returns this thread's reusable event loop and model holder, creating them on first access.

- `make_model`: Factory function called once per thread to build AnthropicModel + AsyncAnthropic client
- Creates new event loop and sets it as the thread's default when no holder exists
- Stores holder in thread-local storage to prevent fd leaks from repeated loop creation
- Ensures each thread gets its own client bound to its own loop to avoid cross-loop errors
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_inflight_lock fingerprint=0b0591e19fe812560f6db6c78c194433716b609e388f21b34daf63dcc61a9ef9 body_fp=7b3cb3945c721fb91fcaea9dffaa2e74df60e7dffe043a2bc5d121f5ea33bba0 source_ref=7b6978ad15fe0381f84e0d22885ce10437c8dfb5 role=util -->
Protects access to global inflight semaphore state during reconfiguration.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_inflight_sem fingerprint=1b10af5b4853bfeda79e44b27896d47f8b35e04865242604cebb8925cbf691bd body_fp=7328494ab6525619948eb3fbc87f0ccd3f31a9a0ea11f658e7154348bdd637b0 source_ref=7b6978ad15fe0381f84e0d22885ce10437c8dfb5 role=config -->
Global semaphore that caps concurrent LLM requests across all worker threads.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_inflight_bound fingerprint=ff1b2dc25a706dfb27a819c7aa05a832873229bf8b8f59831e8aa5641cf6a194 body_fp=15ec0eb87902109ad8c5a682930e3dd98b5ae8e18a44648a6daeb35e17abec4a source_ref=7b6978ad15fe0381f84e0d22885ce10437c8dfb5 role=config -->
Global cap on concurrent LLM requests managed by the inflight semaphore system.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:configure_inflight_limit fingerprint=d8c1b49d8dd702a33e8ca276868cc130ab8b3ba4912fa6589cdf6d50a9e1a01f body_fp=0dadbf34938f741fce8f15ec28f94be7ab93e03012b9aedb24f7fa9dfda3883b source_ref=7b6978ad15fe0381f84e0d22885ce10437c8dfb5 role=config -->
## `def configure_inflight_limit(bound: int) -> None`

Set the global cap on concurrent LLM requests process-wide, creating or rebuilding the semaphore when the bound changes.

- `bound`: Maximum concurrent requests; 0 disables throttling entirely
- Idempotent: repeated calls with same bound are no-ops
- Thread-safe via global lock for use before worker fan-out
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_inflight_slot fingerprint=0d3a9686426238175caadcbca2a164cf9e7972213c335ee205811f566295a048 body_fp=01930a9982472ac7655cd00cdcbd83de9b42e756cd9bf994d6033bae0f400fcc source_ref=7b6978ad15fe0381f84e0d22885ce10437c8dfb5 role=util -->
## `def _inflight_slot() -> Iterator[None]`

Acquires and releases one slot from the global inflight request semaphore for the duration of a network attempt.

- Yields immediately without acquiring if no semaphore is configured
- Ensures slot is released even if an exception occurs during the network call
<!-- trie:end -->
<!-- trie:section symbol=trie/models:SectionBody fingerprint=f1c4c6eb19f0882dbf14ae82cd52931932109942e91db24865048776cea2d292 body_fp=e45ee564f8ed328b3b7cf99a48a0e46c860f5a77b9ff75025f022c24c172614d source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
## `class SectionBody(BaseModel)`

Pydantic model representing triefact documentation output with architectural classification.

- `body`: markdown documentation text for the symbol
- `role`: architectural function tag (entrypoint, api, domain, etc.) with detailed standard vocabulary
- `boundary`: system boundary position (entry, exit, internal) based on external interaction patterns
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ProposedRole fingerprint=495f5b5a00623eb05a4cd6cccf1fc0a018d6bf71d20bc221a4c34130c39f3c15 body_fp=89fb193f82bfbb441139de50207f89bef308a0373e73e1bbf5d3151de91af86c source_ref=523bc80dac1cf272d259a694f1e9dbe2f39b6818 role=model -->
## `class ProposedRole(BaseModel)`

Pydantic model representing a single role in a project-specific architectural taxonomy.

- `name`: Short lowercase identifier for the role, hyphenated if multiple words
- `description`: Concrete definition enabling unambiguous symbol classification
<!-- trie:end -->
<!-- trie:section symbol=trie/models:RoleTaxonomy fingerprint=c0840ea457e6a07c657efb1d60e7b4d8afbf93f56e060d24692fa7442362eb09 body_fp=9462d8e5618a8e723304dbd53c34289ef0ab807cb4577444f5db7e9f6abcbcb1 source_ref=523bc80dac1cf272d259a694f1e9dbe2f39b6818 role=model -->
## `class RoleTaxonomy(BaseModel)`

Defines a coherent set of project-specific architectural roles derived by analyzing the entire codebase.

- **roles**: List of ProposedRole objects representing the complete role vocabulary (6-14 roles preferred)
<!-- trie:end -->
<!-- trie:section symbol=trie/models:RoleTag fingerprint=888b91be326405a05aa86b22d6fc97a36e9bbc69d04edaf2792db9e6ab448f45 body_fp=dbf1400afd68efb8c28860d47534d712d382acfa7b120b8fd29c7613951d11bd source_ref=523bc80dac1cf272d259a694f1e9dbe2f39b6818 role=model -->
## `class RoleTag(BaseModel)`

Pydantic model for classifying symbols against project-specific role vocabularies during pass 2 of role tagging.

- `role`: must match one of the role names from the injected taxonomy
- `boundary`: entry/exit/internal classification shared with SectionBody
<!-- trie:end -->
<!-- trie:section symbol=trie/models:MergeNotesOutput fingerprint=88ee7a8f24914ccaa2c1f516d5280519243c5c7c08ee77186fa40ebb85986a90 body_fp=ac495d8401da9c472a3f87508dade347a51ce3cadf503002bc7c60f9bc6689e2 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
## `class MergeNotesOutput(BaseModel)`

Pydantic model containing deduplicated patch notes and their reasons.

- `notes`: list of deduplicated patch note strings
- `reasons`: explanations for why notes were deduplicated or modified
<!-- trie:end -->
<!-- trie:section symbol=trie/models:SymbolEdit fingerprint=57dd52b0d94825f3f668f3b1bfddd8bab7a14c45b43099c5f0ae6ab55384d356 body_fp=a90a99d9b246a8dd50b994d2c85588ab0a18e84590588fa183822884f9557abe source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
## `class SymbolEdit(BaseModel)`

Pydantic model containing updated source code and documentation prose for a single symbol.

- `source`: The modified source code text
- `prose`: The generated documentation text
<!-- trie:end -->
<!-- trie:section symbol=trie/models:SymbolProse fingerprint=b7673717906ca3a3e22cb36409bfa01b9388954c8bdafa7dd74be9adc5eb8334 body_fp=d34d8844b97f1f1d2788658f02fda6dd77231c8aecb64cdcf2cb66a36bacfd2d source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
## `class SymbolProse(BaseModel)`

Holds qualified name and prose for a single symbol within a multi-symbol file edit.

- `qname`: qualified name identifier of the symbol
- `prose`: documentation text content for the symbol
<!-- trie:end -->
<!-- trie:section symbol=trie/models:FileEdit fingerprint=18c6fde126dda842b172894a1d7969bffd6979a42427ef73a00befd2c1624c94 body_fp=ad70157b6925df3552641c1c01465032d364d4d56de373bee30e434775a08024 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
## `class FileEdit(BaseModel)`

Pydantic model for updated file content paired with prose documentation for each symbol.

- `content`: The modified file source code
- `prose`: List of symbol-specific documentation entries
<!-- trie:end -->
<!-- trie:section symbol=trie/models:CallerDecision fingerprint=46e38341622b99ce0e28e749efbcd233a39dc0623e5ee3987b3cf5c46a8d3c18 body_fp=5ceee998c0c35bce18900d165771dc1df91e89f67a2e83fdfa3156f4c3afbe19 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
## `class CallerDecision(BaseModel)`

Represents a decision for one callee→caller relationship in batch filtering operations.

- `action`: defaults to "skip"
- `note`: optional additional information
- `reason`: optional explanation for the decision
<!-- trie:end -->
<!-- trie:section symbol=trie/models:BatchFilterOutput fingerprint=a6734e162ba7265cc8be36a3f0f6964772dfb4f9fd665df8b0872f350b56f293 body_fp=0ee6442f5999c413bebbef0769aec6bf9cb3f7abd84714367a1ac3668b94186f source_ref=cf43f636b926264d14e4819c6c4e6e236424e130 role=model -->
## `class BatchFilterOutput(BaseModel)`

Pydantic model containing a list of `CallerDecision` objects for batch filtering of callee-caller relationships; `decisions` defaults to an empty list so an empty model reply validates rather than raising `ValidationError`.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:FixupOutput fingerprint=c316347f4b7a219db220fbf75660ccfe74b7cd20c5798bf4b17b5870cea277a0 body_fp=8fbd2292c246cbbe0d85e19e9feb7bbff85e8aa6f1723abf5aa49d4481dde1b2 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
## `class FixupOutput(BaseModel)`

Pydantic model containing corrected file content after diagnostic processing.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult fingerprint=944e7a67fb921e06cfb00b9fdcc9087d211425e780245f8b9e055d1c8267ea8b body_fp=2a5cad95200b0c63a62b5984eddf3a836d99eb2a35c43a602d4e439bb9eb7e50 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
## `class ModelResult`

ModelResult wraps structured Pydantic output with token usage counters from LLM calls.

• `output` — the structured Pydantic model returned by the agent
• `cache_creation_input_tokens` — tokens used to create new cache entries
• `cache_read_input_tokens` — tokens read from existing cache entries
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult.__init__ fingerprint=146d3b3c6c2599af53357ed723ae6a33d43fffa4ffd45827f8701b2f0a908133 body_fp=8f5666640c8454dd195b4162a1d89bb807c88008734ad9d5041730697e89468c source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
## `def __init__(self, output: BaseModel, usage: Usage) -> None`

Initializes a ModelResult with structured output and usage statistics.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult.output fingerprint=b42bf4ac160d131fa9fd50d941884f90328324a5719e9825e955198377283293 body_fp=72c3ac5298112e49b63f721e197626fa239daa5c72053b62199199f886dcfd37 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
## `def output(self) -> Any`

Returns the structured Pydantic model output from ModelResult.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult.input_tokens fingerprint=a1b024dca62986b05239ba3a557a6a77cb6716142f9187eb02245c2c084fc341 body_fp=7486001125b33b7da84b0762f23eabe0cba6ba402eedafd640e3c2755b02b164 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
## `def input_tokens(self) -> int`

Returns input token count from ModelResult's usage data.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult.output_tokens fingerprint=b6a524062960a03daf7217df2a7f2a3978267a80402019e11007fa11e0a04fec body_fp=eb9b63450777e5403fc5058044a324210a4d2b6908497ea04f3afcd19e4dff93 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
## `def output_tokens(self) -> int`

Returns the number of output tokens from the ModelResult's usage statistics.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult.cache_creation_input_tokens fingerprint=c412d39b13ce5aa8095b9c6acdf17de80fd32005bb29c200e9d44aaccdfa1ccc body_fp=6d8cfa9dc0487e5b2130030aade668ccc32b4256f68a9e9a148a054bb8621344 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
## `def cache_creation_input_tokens(self) -> int`

Returns ModelResult's cache creation input token count from usage details, defaulting to zero.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:ModelResult.cache_read_input_tokens fingerprint=c6401a552c228d7d6a73e44517e411117af40bfb71c63e0df7e1edf3bc5b22df body_fp=f4e33942757eb7fca2a19c2b36a294d99cbe946a64fec5f2658dbd537971be2d source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
## `def cache_read_input_tokens(self) -> int`

Returns the number of input tokens read from cache during ModelResult generation.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_retry_after_seconds fingerprint=eea4acb8b1e16f87411463e5b36f7296696e1226574047bf6b26e59be639801c body_fp=4408c299c7d20505f2d3367e409a0a6ec71eb5714f786880619631483b93ea07 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
## `def _retry_after_seconds(exc: APIStatusError) -> float | None`

Extracts the retry delay in seconds from an APIStatusError's retry-after header, returning None if unavailable or invalid.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_is_retryable fingerprint=9a462dee2bc45c867178a1a94a1045618b80f35b44037f9a71ae4ffb45c1e866 body_fp=69feea58de32cf20c03d6adb92528d28e7f099797283d606f089fa0a68e817b6 source_ref=6d3009ea34c12a4e21d988bbf83b56661c4fb7c8 role=util -->
## `def _is_retryable(exc: BaseException) -> bool: # Direct anthropic exceptions: APIConnectionError covers transient network # failures (DNS lookup failure, connection refused, reset) and is the parent # of APITimeoutError; RateLimitError/InternalServerError cover 429/529. # # pydantic-ai wraps the underlying anthropic exception in its own # ModelAPIError, so a transient connection drop arrives as a ModelAPIError # ("Connection error.") that does NOT isinstance-match the anthropic types — # which is why these were surfaced immediately as a per-file failure instead # of being retried. We therefore (a) walk the __cause__/__context__ chain for # a retryable anthropic exception, and (b) treat a bare ModelAPIError whose # message names a connection/timeout as retryable.`

Returns True if the exception is retryable, walking the exception chain to handle wrapped ModelAPIError cases.

- Checks direct Anthropic exceptions (rate limit, server error, timeout, connection)
- Inspects ModelAPIError messages for connection/timeout keywords
- Traverses __cause__/__context__ chain to find wrapped retryable exceptions
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_backoff_delay fingerprint=77f4e3c66b993cc965f7254cdc34761c6af37a46bcee27228820a1f4647a0475 body_fp=527ce55ba1bf16e1954626534358ae797cdb7a60d14e2812ae5f12075964bfa8 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
## `def _backoff_delay(*, attempt: int, base: float, cap: float, rng: random.Random) -> float`

Calculates exponential backoff delay with jitter, returning a random duration between zero and the capped window.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_run_with_retry fingerprint=d86abd050b243f2ba2634f21776f52adf438ede4ede404684f4881160e285a7a body_fp=a1dd1ffada36d8f8c6120fbc79f99e88cfa1bb585b199e75c1b71af8ba747f95 source_ref=6d3009ea34c12a4e21d988bbf83b56661c4fb7c8 role=util -->
## `def _run_with_retry( fn: Callable[[], T], *, cfg: Sync, kind: str, model_id: str, sleep: Callable[[float], None] = time.sleep, rng: random.Random | None = None, ) -> T`

Executes a callable with exponential backoff retry logic for rate limits, timeouts, and server errors.

- Respects `retry-after` headers for rate limit exceptions
- Emits telemetry events on each retry attempt with delay and reason
- Stops retrying after `cfg.max_retries` attempts, non-retryable exceptions, or elapsed `cfg.retry_total_seconds` budget
- Prints a stderr line per retry and a budget-exhaustion message when the time budget is exceeded
<!-- trie:end -->
<!-- trie:section symbol=trie/models:T fingerprint=511f85b873237a1963584329b2ded56f290efb33b59ff4f1f52a3ff84742f48d body_fp=d54080f28b388848817988e57cc93775750bb1d46b147449f3fe09535a32e6c4 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
Type alias for Any used as a TypeVar placeholder in the retry helper function.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_MODEL_ID_ALIASES fingerprint=8ea596648226175d01cd1ab68d645474d71f1cfbfdcfb7979035a854a0124f68 body_fp=3c9f7a7e8db2d345ae74211923836c8d2d5c347f1539b3938a84a75bc2a382f1 source_ref=4b7e4089969de6d955dc0a0a5314c5d7d6aacd57 role=config -->
Empty mapping; reserved for trie `provider/model` → pydantic_ai `provider:model` overrides when a model ID requires non-trivial translation beyond a `/`→`:` swap.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_pydantic_ai_model_id fingerprint=a0a6b3d1a8febf77bc636de899705a5808a8091b4f9ec907ce9d9611400a53ec body_fp=8067e32fe3dc06816da4bd3bae4baa38b0dd71ff216487d07946f1ef3510e557 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
## `def _pydantic_ai_model_id(full_model_id: str) -> str`

Converts trie's provider/model format to pydantic_ai's provider:model format using aliases or simple substitution.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:_anthropic_model_name fingerprint=3c87d22ca61cada7c6dd2721cf27ba2000942a7010fc3dac57aeb0cd6ca74261 body_fp=5266dc158016de8d4538b280682ea6e46e7b75c9191bd69ce0e6f2e66bdeaf89 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
## `def _anthropic_model_name(full_model_id: str) -> str`

Extract the bare Anthropic model name from a full trie model ID by stripping the provider prefix.
<!-- trie:end -->
<!-- trie:section symbol=trie/models:TrieClient fingerprint=548fa2056f79a7136f9e16d95c56158b504d6286c116945207a053e69a3803e2 body_fp=9e31cbc1b743690429aef4bd7ad92d18bda9396e97a66e1585e6b1a84f07d4ba source_ref=575363a50a7e61687de06389efdf5cfdbd9ccdaa role=io -->
## `class TrieClient`

Wraps Pydantic AI agent creation and execution with structured output, prompt caching, and retry logic.

- `run`: Creates one-shot agent; accepts `output_type=str` for plain-text mode or a `BaseModel` subclass for structured output; supports configurable `output_retries` for pydantic-ai's internal validation retries
- `run_text`: Convenience wrapper that calls `run` with `output_type=str` for code-generation paths
- `count_tokens`: Uses raw Anthropic SDK to estimate token costs without generation
- Manages per-thread event loops and HTTP clients to avoid file descriptor leaks and connection errors
- Applies exponential backoff retry on rate limits and server errors
- Configures request timeouts to prevent hung connections from blocking worker threads indefinitely
<!-- trie:end -->
<!-- trie:section symbol=trie/models:TrieClient.__init__ fingerprint=04b6ed79ba0cbb2b4fd287c4ec4a51a31da9fef185b437014606458b8ddc0c14 body_fp=09ba71dee7605b76737eaaed959708a4b9de8a0ce33f0f405c7c5c8a6d8d7deb source_ref=575363a50a7e61687de06389efdf5cfdbd9ccdaa role=domain -->
## `def __init__( self, full_model_id: str, *, sync_cfg: Sync | None = None, ) -> None`

Initializes `TrieClient` with model ID conversion, timeout configuration, and raw Anthropic client.

- `full_model_id`: trie's provider/model format (e.g., `"anthropic/claude-sonnet-4-6"`)
- `sync_cfg`: retry configuration, defaults to `Sync()` if `None`
- Sets bounded HTTP timeout using `anthropic.Timeout` (not `httpx.Timeout`) to prevent infinite stalls
- Creates raw Anthropic client with retries disabled and timeout configured
<!-- trie:end -->
<!-- trie:section symbol=trie/models:TrieClient._make_thread_model fingerprint=26679b1d1fcca5bba12edd1393767a0b62ee83a48ddadf10afe0492546ce0c6b body_fp=45816933d6a51a5d97e220509850e1c96dea6a13b40386211258a2092782b5f6 source_ref=6d3009ea34c12a4e21d988bbf83b56661c4fb7c8 role=io -->
## `def _make_thread_model(self) -> tuple[AnthropicModel, AsyncAnthropic]`

Creates thread-specific AnthropicModel and AsyncAnthropic client instances to avoid cross-thread event loop conflicts.

- Called once per worker thread by `_thread_holder`
- Returns tuple of model and async client with configured timeout
- Prevents file descriptor leaks and connection errors from shared clients
<!-- trie:end -->
<!-- trie:section symbol=trie/models:TrieClient.run fingerprint=617cc9fa75deaa20ea12148909ff060544700b3b3f84c02e19279f2fe5cdc4b3 body_fp=9aa32ad5f00d46f76944f6643af51e06624a23f106493f02546ba3a640af59c5 source_ref=6d3009ea34c12a4e21d988bbf83b56661c4fb7c8 role=domain -->
## `def run( self, output_type: type[BaseModel] | type[str], system_prompt: str, user_prompt: str, *, max_tokens: int = 1024, cache_prefix: str | None = None, output_retries: int = 3, ) -> ModelResult`

TrieClient.run creates a pydantic-ai Agent with structured or plain-text output and executes it with retry logic and rate limiting.

- `output_type`: accepts `str` for plain-text mode (no JSON schema) in addition to `BaseModel` subclasses
- `cache_prefix`: when provided, cached as a shared prefix across multiple calls for cost efficiency
- `max_tokens`: maximum tokens for the model output (default 1024)
- `output_retries`: pydantic-ai-level output validation retries passed to `Agent` (default 3)
- Returns `ModelResult` containing structured output and token usage counters
<!-- trie:end -->
<!-- trie:section symbol=trie/models:TrieClient.run_text fingerprint=5fb414109bd7f5773dca61e8e058cb84f27fb4ee079479d0063b660eb78eb4a0 body_fp=a256eaffd7e5163e8324601e3a8dffe092ba0f3ac51b7ffa21703ae996174d10 source_ref=eac7d606b20c417f983eb8e133fd62c5dcf7aa6a role=io -->
## `def run_text( self, system_prompt: str, user_prompt: str, *, max_tokens: int = 1024, cache_prefix: str | None = None, ) -> ModelResult`

Invoke `TrieClient.run` with `output_type=str`, returning a `ModelResult` whose `output` is the raw model text instead of a structured Pydantic object.

- `cache_prefix`: forwarded to `run`; cached as a leading user content block before `user_prompt`.
- `result.output`: raw string (fenced code block parsed by `trie.edits.textgen`).
<!-- trie:end -->
<!-- trie:section symbol=trie/models:TrieClient.count_tokens fingerprint=3c0147fbfd76558d6fd2a6176f921093c72e3ac31e6c8b6ad60f9438d78015cd body_fp=2f7cd8beb8a4cd33a0686f8981a75a7cbe3ad6fc6a57527d0b90fdab9022c775 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
## `def count_tokens(self, system_prompt: str, user_prompt: str) -> int`

TrieClient.count_tokens returns the number of input tokens via the Anthropic count_tokens API for system and user prompts.

- Empty user prompts are replaced with "." to avoid API rejection while preserving cost estimation accuracy
<!-- trie:end -->
<!-- trie:section symbol=trie/models:make_client fingerprint=3357d2c90a369504b954bcdaeda5dc66234fd60cb89e23082eda6f4ddc882612 body_fp=f45c7b25631aa760b4b7d55bdd49d147b8dc15de4e18abff28dc9bbc08f9d2a6 source_ref=1a9fb4f4e7b12424d36509260b65dcfc94171e79 role=llm-client -->
## `def make_client(model_id: str, *, sync_cfg: Sync | None = None) -> TrieClient`

Constructs a TrieClient from a provider/model ID string, validating format and supporting only anthropic provider.
<!-- trie:end -->