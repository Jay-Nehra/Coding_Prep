""" 
    High Level Overview:
        - This technique is a useful approach for solving problems that involve subarrays of an array.
        - This involves the concept of a `WINDOW` that slides over the array to examine teh subset of its elements.
            - This window can be of a fixed size or a variable size.
        - The idea is to move the window from start of the array to the end while maintaining the required properties like sum, maximum, minimum etc.
    
    Common Problems Solved using this technique:
        - Fixed Sized Window:
            - Find the minimum or maximum sum of any subarry of size `k`.
                - Solution: 
                    - Initializaiton: calculate the sum of the first k element 
                    - Sliding window: then move the window one element at a time by subtracting the element that is left behind and adding the new element entering the window.
        - Variable Sized Window:
            - Find the smallest subarray with a sum greater than or equal to a target value.
                - Solution:
                    - Initialization: Start with both pointers ar the beginning of the array. 
                    - Manipulate the window:
                        - expand teh window by mobing the end pointer to include more elements until condition have met, then by moving the start pointer to find the smallest window that satisfies the condition.
"""

### Fixed Sized Window:

from loguru import logger
from typing import List, Tuple


def max_sum_subarray(numbers: List[int], k: int) -> int:
    if len(numbers) < k:
        raise ValueError("The length of the array should be at least `k`.")

    max_sum = sum(numbers[:k])
    current_sum = max_sum

    logger.info(f"Initial sum of window size `{k}`: {max_sum}")

    for j in range(k, len(numbers)):
        current_sum = current_sum - numbers[j - k] + numbers[j]
        max_sum = max(max_sum, current_sum)

    return max_sum


def user_input() -> Tuple[List[int], int]:
    while True:
        numbers = input("Please enter the space separated integer array: \n")
        target = input("Please enter the window size for the subarray:   \n")
        try:
            numbers = list(map(int, numbers.split()))
            window = int(target)
            return numbers, window
        except ValueError as e:
            logger.error(
                f"Could not parse the input. Please enter valid integers. Error: {e}"
            )


def main():
    numbers, window = user_input()
    max_sum = max_sum_subarray(numbers=numbers, k=window)
    logger.info(
        f"Here is the maximum sum from the array for the given window size:   {max_sum}"
    )


if __name__ == "__main__":
    main()
