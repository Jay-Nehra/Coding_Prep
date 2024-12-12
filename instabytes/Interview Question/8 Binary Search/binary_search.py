"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:
    1 <= nums.length <= 104
    -104 < nums[i], target < 104
    All the integers in nums are unique.
    nums is sorted in ascending order.
"""

from loguru import logger
from typing import List


def search(nums: List[int], target: int):
    """
    Searches for a target value in a sorted list of integers using binary search.
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def validate_non_decreasing_list(numbers):
    """
    Validate if the given list is a list of numbers and is non-decreasing.
    """
    if not isinstance(numbers, list) or not all(
        isinstance(x, (int, float)) for x in numbers
    ):
        return False
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))


# def main() -> None:
#     logger.info("Starting the program.")
#     print(
#         """
#         Constraints:
#             1. Numbers should be space separated in the List.
#             2. Numbers should be in the non-decresing order.
#             3. Press Enter to send the input.
#         """
#     )
#     nums = input("Please enter the list of numbers:  ")

#     nums = [int(x) for x in nums.split()]
#     if not validate_non_decreasing_list(nums):
#         logger.error("Invalid input. Please enter a list of numbers in non-decreasing order.")
#         return

#     logger.info(f"Input List of numbers: {nums}")

#     target = int(input("Please enter the target number."))

#     result = search(nums, target)
#     logger.info(f"Target number: {target}")
#     logger.info(f"Result: {result}")

#     if result == -1:
#         print("Target number not found in the list.")
#     else:
#         print(f"Target number found at index: {result}")

import click


@click.command()
@click.option(
    "--numbers",
    prompt="Please enter the list of numbers",
    help="Numbers should be space separated.",
)
@click.option(
    "--target",
    prompt="Please enter the target number",
    help="The number to search for.",
)
def main(numbers, target):
    numbers = [int(x) for x in numbers.split()]
    if not validate_non_decreasing_list(numbers):
        click.echo(
            "Invalid input. Please enter a list of numbers in non-decreasing order."
        )
        return

    result = search(numbers, int(target))
    if result == -1:
        click.echo("Target number not found in the list.")
    else:
        click.echo(f"Target number found at index: {result}")


if __name__ == "__main__":
    main()
