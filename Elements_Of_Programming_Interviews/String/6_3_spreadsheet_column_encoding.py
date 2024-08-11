"""
    Objective:
        - Alphabetical Encoding as the column naming of the spreadsheet.
        - Implement a function that converts the column encoding to the corresponding integer value.

    Solution:
        - Brute Force Approach:
            - Enumerate the column IDs, stopping when the column ID is equal to the input.
            - The logic for getting the successor of the column IDs when we reach the `Z` is slightly involved:
                - The main issue with this approach is the time complexity required for the brute force solution.
                    - If the column IDs contain `n` letters, it would take 26^n steps to get to the column ID.

        - Optimal Solution:
            - Treat the string as a base-26 number, where each letter represents a digit in this system.
            - Multiply the current result by 26 and add the numeric value of the current character.
            - This approach directly computes the integer value in a single pass with a time complexity of O(n), 
              where n is the length of the string.
"""

from loguru import logger
from typing import str


def user_input() -> str:
    while True:
        column_id = input("Please enter the column encoding (e.g., ABC): ")
        if column_id.isalpha() and column_id.isupper():
            return column_id
        else:
            logger.error(
                "Invalid input. Please enter a valid column encoding using uppercase letters only."
            )


def column_encoding_bf(column_id: str) -> int:
    """Brute force approach to find the column number."""
    current_id = ""
    count = 0
    while current_id != column_id:
        count += 1
        current_id = next_column_id(current_id)
    return count


def next_column_id(current_id: str) -> str:
    """Helper function to find the next column ID."""
    if current_id == "":
        return "A"

    last_char = current_id[-1]
    if last_char != "Z":
        return current_id[:-1] + chr(ord(last_char) + 1)
    else:
        return next_column_id(current_id[:-1]) + "A"


def column_encoding(column_id: str) -> int:
    """Optimal approach to find the column number."""
    result = 0
    length = len(column_id)
    for i in range(length):
        result += 26 ** (length - 1 - i) * (ord(column_id[i]) - ord("A") + 1)
    return result


def main():
    column_id = user_input()
    result_optimal = column_encoding(column_id=column_id)
    result_bf = column_encoding_bf(column_id=column_id)
    logger.info(
        f"The integer encoding for the column '{column_id}' using the optimal approach is: {result_optimal}"
    )
    logger.info(
        f"The integer encoding for the column '{column_id}' using the brute-force approach is: {result_bf}"
    )


if __name__ == "__main__":
    main()
