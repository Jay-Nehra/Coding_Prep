""" 
    - Problem Description:
        - We are given an integer array and a target sum. The goal is to find the smallest subarray whose sum of elements is greater than or equal to the target sum. If no such subarray exists, return -1.

    - Solution:
        - Initialization:
            - Start with both the `start` and `end` pointers at the beginning of the array.
            - Initialize `current_sum` to 0.
            - Track the minimum length of the subarray with a variable, initially set to infinity (or a large value).
        - Expand the Window:
            - Incrementally move the `end` pointer to the right, adding the value of `numbers[end]` to `current_sum`.
            - Continue this process until `current_sum` is greater than or equal to the target sum.
        - Contract the Window:
            - While `current_sum` is greater than or equal to the target sum, update the minimum length.
            - Move the `start` pointer to the right, subtracting `numbers[start]` from `current_sum` to minimize the subarray length while maintaining the sum condition.
        - Result:
            - If a valid subarray is found, return the minimum length. Otherwise, return -1 if no such subarray exists.
"""
from math import inf
from loguru import logger 
from typing import List, Tuple

def min_length_subarray(numbers: List[int], target: int) -> int:
    current_sum, left, right = 0, 0, 0
    min_length = inf
    
    for right in range(len(numbers)):
        current_sum += numbers[right]
        logger.info(f"This is the current sum:  {current_sum}")
        while current_sum >= target:
            min_length = min(min_length, right-left+1)
            logger.info(f"Current minimum length is: {min_length}")
            current_sum -= numbers[left]
            logger.info(f"Contracting the window from the start. Previous left index is at:  {left}")
            left += 1
            
    return -1 if min_length == inf else min_length

def user_input() -> Tuple[List[int], int]:
    while True:
        ui = input("Please enter the array that we are going to reference: \n")
        target_sum = input("Please enter the threshold sum that we need to go over: \n")
        try:
            ui = list(map(int, ui.split()))
            target_sum = int(target_sum.strip())
            return ui, target_sum
        except ValueError as e:
            logger.error(f"Could not parse the input. Please enter valid integers. Error: {e}")
            
def main():
    numbers, target = user_input()
    min_length = min_length_subarray(numbers=numbers, target=target)
    logger.info(f"Here is the Minimum length for the subarray whose element is greater than threshold:   {min_length}")
    
if __name__ == '__main__':
    main()