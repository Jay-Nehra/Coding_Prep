from loguru import logger
from typing import List


def user_input():
    while True:
        user_input = input(
            "\n Please enter the space separated integer array and it should be sorted in the ascending order (eg '1 2 3 4'):  "
        )
        try:
            nums = list(map(int, user_input.split()))
            logger.info("Input received successfully.")
            return nums
        except ValueError:
            logger.error(
                "Invalid Input. Please follow all the guidelines while entering the input."
            )


def remove_duplicates(nums: List[int]) -> List[int]:
    if not nums:
        logger.warning("Provided List is empty.")
        return 0
    last_unique_index = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[last_unique_index]:
            nums[last_unique_index + 1] = nums[i]
            last_unique_index += 1

    return nums[: last_unique_index + 1], last_unique_index + 1


def main():
    nums = user_input()
    unique_array, unique_count = remove_duplicates(nums)
    logger.info(f"Array after removing the duplicate elements:  {unique_array} ")
    logger.info(f"Unique numbers in the resulting array:  {unique_count}")


if __name__ == "__main__":
    logger.add("EOPI.log", format="{time} - {level} - {message}", level="DEBUG")
    main()
