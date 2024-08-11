"""
    Problem Statement:
        - Given a sorted array, remove the duplicates in-place such that each element appears only once and return the new length.
        - Do not allocate extra space for another array.

    Solution:
        - Initialize two pointers:
        - One (`last_unique`) at the beginning of the array (index 0).
        - The other (`current`) at index 1.
        - The first pointer (`last_unique`) symbolizes the position of the last unique element, and the second (`current`) is the current element being checked.
        - Compare the current element with the element at the `last_unique` position:
        - If the current element is different from the element at the `last_unique` position, it is the next unique element.
        - Update the array by moving this unique element to the position next to the last unique element.
        - Increment the `last_unique` pointer to the next position.
        - The length of the unique elements is `last_unique + 1`.

"""

from loguru import logger
from typing import List, Tuple


def remove_duplicates(numbers: List[int]) -> int:
    last_unique, current = 0, 1

    while current < len(numbers):
        logger.info(f"Current Index:    {current}, Last unique Index:   {last_unique}")
        if numbers[current] != numbers[last_unique]:
            last_unique += 1
            numbers[last_unique] = numbers[current]
            logger.info(
                f"Assigning the unique number in the beginning of the array:    {numbers[last_unique]}"
            )

        current += 1

    return last_unique + 1


def user_input() -> List[int]:
    while True:
        numbers = input("Please enter the space separated integer array: ")
        try:
            numbers = list(map(int, numbers.split()))
            return numbers
        except ValueError as e:
            logger.error(
                f"Could not parse the input. Please enter valid integers. Error: {e}"
            )


def main():
    numbers = user_input()
    unique = remove_duplicates(numbers=numbers)
    logger.info(f"Total Number of Unique Elements present in teh array:   {unique}")
    logger.info(f"And the Unique element array is:      {numbers[:unique]}")
    logger.info(f"Complete New Array after changin elements inplace:    {numbers}")


if __name__ == "__main__":
    main()
