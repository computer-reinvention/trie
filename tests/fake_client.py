from __future__ import annotations

from pydantic import BaseModel

from trie.models import ModelResult


def _make_default_body(qname: str) -> str:
    return f"## `{qname}`\n\nGenerated body for `{qname}`."


class FakeTrieClient:
    """Deterministic test double for `TrieClient`.

    Records call parameters so tests can verify prompt shape and token
    accounting.  Returns canned structured output based on ``output_type``.
    """

    def __init__(
        self,
        *,
        output_body: str | None = None,
        output_prose: str = "## Updated\n\nModified by patch.",
        output_notes: list[str] | None = None,
        output_reasons: list[str] | None = None,
        output_source: str | None = None,
        output_file_content: str | None = None,
        output_fixup_content: str | None = None,
        output_role: str = "domain",
        output_boundary: str = "internal",
        output_taxonomy: list[tuple[str, str]] | None = None,
        input_tokens: int = 10,
        output_tokens: int = 20,
        cache_creation_input_tokens: int = 0,
        cache_read_input_tokens: int = 0,
        model_id: str = "fake/test",
    ) -> None:
        self.full_model_id = model_id
        self.output_body = output_body
        self.output_prose = output_prose
        self.output_notes = (
            output_notes if output_notes is not None else ["* change return value  —  test"]
        )
        self.output_reasons = output_reasons if output_reasons is not None else ["test"]
        self.output_source = output_source
        self.output_file_content = output_file_content
        self.output_fixup_content = output_fixup_content
        self.output_role = output_role
        self.output_boundary = output_boundary
        # Default taxonomy used when RoleTaxonomy is requested. (name, description).
        self.output_taxonomy = (
            output_taxonomy
            if output_taxonomy is not None
            else [
                ("domain", "core business logic"),
                ("persistence", "storage and serialization"),
                ("api", "request handlers and public surface"),
            ]
        )
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.cache_creation_input_tokens = cache_creation_input_tokens
        self.cache_read_input_tokens = cache_read_input_tokens
        self.calls: int = 0
        self.last_output_type: type | None = None
        self.last_system_prompt: str = ""
        self.last_user_prompt: str = ""
        self.last_max_tokens: int = 0
        self.last_cache_prefix: str | None = None

    @property
    def model_id(self) -> str:
        return self.full_model_id

    def run(
        self,
        output_type: type[BaseModel],
        system_prompt: str,
        user_prompt: str,
        *,
        max_tokens: int = 1024,
        cache_prefix: str | None = None,
    ) -> ModelResult:
        from trie.models import (
            BatchFilterOutput,
            CallerDecision,
            FileEdit,
            FixupOutput,
            MergeNotesOutput,
            ProposedRole,
            RoleTag,
            RoleTaxonomy,
            SectionBody,
            SymbolEdit,
            SymbolProse,
        )

        self.calls += 1
        self.last_output_type = output_type
        self.last_system_prompt = system_prompt
        self.last_user_prompt = user_prompt
        self.last_max_tokens = max_tokens
        self.last_cache_prefix = cache_prefix

        if output_type is SectionBody:
            body = self.output_body
            if body is None:
                qname = "(unknown)"
                # Try to extract qname from the user prompt for realistic output.
                for line in user_prompt.splitlines():
                    if "Writing the Markdown body for the symbol `" in line:
                        qname = line.split("`")[1]
                        break
                body = _make_default_body(qname)
            # Mirror production: prose generation always yields a role, so the
            # steady-state graph is fully tagged and the role auto-backfill in
            # run_incremental short-circuits without extra LLM calls.
            output = SectionBody(body=body, role=self.output_role, boundary=self.output_boundary)
        elif output_type is MergeNotesOutput:
            output = MergeNotesOutput(
                notes=self.output_notes,
                reasons=self.output_reasons,
            )
        elif output_type is SymbolEdit:
            output = SymbolEdit(
                source=self.output_source or "",
                prose=self.output_prose,
            )
        elif output_type is FileEdit:
            output = FileEdit(
                content=self.output_file_content or "",
                prose=[SymbolProse(qname="", prose=self.output_prose)],
            )
        elif output_type is BatchFilterOutput:
            output = BatchFilterOutput(
                decisions=[CallerDecision(caller_qname="test.qname", action="skip")]
            )
        elif output_type is FixupOutput:
            output = FixupOutput(content=self.output_fixup_content or "")
        elif output_type is RoleTaxonomy:
            output = RoleTaxonomy(
                roles=[ProposedRole(name=n, description=d) for n, d in self.output_taxonomy]
            )
        elif output_type is RoleTag:
            output = RoleTag(role=self.output_role, boundary=self.output_boundary)
        else:
            raise TypeError(f"FakeTrieClient does not support output_type={output_type!r}")

        usage = type(
            "Usage",
            (),
            {
                "input_tokens": self.input_tokens,
                "output_tokens": self.output_tokens,
                "details": {
                    "cache_creation_input_tokens": self.cache_creation_input_tokens,
                    "cache_read_input_tokens": self.cache_read_input_tokens,
                },
            },
        )()
        return ModelResult(output=output, usage=usage)

    def count_tokens(self, system_prompt: str, user_prompt: str) -> int:
        return 100
