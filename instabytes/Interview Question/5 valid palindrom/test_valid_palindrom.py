import pytest
from valid_palindrom import valid_palindrome


@pytest.mark.parametrize(
    "phrase, expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("", True),
        ("a", True),
        ("aa", True),
        ("ab", False),
        ("aba", True),
        ("abba", True),
        ("abcba", True),
        ("abcdba", False),
        ("abcdeba", False),
        ("A1b1A", True),
        ("!@$", True),
        ("1234321", True),
        ("Race a E-car", True),
        ("0P0", True),
        ("Never odd or even", True),
        ("My age is 0, 0 si ega ym.", True),
        ("1a2", False),
        ("Zeus was deified, saw Suez.", True),
    ],
)
def test_valid_palindrome(phrase: str, expected: bool) -> None:
    result = valid_palindrome(phrase)
    assert result == expected
