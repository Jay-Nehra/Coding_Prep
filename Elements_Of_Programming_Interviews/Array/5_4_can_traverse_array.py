from typing import List
from loguru import logger

# Basic logging
logger.add("EOPI.log", format="{time} {level} {message}", level="INFO")
logger.info("5_4 Can Traverse the Array")


def can_traverse(nums: List[int]) -> bool:
    index, max_traversable_distance = 0, 0
    while (
        max_traversable_distance < len(nums) - 1
    ) and index <= max_traversable_distance:
        max_traversable_distance = max(max_traversable_distance, nums[index] + index)
        index += 1
    return max_traversable_distance >= len(nums) - 1


def get_user_input():
    while True:
        user_input = input("\nPlease enter an integer array (e.g., '1 2 3'): ")
        try:
            nums = list(map(int, user_input.split()))
            if not nums:
                raise ValueError("Empty array provided.")

            return nums
        except ValueError as e:
            print(
                f"Invalid input. Please ensure you enter integers separated by spaces.\nError: {e}"
            )


def main():
    nums = get_user_input()
    result = can_traverse(nums)
    print(f"Can traverse: {result}")


if __name__ == "__main__":
    main()
