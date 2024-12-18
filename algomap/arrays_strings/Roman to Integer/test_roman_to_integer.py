import pytest
from roman_to_integer import roman_to_int


@pytest.mark.parametrize(
    "roman, expected",
    [
        ("III", 3),
        ("IV", 4),
        ("IX", 9),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("I", 1),
        ("II", 2),
        ("V", 5),
        ("X", 10),
        ("XL", 40),
        ("L", 50),
        ("XC", 90),
        ("C", 100),
        ("CD", 400),
        ("D", 500),
        ("CM", 900),
        ("M", 1000),
        ("MMMDCCCLXXXVIII", 3888),
        ("MMMCMXCIX", 3999),
        ("", 0),
        ("MMMM", 4000),
        ("IXIX", 18),
        ("XXIV", 24),
        ("XLII", 42),
        ("LXXX", 80),
        ("CXL", 140),
        ("DCCC", 800),
        ("MCM", 1900),
        ("MMXXIII", 2023),
    ],
)
def test_roman_to_int(roman, expected):
    assert roman_to_int(roman) == expected
