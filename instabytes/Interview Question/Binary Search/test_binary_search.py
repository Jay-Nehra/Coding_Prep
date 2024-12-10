import pytest
from binary_search import search

@pytest.mark.parametrize("nums, target, expected", [
    ([-1, 0, 3, 5, 9, 12], 9, 4),
    ([-1, 0, 3, 5, 9, 12], 2, -1),
    ([1, 2, 3, 4, 5], 3, 2),
    ([1, 2, 3, 4, 5], 6, -1),
    ([-10, -5, 0, 5, 10], 0, 2),
    ([-10, -5, 0, 5, 10], 15, -1),
])
def test_search(nums, target, expected):
    assert search(nums, target) == expected
