import pytest
from loguru import logger
from merge_sorted_list import merger, validate_input


@pytest.mark.parametrize(
    "list1, list2, expected",
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([1], [], [1]),
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([-3, -2, -1], [-4, 0, 1], [-4, -3, -2, -1, 0, 1]),
        ([0, 0, 0], [0, 0], [0, 0, 0, 0, 0]),
        ([1, 1, 1], [2, 2, 2], [1, 1, 1, 2, 2, 2]),
        ([-100], [100], [-100, 100]),
        ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ],
)
def test_merger(list1, list2, expected):
    logger.info(f"Testing with list1={list1}, list2={list2}")
    result = merger(list1, list2)
    logger.info(f"Result: {result}")
    assert result == expected


@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([1, 2, 3, 4, 5], True),
        ([1, 1, 1, 1], True),
        ([5, 4, 3, 2, 1], False),
        ([], True),
        ([1], True),
        ([0, 0], True),
        ([-3, -2, -1, 0], True),
        ([1, 1, 2, 1], False),
        ([-1, -2, -3], False),
    ],
)
def test_validate_input(input_list, expected):
    logger.info(f"Testing validation with input={input_list}")
    result = validate_input(input_list)
    logger.info(f"Validation result: {result}")
    assert result == expected
