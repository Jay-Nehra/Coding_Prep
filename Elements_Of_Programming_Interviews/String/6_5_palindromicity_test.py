"""
    Palindromicity Test:
        For the purpose of this problem, a palindrome is a string that reads the same forwards and backwards after removing all non-alphanumeric characters and ignoring case.
        
    Solution:    
        - A naive approach would be to reverse the string and compare it to the original.
        - However, we can use the `Two Pointers` technique, which we've already worked with, to simulate reversing the string.
        - In each iteration of the loop, we skip non-alphanumeric characters from both the left and right pointers and only compare the lowercase characters.
        - The loop continues until the two pointers cross each other.
"""

from loguru import logger


def palindromicity_test(sentence: str) -> bool:
    left, right = 0, len(sentence) - 1 
    
    logger.debug(f"Initial string: '{sentence}'")
    
    while left < right:
        while left < right and not sentence[left].isalnum():
            logger.debug(f"Skipping non-alphanumeric at left index {left}: '{sentence[left]}'")
            left += 1
        
        while left < right and not sentence[right].isalnum():
            logger.debug(f"Skipping non-alphanumeric at right index {right}: '{sentence[right]}'")
            right -= 1
        
        logger.debug(f"Comparing left '{sentence[left]}' at index {left} with right '{sentence[right]}' at index {right}")
        
        if sentence[left].lower() != sentence[right].lower():
            logger.debug(f"Mismatch found: left '{sentence[left]}' != right '{sentence[right]}'")
            return False
        
        left += 1
        right -= 1
        
    logger.debug("The string is a palindrome.")
    return True


def user_input() -> str:
    while True:
        sentence = input(
            "Please enter the sentence that you want to test for palindromicity:\n"
        )
        try:
            if sentence.strip():
                return sentence
            else:
                raise ValueError("Input should not be empty.")
        except ValueError as e:
            logger.error(f"Invalid input. Please enter a valid sentence. Error: {e}")


def main():
    sentence = user_input()
    logger.info(f"Input sentence: '{sentence}'")

    is_palindrome = palindromicity_test(sentence=sentence)

    if is_palindrome:
        logger.info("The sentence is a palindrome.")
    else:
        logger.info("The sentence is not a palindrome.")


if __name__ == "__main__":
    main()
