import pytest
from single_number import single_number, single_number_xor, single_number_k_times


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
    ],
)
def test_single_number_xor(nums, expected):
    assert single_number_xor(nums) == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 2, 3, 2], 3),
        ([0, 1, 0, 1, 0, 1, 99], 99),
        ([7, 7, 7, 8], 8),
    ],
)
def test_single_number_k_times(nums, expected):
    assert single_number_k_times(nums, 3) == expected
