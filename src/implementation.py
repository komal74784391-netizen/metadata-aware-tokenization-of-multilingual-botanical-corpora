"""Metadata-aware tokenizer for multilingual botanical corpora."""

from collections import Counter
from dataclasses import dataclass, field
from typing import Iterable


@dataclass
class TokenizerConfig:
    lowercase: bool = True
    preserve_taxon_names: bool = True
    metadata_tags: tuple[str, ...] = ("lang", "region", "collector")


@dataclass
class TokenizedDocument:
    tokens: list[str]
    metadata: dict[str, str] = field(default_factory=dict)


def tokenize(text: str, config: TokenizerConfig) -> list[str]:
    raw = text.strip().split()
    if config.lowercase:
        raw = [token.lower() for token in raw if token.strip()]
    if config.preserve_taxon_names:
        raw = [token if token[:1].isupper() else token.lower() for token in raw]
    return raw


def attach_metadata(document: TokenizedDocument, fields: dict[str, str]) -> TokenizedDocument:
    document.metadata.update({key: str(value) for key, value in fields.items()})
    return document


def vocabulary(documents: Iterable[TokenizedDocument]) -> Counter:
    counter: Counter = Counter()
    for document in documents:
        counter.update(document.tokens)
    return counter
