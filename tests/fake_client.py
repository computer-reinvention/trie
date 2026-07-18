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

    def run_text(
        self,
        system_prompt: str,
        user_prompt: str,
        *,
        max_tokens: int = 1024,
        cache_prefix: str | None = None,
    ) -> ModelResult:
        """Return canned plaintext for the code-gen path.

        The real code path now asks for a fenced code block plus delimited prose
        sections (see ``trie.edits.textgen``) instead of structured output. We
        synthesise that text from the same canned fields the structured ``run``
        used, so existing tests keep their assertions on source/prose/content.

        Which body to emit is inferred from the prompt: a fixup prompt yields the
        fixup content; a multi-symbol file prompt yields the file content with a
        prose section per requested qname; otherwise a single symbol edit.
        """
        from trie.edits import textgen

        self.calls += 1
        self.last_output_type = None
        self.last_system_prompt = system_prompt
        self.last_user_prompt = user_prompt
        self.last_max_tokens = max_tokens
        self.last_cache_prefix = cache_prefix

        is_fixup = "diagnostics errors" in user_prompt.lower() or "Diagnostics:" in user_prompt
        # The multi-symbol file prompt embeds one section per changed symbol and
        # asks for qname-keyed prose blocks; detect it by that delimiter request.
        is_file = textgen.PROSE_OPEN_QNAME in user_prompt

        if is_fixup:
            code = self.output_fixup_content or ""
            text = f"```\n{code}\n```\n"
        elif is_file:
            code = self.output_file_content or ""
            qnames = self._extract_requested_qnames(user_prompt)
            sections = "".join(
                f"{textgen.PROSE_OPEN_QNAME}{qn}>>>\n{self.output_prose}\n{textgen.PROSE_END}\n"
                for qn in qnames
            )
            text = f"```\n{code}\n```\n\n{sections}"
        else:
            code = self.output_source or ""
            text = (
                f"```\n{code}\n```\n\n"
                f"{textgen.PROSE_OPEN}\n{self.output_prose}\n{textgen.PROSE_END}\n"
            )

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
        return ModelResult(output=text, usage=usage)

    @staticmethod
    def _extract_requested_qnames(user_prompt: str) -> list[str]:
        from trie.edits import textgen

        qnames: list[str] = []
        for chunk in user_prompt.split(textgen.PROSE_OPEN_QNAME)[1:]:
            qn = chunk.split(">>>", 1)[0].strip()
            if qn:
                qnames.append(qn)
        # De-dup while preserving order; fall back to a single empty-key section
        # so callers that key prose by "" (legacy single-symbol fakes) still work.
        seen: set[str] = set()
        out = [q for q in qnames if not (q in seen or seen.add(q))]
        return out or [""]

    def count_tokens(self, system_prompt: str, user_prompt: str) -> int:
        return 100
