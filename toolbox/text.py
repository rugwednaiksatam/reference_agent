"""Text helpers. The worked example every contribution is modelled on."""
import re
import unicodedata


def word_count(text):
    """Count whitespace-separated words.

    >>> word_count("one two three")
    3
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return len(text.split())


def slugify(text):
    """Convert text into a URL-friendly slug.

    Normalizes unicode characters, converts text to lowercase, replaces spaces
    with hyphens, removes special characters, and strips extra hyphens.

    >>> slugify("Hello World")
    'hello-world'
    >>> slugify("My First Project!")
    'my-first-project'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    normalized = (
        unicodedata.normalize("NFKD", text)
        .encode("ascii", "ignore")
        .decode("ascii")
    )
    lowered = normalized.lower()
    cleaned = re.sub(r"[^a-z0-9\s-]", "", lowered)
    slug = re.sub(r"[-\s]+", "-", cleaned)
    return slug.strip("-")


def normalize_whitespace(text):
    """Clean unnecessary whitespace from text.

    Removes leading/trailing whitespace, replaces tabs and newlines, and collapses
    multiple consecutive whitespace characters into a single space.

    >>> normalize_whitespace("  Hello   World  ")
    'Hello World'
    >>> normalize_whitespace("Python\\tProgramming")
    'Python Programming'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return " ".join(text.split())


def truncate(text, limit, suffix="..."):
    """Shorten text to limit characters, ending with suffix.

    The result is never longer than limit.

    >>> truncate("hello world", 8)
    'hello...'
    >>> truncate("short", 20)
    'short'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if isinstance(limit, bool) or not isinstance(limit, int):
        raise TypeError("limit must be an integer")
    if not isinstance(suffix, str):
        raise TypeError("suffix must be a string")
    if limit < len(suffix):
        raise ValueError("limit must be at least len(suffix)")
    if len(text) <= limit:
        return text
    return text[:limit - len(suffix)] + suffix

