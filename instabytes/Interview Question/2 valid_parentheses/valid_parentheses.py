"""
[LeetCode Problem Statement](https://leetcode.com/problems/valid-parentheses/description/)

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
    * Open brackets must be closed by the same type of brackets.
    * Open brackets must be closed in the correct order.
    * Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

"""
The valid parentheses problem is an example of using a stack data structure. 

Key Pattern Identifiers:
    * When we see problems involving matching pairs or symmetry
    * When we need to process elements in a Last-In-First-Out (LIFO) order
    * Problems involving nested structures
    * Problems requiring backtracking or undoing operations

The Stack Approach, Why Stack Works Here:
    * Stack perfectly handles nested structures
    * Most recent opening bracket must match the next closing bracket
    * LIFO property ensures proper ordering
    * Easy to track unmatched brackets

Similar Problem Patterns:
    * Expression evaluation (mathematical expressions)
    * HTML/XML tag validation
    * Directory structure validation
    * Function call stack simulation
    * Undo/Redo operations

Time Complexity: O(n) Space Complexity: O(n)

Remember this pattern when we see:
    * Matching pairs
    * Nested structures
    * Balance checking
    * Symbol validation
    * Processing items in reverse order
"""


from loguru import logger
from time import perf_counter
from functools import wraps
from typing import Callable, Any


def performance_counter(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    Measures and logs execution time of the decorated function.

    Args:
        func: The function to be decorated
    Returns:
        wrapper: The decorated function with performance monitoring
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        execution_time = end_time - start_time
        logger.info(
            f"Function '{func.__name__}' execution time:  {execution_time:.6f} seconds."
        )
        logger.debug(f"Arguments passed: args={args}, kwargs={kwargs}")
        logger.debug(f"Result returned: {result}")
        return result

    return wrapper


@performance_counter
def validateParentheses(s: str) -> bool:
    stack = []
    brackets = {")": "(", "}": "{", "]": "["}

    logger.info(f"Processing string: {s}")

    for char in s:
        if char in brackets.values():  # Opening bracket
            stack.append(char)
            logger.debug(f"Added opening bracket: {char}")
        elif char in brackets:  # Closing bracket
            if not stack or stack.pop() != brackets[char]:
                logger.error(f"Invalid closing bracket: {char}")
                return False
            logger.debug(f"Matched closing bracket: {char}")

    valid = len(stack) == 0
    logger.info(f"Validation result: {valid}")
    return valid


def main():
    logger.add("valid_parentheses.log", rotation="1 MB")
    logger.info("Starting the program.")

    parentheses_string = input(
        "Enter the parentheses string that we would like to validate:  "
    )
    logger.info(f"User Input:  {parentheses_string}")

    logger.info("Running the validation testing on the user input...")

    print(validateParentheses(parentheses_string))


if __name__ == "__main__":
    main()
