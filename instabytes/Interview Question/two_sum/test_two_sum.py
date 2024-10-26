import pytest
from loguru import logger
from two_sum import two_sum_On as two_sum


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([1, 5, 8, 3, 9, 2], 10, [1, 4]),
        ([0, 0], 0, [0, 1]),
        ([1, 2, 3, 4, 5], 9, [3, 4]),
        ([-3, 4, 3, 90], 0, [0, 2]),
        ([1000000000, 1000000000], 2000000000, [0, 1]),
        ([-10, -1, -18, -19], -28, [0, 2]),
    ],
)
def test_two_sum(nums, target, expected):
    logger.info(f"Testing with nums={nums}, target={target}")
    result = two_sum(nums, target)
    logger.info(f"Result: {result}")
    assert result == expected


# Additional edge cases
def test_two_sum_empty():
    with pytest.raises(ValueError):
        two_sum([], 5)


def test_two_sum_single_element():
    with pytest.raises(ValueError):
        two_sum([1], 5)
