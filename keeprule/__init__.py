"""
KeepRule - Investment principles from Buffett, Munger & masters.

Curated by https://keeprule.com
"""

import json
import os
import random as _random
from typing import List, Optional, Dict, Any

__version__ = "1.0.0"
__author__ = "William Wang"

Principle = Dict[str, Any]

# Load principles data
_data_path = os.path.join(os.path.dirname(__file__), "data", "principles.json")
with open(_data_path, "r", encoding="utf-8") as _f:
    _principles: List[Principle] = json.load(_f)


def random() -> Principle:
    """Get a random investment principle.

    Returns:
        A principle dict with keys: id, text, author, category, source.

    Example:
        >>> import keeprule
        >>> p = keeprule.random()
        >>> print(f'"{p["text"]}" -- {p["author"]}')
    """
    return _random.choice(_principles)


def random_multiple(count: int) -> List[Principle]:
    """Get multiple random non-repeating principles.

    Args:
        count: Number of principles to return.

    Returns:
        List of principle dicts.
    """
    if count >= len(_principles):
        return list(_principles)
    return _random.sample(_principles, count)


def by_author(name: str) -> List[Principle]:
    """Get principles by author name (case-insensitive partial match).

    Args:
        name: Author name or partial name (e.g., "Buffett", "Munger").

    Returns:
        List of matching principles.

    Example:
        >>> import keeprule
        >>> buffett = keeprule.by_author("Buffett")
        >>> print(f"{len(buffett)} principles from Buffett")
    """
    lower = name.lower()
    return [p for p in _principles if lower in p["author"].lower()]


def by_category(category: str) -> List[Principle]:
    """Get principles by category (case-insensitive partial match).

    Args:
        category: Category name (e.g., "Risk Management", "Value Investing").

    Returns:
        List of matching principles.

    Example:
        >>> import keeprule
        >>> risk = keeprule.by_category("Risk Management")
    """
    lower = category.lower()
    return [p for p in _principles if lower in p["category"].lower()]


def search(keyword: str) -> List[Principle]:
    """Search principles by keyword across all fields.

    Args:
        keyword: Search term to match against text, author, category, source.

    Returns:
        List of matching principles.

    Example:
        >>> import keeprule
        >>> results = keeprule.search("margin of safety")
    """
    lower = keyword.lower()
    return [
        p for p in _principles
        if lower in p["text"].lower()
        or lower in p["author"].lower()
        or lower in p["category"].lower()
        or lower in p["source"].lower()
    ]


def all() -> List[Principle]:
    """Get all investment principles.

    Returns:
        List of all 100 principles.
    """
    return list(_principles)


def authors() -> List[str]:
    """Get a sorted list of all unique author names.

    Returns:
        Sorted list of author name strings.
    """
    return sorted(set(p["author"] for p in _principles))


def categories() -> List[str]:
    """Get a sorted list of all unique categories.

    Returns:
        Sorted list of category name strings.
    """
    return sorted(set(p["category"] for p in _principles))


def get_by_id(id: int) -> Optional[Principle]:
    """Get a principle by its ID.

    Args:
        id: Principle ID (1-100).

    Returns:
        The principle dict, or None if not found.
    """
    for p in _principles:
        if p["id"] == id:
            return p
    return None


def count() -> int:
    """Get the total number of principles.

    Returns:
        Total count.
    """
    return len(_principles)
