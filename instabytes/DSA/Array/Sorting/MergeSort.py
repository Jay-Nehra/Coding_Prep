"""
    High-Level Overview:
        - Merge sort algorithm is a divide and conquer algorithm.
        - Here are the steps of the merge sort algorithm:
            - Divide: Divide the array into two halves. 
                - If the array has one or zero elements, it is already sorted. (This will serve as the base case.)
                - Otherwise split the array into two halves.
            - Conquer: Recursively sort the two halves.
                - recursively apply the merge sort algorithm to voth halves.
            - Merge the two sorted halves intp one array. 
                - Merge the two sub-arrays into one sorted array.
                - To determine the order of the merge process compare the smallest element in both of the sub-arrays.
                - the Process:
                    - start with two pointers ar the beginning of each subarray.
                    - Compare elements and then append the smaller element to the result subarray and increment the pointer for the sub-array from which the element was taken.
                    - continue until one of the sub-array is completely exausted. 
                    - append the remaining element from the other sub-array to the result sub-array.
    """

from typing import List
from loguru import logger

def merge(left: List[int], right: List[int]) -> List[int]:
    logger.info(f"Merging left: {left} and right: {right}")
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            logger.debug(f"left[{i}] ({left[i]}) < right[{j}] ({right[j]}) - adding left[{i}]")
            result.append(left[i])
            i += 1
        else:
            logger.debug(f"left[{i}] ({left[i]}) >= right[{j}] ({right[j]}) - adding right[{j}]")
            result.append(right[j])
            j += 1
    logger.debug(f"Extending remaining left: {left[i:]}")
    result.extend(left[i:])
    logger.debug(f"Extending remaining right: {right[j:]}")
    result.extend(right[j:])
    logger.info(f"Merged result: {result}")
    return result

def split(numbers: List[int]) -> List[int]:
    logger.info(f"Splitting array: {numbers}")
    if len(numbers) <= 1:
        logger.info(f"Base case reached with array: {numbers}")
        return numbers
    else:
        split_index = len(numbers) // 2
        left = numbers[:split_index]
        right = numbers[split_index:]
        logger.info(f"Left half: {left}, Right half: {right}")
        left_sorted = split(left)
        right_sorted = split(right)
        merged_result = merge(left_sorted, right_sorted)
        logger.info(f"Merged array: {merged_result}")
        return merged_result

def mergeSort(numbers: List[int]) -> List[int]:
    logger.info(f"Starting mergeSort on array: {numbers}")
    sorted_array = split(numbers)
    logger.info(f"Sorted array: {sorted_array}")
    return sorted_array

def user_input() -> List[int]:
    while True:
        ui = input("Please enter the space-separated integer array that you want to sort: \n")
        try:
            ui = list(map(int, ui.split()))
            logger.info(f"Here is the array that we need to sort: {ui}")
            return ui
        except Exception as e:
            logger.debug(f"Invalid Input. Failed to convert to the integer array. {e}")

def main():
    logger.info("Starting the Application.")
    ui = user_input()
    merged_sort_result = mergeSort(ui)
    logger.info(f"Here is the sorted output: {merged_sort_result}")

if __name__ == "__main__":
    main()
