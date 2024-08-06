"""
        High-Level Overview:
            Quicksort is a divide and conquer algorithm. 
                - The main idea is to select the `pivot` element from the array and partition the other elements into two sub-arrays. 
                    - There are multiple ways to select the pivot element like the first element, last element, random element or mediam element etc.
                - Rearrange the array elements in such a way that all the elements that are less than the pivot element come before it, all the elements that are greater than the pivot come after it. 
                    - The pivot is now in the final position. 
                - Now, recursively apply the same process to the sub-arrays that are formed by the splitting the array ar the pivot. 
    """
    


from typing import List
from loguru import logger

def quicksort(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers
    else:
        # First step: pivot selection
        # let's start with the last element as the pivot 
        pivot = numbers[-1]
        #divide the array into left and right subarray
        left = [x for x in numbers if x<pivot]
        right = [x for x in numbers if x>pivot]
        middle = [x for x in numbers if x==pivot]
        logger.info(f"Current state of the Left sub-array: {left}")
        logger.info(f"Current state of the right sub-array:  {right}")
        logger.info(f"Current state of the middle sub-array:  {middle}" )
        return quicksort(left)+middle+quicksort(right)
    
def user_input() -> List[int]:
    while True: 
        user_input = input("Please enter the space separated integer arrau. \n")
        try:
            arr = list(map(int, user_input.split()))
            logger.info(f"Given array that we need to arrange :     {arr} \n")
            return arr
        except Exception as e:
            logger.error(f"Invalid input. Failed to convert to integer array. Error: {e}")
            
def main():
    logger.info("Starting the application.")
    arr = user_input()
    output = quicksort(arr)
    logger.info(f"Resulting list of numbers in the with sorted output : \n {output}")

if __name__  == '__main__':
    main()