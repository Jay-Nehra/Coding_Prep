"""
    High-Level Overview:
    - Binary search algorithm is used to find the position of a target element in a sorted array.
    - It follows a divide-and-conquer approach similar to some sorting algorithms that we have just implemented.
    - The steps of the binary search algorithm are as follows:
    
        Steps:
        1. Initialize two pointers, `left` and `right`, representing the current search range.
            - `left` starts at the first index of the array.
            - `right` starts at the last index of the array.
        
        2. Calculate the middle index of the current search range:
            - `mid = left + (right - left) // 2`
        
        3. Compare the middle element with the target element:
            - If the middle element is equal to the target, return the middle index.
            - If the middle element is less than the target, update `left` to `mid + 1` to search the right sub-array.
            - If the middle element is greater than the target, update `right` to `mid - 1` to search the left sub-array.
        
        4. Repeat steps 2 and 3 until the target element is found or the search range is exhausted:
            - If the search range is exhausted (`left` > `right`), return -1 indicating the target element is not in the array.
"""

from loguru import logger
from typing import List, Tuple


def binarySearch(numbers: List[int], target: int) -> int:
    left, right = 0, len(numbers) - 1

    while left <= right:
        mid = left + (right - left) // 2
        logger.info(
            f"Left: {left}, Right: {right}, Mid: {mid}, numbers[Mid]: {numbers[mid]}"
        )

        if numbers[mid] == target:
            return mid
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def user_input() -> Tuple[List[int], int]:
    while True:
        ui_arr = input("Please enter the space-separated integer array: \n")
        target = input(
            "Please enter the value that you want to search in the array: \n"
        )
        try:
            ui = list(map(int, ui_arr.split()))
            logger.info(f"Here is the array that we are referencing: {ui}")
            target = int(target)
            logger.info(f"Here is the number that we are searching for: {target}")
            return ui, target
        except Exception as e:
            logger.debug(
                f"Could not parse the input properly. Ran into problem: \n {e}"
            )


def main():
    logger.info("Starting the Application.")
    ui, target = user_input()
    index = binarySearch(ui, target)
    if index != -1:
        logger.info(f"Index of the number that you are looking for is: {index}")
    else:
        logger.info("The number is not in the array.")


if __name__ == "__main__":
    main()
