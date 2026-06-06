"""Role taxonomy: the project-specific role vocabulary that constrains role tagging.

Roles are not an arbitrary per-symbol free choice. trie derives a single coherent
vocabulary fitted to *this* codebase (pass 1), and every symbol is then classified
against exactly that fixed set (pass 2, see `trie.sync.roles`). This keeps the
graph's role axis legible — a dozen meaningful groups instead of a long tail of
near-synonyms.

The taxonomy is persisted at ``<triefacts.root>/role_taxonomy.json`` — committed
alongside the triefact tree, not in ``.trie/`` (which is a regenerable cache that
gets wiped). The DB mirrors per-symbol roles for query speed, but the taxonomy
itself and the section roles live in the durable artifact tree, so a graph.db wipe
loses neither.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

from trie import telemetry
from trie.config import Config
from trie.graph.store import Store
from trie.models import RoleTaxonomy, TrieClient

TAXONOMY_FILENAME = "role_taxonomy.json"


@dataclass(frozen=True)
class Role:
    name: str
    description: str


@dataclass(frozen=True)
class Taxonomy:
    roles: tuple[Role, ...]

    def names(self) -> list[str]:
        return [r.name for r in self.roles]

    def is_empty(self) -> bool:
        return len(self.roles) == 0

    def to_json(self) -> dict[str, object]:
        return {"roles": [{"name": r.name, "description": r.description} for r in self.roles]}

    @classmethod
    def from_json(cls, raw: dict[str, object]) -> Taxonomy:
        roles_raw = raw.get("roles", [])
        roles: list[Role] = []
        if isinstance(roles_raw, list):
            for item in roles_raw:
                if isinstance(item, dict):
                    name = str(item.get("name", "")).strip().lower()
                    desc = str(item.get("description", "")).strip()
                    if name:
                        roles.append(Role(name=name, description=desc))
        return cls(roles=tuple(roles))


def taxonomy_path(project_root: Path, config: Config) -> Path:
    """Canonical location of the committed taxonomy file."""
    return project_root / config.triefacts.root / TAXONOMY_FILENAME


def load_taxonomy(project_root: Path, config: Config) -> Taxonomy | None:
    """Return the persisted taxonomy, or None if absent/unreadable.

    An unreadable file (missing, malformed, wrong schema) collapses to None so the
    caller re-derives — the same conservative posture as the freshness stamp.
    """
    path = taxonomy_path(project_root, config)
    if not path.exists():
        return None
    try:
        raw = json.loads(path.read_text())
    except (OSError, json.JSONDecodeError):
        return None
    if not isinstance(raw, dict):
        return None
    tax = Taxonomy.from_json(raw)
    return tax if not tax.is_empty() else None


def save_taxonomy(project_root: Path, config: Config, taxonomy: Taxonomy) -> Path:
    """Write the taxonomy to its canonical path, creating parent dirs. Returns the path."""
    path = taxonomy_path(project_root, config)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(taxonomy.to_json(), indent=2) + "\n")
    return path


TAXONOMY_SYSTEM_PROMPT = """\
You are trie, designing the architectural role vocabulary for a single codebase.

You are given a survey of the codebase: every symbol's qualified name, kind, and a
one-line description, grouped by file. Propose a small, coherent set of roles that
partitions this codebase by architectural function — the kind of work each symbol
does, not its location.

Principles:
- Fit the vocabulary to THIS codebase. Use the survey's actual concerns; don't
  emit generic roles the code doesn't exhibit.
- Prefer 6-14 roles. Each must be distinct and non-overlapping.
- Every symbol in the survey should plausibly map to exactly one role.
- Role names are short, lowercase, hyphenated if two words.
"""


@dataclass(frozen=True)
class TaxonomyResult:
    taxonomy: Taxonomy
    input_tokens: int
    output_tokens: int
    cache_creation_input_tokens: int
    cache_read_input_tokens: int


def derive_taxonomy(
    *,
    store: Store,
    client: TrieClient,
    max_survey_symbols: int = 1200,
    max_tokens: int = 1500,
) -> TaxonomyResult:
    """Survey the codebase and have the model propose a fitted role vocabulary.

    Reads every symbol's name + one-liner from the store (capped at
    `max_survey_symbols` to bound prompt size), formats a compact survey, and asks
    the model for a `RoleTaxonomy`. Does not persist — the caller saves the result.
    """
    survey = store.survey_symbols()
    if len(survey) > max_survey_symbols:
        # Even stride keeps the sample spread across files rather than front-loaded.
        stride = len(survey) / max_survey_symbols
        survey = [survey[int(i * stride)] for i in range(max_survey_symbols)]

    lines: list[str] = []
    current_file = None
    for qname, kind, one_liner, file_path in survey:
        if file_path != current_file:
            lines.append(f"\n# {file_path}")
            current_file = file_path
        suffix = f" — {one_liner}" if one_liner else ""
        lines.append(f"- ({kind}) {qname}{suffix}")
    survey_text = "\n".join(lines)

    with telemetry.timed("derive_taxonomy", symbols=len(survey)):
        result = client.run(
            RoleTaxonomy,
            system_prompt=TAXONOMY_SYSTEM_PROMPT,
            user_prompt=(
                "Here is the codebase survey. Propose the role vocabulary.\n\n"
                f"<survey>\n{survey_text}\n</survey>"
            ),
            max_tokens=max_tokens,
        )
    proposed: RoleTaxonomy = result.output
    roles = tuple(
        Role(name=r.name.strip().lower(), description=r.description.strip())
        for r in proposed.roles
        if r.name.strip()
    )
    return TaxonomyResult(
        taxonomy=Taxonomy(roles=roles),
        input_tokens=result.input_tokens,
        output_tokens=result.output_tokens,
        cache_creation_input_tokens=result.cache_creation_input_tokens,
        cache_read_input_tokens=result.cache_read_input_tokens,
    )
