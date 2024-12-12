import pytest
from valid_anagram import valid_anagram_counter, valid_anagram_sort, valid_anagram_dict


test_cases = [
    # Positive Cases
    ("anagram", "nagaram", True),
    ("listen", "silent", True),
    ("debitcard", "badcredit", True),
    # Negative Cases
    ("rat", "car", False),
    ("hello", "world", False),
    ("python", "java", False),
    # Edge Cases
    ("", "", True),
    ("a", "a", True),
    ("a", "b", False),
    ("ab", "abc", False),
    ("123", "321", True),
]


@pytest.mark.parametrize("s, t, expected", test_cases)
def test_valid_anagram_counter(s: str, t: str, expected: bool) -> None:
    result = valid_anagram_counter(s, t)
    assert result == expected


@pytest.mark.parametrize("s, t, expected", test_cases)
def test_valid_anagram_sort(s, t, expected):
    assert valid_anagram_sort(s, t) == expected


@pytest.mark.parametrize("s, t, expected", test_cases)
def test_valid_anagram_dict(s, t, expected):
    assert valid_anagram_dict(s, t) == expected
