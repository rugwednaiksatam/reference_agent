"""Tests for toolbox.text - the shape every contribution copies."""
import pytest

from toolbox.text import normalize_whitespace, slugify, truncate, word_count


# ============================================================================
# Tests for word_count
# ============================================================================

def test_word_count_counts_words():
    assert word_count("one two three") == 3


def test_word_count_handles_extra_whitespace():
    assert word_count("  one   two  ") == 2


def test_word_count_rejects_non_strings():
    with pytest.raises(TypeError):
        word_count(42)


# ============================================================================
# Tests for slugify
# ============================================================================

def test_slugify_normal_cases():
    assert slugify("Hello World") == "hello-world"
    assert slugify("My First Project!") == "my-first-project"
    assert slugify("Python   Programming") == "python-programming"
    assert slugify("  Hello World  ") == "hello-world"


def test_slugify_converts_to_lowercase():
    assert slugify("UPPERCASE STRING") == "uppercase-string"
    assert slugify("CamelCaseText") == "camelcasetext"


def test_slugify_removes_special_characters():
    assert slugify("Special & Characters #$% Here!") == "special-characters-here"
    assert slugify("rock & roll") == "rock-roll"


def test_slugify_handles_unicode_characters():
    assert slugify("Crème Brûlée") == "creme-brulee"
    assert slugify("Héllo Wörld!") == "hello-world"
    assert slugify("façade naïve") == "facade-naive"
    assert slugify("El Niño") == "el-nino"


def test_slugify_handles_consecutive_spaces_and_hyphens():
    assert slugify("foo    bar") == "foo-bar"
    assert slugify("foo---bar") == "foo-bar"
    assert slugify("foo - - bar") == "foo-bar"


def test_slugify_strips_leading_and_trailing_hyphens():
    assert slugify("-leading-and-trailing-") == "leading-and-trailing"
    assert slugify("---multiple---hyphens---") == "multiple-hyphens"
    assert slugify("   ---spaces-and-hyphens---   ") == "spaces-and-hyphens"


def test_slugify_handles_already_formatted_slug():
    assert slugify("already-a-slug") == "already-a-slug"


def test_slugify_handles_numbers():
    assert slugify("Version 2.0 Released") == "version-20-released"
    assert slugify("123 456") == "123-456"


def test_slugify_handles_edge_cases():
    assert slugify("") == ""
    assert slugify("     ") == ""
    assert slugify("---") == ""
    assert slugify("!@#$%^&*()") == ""


def test_slugify_rejects_non_string_inputs():
    with pytest.raises(TypeError, match="text must be a string"):
        slugify(123)
    with pytest.raises(TypeError, match="text must be a string"):
        slugify(None)
    with pytest.raises(TypeError, match="text must be a string"):
        slugify(["not", "a", "string"])


# ============================================================================
# Tests for normalize_whitespace
# ============================================================================

def test_normalize_whitespace_normal_cases():
    assert normalize_whitespace("  Hello   World  ") == "Hello World"
    assert normalize_whitespace("Python\tProgramming") == "Python Programming"
    assert normalize_whitespace("Hello\n\nWorld") == "Hello World"


def test_normalize_whitespace_handles_tabs_and_newlines():
    assert (
        normalize_whitespace("Line 1\r\nLine 2\n\nLine 3\tEnd")
        == "Line 1 Line 2 Line 3 End"
    )
    assert normalize_whitespace("\t\tTabs\tand\tspaces  ") == "Tabs and spaces"


def test_normalize_whitespace_preserves_words_and_casing():
    assert (
        normalize_whitespace("  Keep UPPER and lower CaSe  ")
        == "Keep UPPER and lower CaSe"
    )


def test_normalize_whitespace_handles_single_word():
    assert normalize_whitespace("Word") == "Word"
    assert normalize_whitespace("   Word   ") == "Word"


def test_normalize_whitespace_handles_edge_cases():
    assert normalize_whitespace("") == ""
    assert normalize_whitespace("    ") == ""
    assert normalize_whitespace("\t\n\r\f\v") == ""


def test_normalize_whitespace_rejects_non_string_inputs():
    with pytest.raises(TypeError, match="text must be a string"):
        normalize_whitespace(123)
    with pytest.raises(TypeError, match="text must be a string"):
        normalize_whitespace(None)
    with pytest.raises(TypeError, match="text must be a string"):
        normalize_whitespace(False)


# ============================================================================
# Tests for truncate
# ============================================================================

def test_truncate_shortens_and_marks():
    assert truncate("hello world", 8) == "hello..."


def test_truncate_leaves_short_text_alone():
    assert truncate("short", 20) == "short"


def test_truncate_never_exceeds_the_limit():
    assert len(truncate("a" * 100, 10)) == 10


def test_truncate_with_custom_suffix():
    assert truncate("Hello World", 8, "!") == "Hello W!"
    assert truncate("Hello World", 8, "") == "Hello Wo"
    assert truncate("Hello World", 10, " [more]") == "Hel [more]"


def test_truncate_exact_limit():
    assert truncate("Hello", 5) == "Hello"


def test_truncate_limit_equals_suffix_length():
    assert truncate("Hello World", 3, "...") == "..."


def test_truncate_handles_empty_string():
    assert truncate("", 5) == ""
    assert truncate("", 0, "") == ""


def test_truncate_raises_when_limit_smaller_than_suffix():
    with pytest.raises(ValueError, match="limit must be at least len\\(suffix\\)"):
        truncate("Hello World", 2, "...")
    with pytest.raises(ValueError, match="limit must be at least len\\(suffix\\)"):
        truncate("Hello World", -1)


def test_truncate_rejects_non_string_text():
    with pytest.raises(TypeError, match="text must be a string"):
        truncate(123, 10)
    with pytest.raises(TypeError, match="text must be a string"):
        truncate(None, 10)


def test_truncate_rejects_invalid_limit_types():
    with pytest.raises(TypeError, match="limit must be an integer"):
        truncate("hello", "10")
    with pytest.raises(TypeError, match="limit must be an integer"):
        truncate("hello", 10.5)
    with pytest.raises(TypeError, match="limit must be an integer"):
        truncate("hello", True)
    with pytest.raises(TypeError, match="limit must be an integer"):
        truncate("hello", None)


def test_truncate_rejects_invalid_suffix_types():
    with pytest.raises(TypeError, match="suffix must be a string"):
        truncate("hello", 5, suffix=123)
    with pytest.raises(TypeError, match="suffix must be a string"):
        truncate("hello", 5, suffix=None)

