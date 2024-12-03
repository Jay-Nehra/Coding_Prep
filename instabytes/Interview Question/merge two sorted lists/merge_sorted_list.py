"""

[21. Merge Two Sorted Lists] (https://leetcode.com/problems/merge-two-sorted-lists/description/)

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

"""

from loguru import logger
from typing import List
from functools import wraps
from time import perf_counter


def performance_measure(func):
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


"""
Time Complexity: O(n+m)
    Single pass through both lists
    Each element is processed exactly once
    Two-pointer technique eliminates redundant comparisons
Space Complexity: O(n+m)
    Only using one result list to store merged elements
    No extra data structures needed
    Minimal auxiliary space beyond the required output
"""


@performance_measure
def merger(list1: List[int], list2: List[int]) -> List[int]:
    if not validate_input(list1) or not validate_input(list2):
        raise ValueError("Input lists must be sorted in non-decreasing order")

    result = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] >= list2[j]:
            result.append(list2[j])
            j += 1
        else:
            result.append(list1[i])
            i += 1

    result.extend(list1[i:] if i < len(list1) else list2[j:])
    return result


def validate_input(lst: List[int]) -> bool:
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))


def main():
    logger.add("merge_sorted_list.log", rotation="10 KB")
    logger.info("Starting the merger :)")
    print(
        """
            **Constraints**: 
                - Make sure that the lists that you would like to merge together are sorted in non decreasing order. 
                - List elements should be space seperated. 
                - Once the list is complete then press ENTER to send the list to the `Merger`.
          """
    )

    try:
        list1 = input("Enter the first list of numbers: ")
        list1 = [int(x) for x in list1.split()]
        logger.info(f"First List: {list1}")

        list2 = input("Enter the second list of numbers: ")
        list2 = [int(x) for x in list2.split()]
        logger.info(f"Second List: {list2}")

        if not validate_input(list1):
            raise ValueError("First list must be sorted in non-decreasing order")
        if not validate_input(list2):
            raise ValueError("Second list must be sorted in non-decreasing order")

        result = merger(list1=list1, list2=list2)
        print(f"Merged result: {result}")

    except ValueError as e:
        logger.error(f"Invalid input: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
