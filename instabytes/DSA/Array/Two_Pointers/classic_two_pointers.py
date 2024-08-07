""" 
    High Level Overview:
        - This is often used to solve the array related problems, particularly those involving the searching of pairs or triplets that often meet the certain conditions, removing duplicates, or partitioning arrays.
        - Steps:
            - You use two pointers to iterate through the array simultaneously, 
                - typically from different directions like one from start and one from end,
                - or both starting from the same point but moving at different speeds. 
"""

"""
    Classic Two Pointers from Opposite Ends:
        - Problem: Find a pair in a sorted array that sums up to a target value.
        - Initialization: One pointer at the beginning (left), one at the end (right).
        - Movement: Move pointers towards each other based on the sum comparison with the target.
    """

from loguru import logger
from typing import List, Tuple

def pair_sum(numbers: List[int], target: int) -> List[Tuple[int, int]]:
    left, right = 0, len(numbers)-1
    result = []
    pair = ()
    while left < right:
        logger.info(f"Numbers at the left pointer:  {numbers[left]}, and number at the right pointer: {numbers[right]}")
        current_sum = numbers[left] + numbers[right]
        logger.info(f"Current Sum from the pair:    {current_sum}")
        if current_sum == target:
            pair = (numbers[left], numbers[right])
            logger.info(f"Adding the pair as this is equal to the target value: {pair}")
            result.append(pair)
            left +=  1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    logger.info(f"These are the total pair from the array which are equal to the target sum:    {result}")
    return result


def user_input() -> Tuple[List[int], int]:
    while True:
        numbers = input("Please enter the space separated integer array: ")
        target = input("Please enter the target that we are finding the pair sum for:   ")
        try:
            numbers = list(map(int, numbers.split()))
            target = int(target)
            return numbers, target
        except ValueError as e:
            logger.error(f"Could not parse the input. Please enter valid integers. Error: {e}")
            
def main():
    numbers, target = user_input()
    pairs = pair_sum(numbers=numbers, target=target)
    logger.info(f"Here are the pairs from the array that sum upto the target:   {pairs}")
    
if __name__ == '__main__':
    main()