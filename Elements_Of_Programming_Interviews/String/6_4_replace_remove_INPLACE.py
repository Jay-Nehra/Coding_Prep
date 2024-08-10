""" 
    Problem Statement:
        - Given an Input list of charectors, the goal is to perform the transformation inplace.
        and return the new length of the transformed list. 
        - Example: 
            - Input: [a,b,c,d,e]
            - Replace `a` with 2 `d` and remove `b` from the input. 
            
    Solution:
        - This can be quite easy to solve if we write the result to a new array,
            - we skip the `b` and wherever we encounter `a` we append `d` twice to the result list. 
            
        - Challenge:
            - But the challenge comes from teh restriction on doing this without allocation of additional space.
            - Approach:
                - This is an exercise in understanding how to manipulate the arrays in place with constraints on the space complexity. 
                - Forward Pass:
                    - First, count the number of `a's` and remove all the `b's` while shifting the element in the list.
                -Backward Pass:
                    - Replace `a` with two `d's` by working backwards from the end of the resulting list from teh first pass. 
"""

from typing import List, Tuple
from loguru import logger

def replace_and_remove(characters: List[str]) -> Tuple[List[str], int]:
    a_count = 0 
    write_index = 0
    
    # Forward pass
    for i, char in enumerate(characters):
        logger.info(f"Current char in the array is: {char} and the input array index is: {i}.")
        if char != 'b':
            characters[write_index] = char 
            write_index += 1
        if char == 'a':
            a_count += 1
    
    logger.info(f"Array after forward pass: {characters[:write_index]} with a_count = {a_count}")
    
    # Resize the array
    characters.extend([''] * a_count)
    
    # Backward pass:
    final_size = write_index + a_count - 1
    
    for j in reversed(range(write_index)):
        logger.info(f"Current char in the array is: {characters[j]} and the input array index is: {j}.")
        char = characters[j]
        if char == 'a':
            characters[final_size] = 'd'
            characters[final_size - 1] = 'd'
            final_size -= 2
        else: 
            characters[final_size] = char
            final_size -= 1
    
    return characters, write_index + a_count

def user_input() -> List[str]:
    while True:
        chars = input("Please enter a space-separated list of characters (e.g., a c b a b): \n")
        try:
            chars = chars.split()
            if all(len(c) == 1 and c.isalpha() for c in chars):
                return chars
            else:
                raise ValueError("Each input should be a single alphabetic character.")
        except ValueError as e:
            logger.error(f"Could not parse the input. Please enter valid single characters. Error: {e}")

def main():
    characters = user_input()
    logger.info(f"Input characters: {characters}")
    
    modified_chars, new_length = replace_and_remove(characters=characters)
    
    logger.info(f"Modified array: {modified_chars[:new_length]}")
    logger.info(f"New length of the array after operations: {new_length}")

if __name__ == '__main__':
    main()
