""" 
[Two Sum Leetcode](https://leetcode.com/problems/two-sum/description/)

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 
Constraints:
* 2 <= nums.length <= 104
* -109 <= nums[i] <= 109
* -109 <= target <= 109
* Only one valid answer exists.

"""

from functools import wraps
from time import perf_counter
from typing import List

from loguru import logger


def performance_counter(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        logger.info(
            f"Function '{func.__name__}' execution time: {execution_time:.6f} seconds"
        )
        logger.debug(f"Arguments passed: args={args}, kwargs={kwargs}")
        logger.debug(f"Result returned: {result}")
        return result

    return wrapper


@performance_counter
def two_sum_On2(nums: List[int], target: int) -> List[int]:
    """
    This implementation of two_sum function has a time complexity of O(n²) because:
    1. It uses nested loops:
        - The outer loop iterates through each element (n times)
        - For each element, the inner loop iterates through remaining elements (n-1, n-2, ..., 1 times)
    """
    logger.info(f"Starting two_sum_On2 with nums={nums} and target={target}")
    for index, value in enumerate(nums):
        for index2, value2 in enumerate(nums[index + 1 :]):
            logger.debug(f"Checking pair: {value} + {value2}")
            if value + value2 == target:
                logger.success(f"Found solution: indices [{index}, {index2+index+1}]")
                return [index, index2 + index + 1]
    logger.warning("No solution found")


@performance_counter
def two_sum_On(nums: List[int], target: int) -> List[int]:
    """
    This implementation of two_sum function has a time complexity of O(n) because:
    1. It uses a dictionary to  store the complement of each element and its index.
    2. It iterates through the list once.
    """
    logger.info(f"Starting two_sum_On with nums={nums} and target={target}")
    # Initialize an empty dictionary to store the complement for the each element and its index.
    seen = {}
    # Now, we will iterate over the list of numbers once.
    for index, value in enumerate(nums):
        complement = target - value
        logger.debug(f"Current value: {value}, Complement needed: {complement}")
        if complement in seen:
            # If the complement is in the dictionary, we have found a pair that adds up to the target. So we return the indices of the two numbers.
            logger.success(f"Found solution: indices [{seen[complement]}, {index}]")
            return [seen[complement], index]
        # If the complement is not in the dictionary, we add the current number and its index to the dictionary.
        seen[value] = index
    logger.warning("No solution found")


def main():
    logger.add("two_sum.log", rotation="10 KB")
    logger.info("Starting the program")

    nums = input("Enter the list of numbers seperated by spaces: ")
    nums = [int(x) for x in nums.split()]
    logger.info(f"Input numbers: {nums}")

    target = int(input("Enter the target number: "))
    logger.info(f"Target number: {target}")

    logger.info("Running O(n²) solution")
    print(two_sum_On2(nums, target))

    logger.info("Running O(n) solution")
    print(two_sum_On(nums, target))


if __name__ == "__main__":
    main()
