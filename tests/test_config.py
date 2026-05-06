from __future__ import annotations

from pathlib import Path

import pytest

from trie.config import DEFAULT_CONFIG_TOML, Config, ConfigNotFoundError


def test_defaults_when_empty_dict():
    cfg = Config.from_dict({})
    assert cfg.trie.version == "0.1.0"
    assert "**/*.py" in cfg.scope.include
    assert cfg.triefacts.root == "triefacts"
    assert cfg.models.bootstrap.startswith("anthropic/")
    assert cfg.cascade.default_depth == 1
    assert cfg.cascade.hub_symbol_threshold == 20


def test_overrides_merge_per_section():
    cfg = Config.from_dict(
        {
            "scope": {"include": ["lib/**/*.py"]},
            "models": {"bootstrap": "openai/deepseek-chat"},
        }
    )
    # overridden
    assert cfg.scope.include == ["lib/**/*.py"]
    assert cfg.models.bootstrap == "openai/deepseek-chat"
    # untouched sections keep defaults
    assert cfg.triefacts.root == "triefacts"
    assert cfg.cascade.default_depth == 1
    # untouched keys within a partially-overridden section keep defaults
    assert cfg.models.cascade == "anthropic/claude-sonnet-4-6"


def test_load_roundtrips_default_template(tmp_path: Path):
    config_file = tmp_path / "trie.toml"
    config_file.write_text(DEFAULT_CONFIG_TOML)
    cfg = Config.load(config_file)
    assert cfg.trie.version == "0.1.0"
    assert cfg.triefacts.root == "triefacts"


def test_find_and_load_walks_up(tmp_path: Path):
    (tmp_path / "trie.toml").write_text(DEFAULT_CONFIG_TOML)
    nested = tmp_path / "src" / "deeply" / "nested"
    nested.mkdir(parents=True)
    cfg, root = Config.find_and_load(nested)
    assert root == tmp_path
    assert cfg.triefacts.root == "triefacts"


def test_find_and_load_raises_when_missing(tmp_path: Path):
    with pytest.raises(ConfigNotFoundError):
        Config.find_and_load(tmp_path)


def test_unknown_top_level_keys_are_ignored():
    # Forward-compat: future versions may add sections; old trie shouldn't crash.
    cfg = Config.from_dict({"future_section": {"foo": "bar"}})
    assert cfg.triefacts.root == "triefacts"


def test_unknown_keys_within_known_section_raise():
    # Typos within a known section should fail loudly.
    with pytest.raises(TypeError):
        Config.from_dict({"triefacts": {"rooot": "triefacts"}})  # typo
