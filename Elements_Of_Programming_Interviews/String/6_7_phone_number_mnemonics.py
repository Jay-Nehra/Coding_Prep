"""
    Problem Statement:
        - Given a string representing a phone number, compute all possible mnemonics (letter combinations) that the phone number could represent. 
        - Each digit on the phone corresponds to a specific set of characters, similar to the mappings on a traditional phone keypad.

    Solution:
        - Recursive Method:
            - Start with an empty prefix and recursively append characters for each digit from the mapping.
            - For each digit in the phone number, look up the corresponding characters and recursively combine them with the combinations generated for the previous digits.
            - When the end of the phone number is reached, add the completed combination to the list of results.
        
        - Iterative Method:
            - Begin with an initial list containing an empty string as the only "combination".
            - For each digit in the phone number, look up the corresponding characters and expand the list of current combinations by appending each possible character.
            - Continue expanding the list until all digits have been processed, resulting in a list of all possible mnemonics.
"""

from typing import List
from loguru import logger

class MnemonicsMapping:
    def __init__(self) -> None:
        self.mapping = {
            "0": "",
            "1": "",
            "2": "ABC",
            "3": "DEF",
            "4": "GHI",
            "5": "JKL",
            "6": "MNO",
            "7": "PQRS",
            "8": "TUV",
            "9": "WXYZ",
        }

    def get_letter(self, digit: str) -> str:
        return self.mapping.get(digit, "")


def mnemonics_iterative(numbers: List[int]) -> List[str]:
    mapping = MnemonicsMapping()

    result = [""]

    for num in numbers:
        letters = mapping.get_letter(str(num))
        logger.debug(f"Processing digit: {num}, letters: {letters}")

        new_result = []
        for res in result:
            for letter in letters:
                new_result.append(res + letter)

        result = new_result

    return result

def mnemonics_recursive(numbers: List[int], index: int = 0, current_combination: str = "") -> List[str]:
    if index == len(numbers):
        return [current_combination]
    
    mapping = MnemonicsMapping()
    current_digit = str(numbers[index])
    letters = mapping.get_letter(current_digit)
    
    result = []
    for letter in letters:
        result.extend(mnemonics_recursive(numbers, index + 1, current_combination + letter))
    
    return result

def mnemonics_recursive_with_helper(numbers: List[int]) -> List[str]:
    mapping = MnemonicsMapping()
    result = []
    
    def _mnemonics_helper(index: int, current_combination: str):
        if index == len(numbers):
            result.append(current_combination)
            return
        
        current_digit = str(numbers[index])
        letters = mapping.get_letter(current_digit)
        
        for letter in letters:
            _mnemonics_helper(index + 1, current_combination + letter)
    
    _mnemonics_helper(0, "")
    return result

def user_input() -> List[int]:
    while True:
        user_numbers = input("Please enter a sequence of digits (0-9): ")
        try:
            if not user_numbers.isdigit():
                raise ValueError("Input must be a string of digits.")
            return [int(digit) for digit in user_numbers]
        except ValueError as e:
            logger.error(f"Invalid input: {e}. Please try again.")

def main():
    numbers = user_input()
    logger.info(f"User input digits: {numbers}")

    mnemonics_iter = mnemonics_iterative(numbers)
    logger.info(f"Mnemonics (Iterative): {mnemonics_iter}")

    mnemonics_recur = mnemonics_recursive(numbers)
    logger.info(f"Mnemonics (Recursive): {mnemonics_recur}")

    mnemonics_recur_helper = mnemonics_recursive_with_helper(numbers)
    logger.info(f"Mnemonics (Recursive with Helper): {mnemonics_recur_helper}")

if __name__ == "__main__":
    main()
