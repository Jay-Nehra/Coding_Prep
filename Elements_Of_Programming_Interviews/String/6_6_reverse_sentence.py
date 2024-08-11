"""
    Problem Statement:
        - Given a string containing a set of words separated by whitespace, the objective is to transform this string so that the words appear in reverse order.

    Solution:
        - Split-Reverse-Join:
            - First, split the string based on spaces to get a list of words.
            - Then, reverse the list of words.
            - Finally, join the reversed list back into a single string using spaces.

        - In-Place Reversal:
            - We'll start by reversing the entire string, which gives a mirror image of the original sentence.
            - Then, reverse each word individually to restore the correct order of characters within the words.
"""

from loguru import logger
from typing import List
def reverse_words_split_join(sentence: str) -> str:
    logger.info(f"Original sentence: '{sentence}'")
    
    words_list = sentence.split()
    logger.debug(f"List of words after split: {words_list}")
    
    words_list = words_list[::-1]
    logger.debug(f"List of words after reversing: {words_list}")
    
    reversed_sentence = ' '.join(words_list)
    logger.info(f"Reversed sentence: '{reversed_sentence}'")
    
    return reversed_sentence

def reverse_word(word_list: List[str], left: int, right: int) -> None:
    while left < right:
        word_list[left], word_list[right] = word_list[right], word_list[left]
        left, right = left + 1, right - 1

def reverse_words_in_place(sentence: str) -> str:
    logger.info(f"Original sentence: '{sentence}'")
    
    sentence_list = list(sentence)
    reverse_word(sentence_list, 0, len(sentence_list) - 1)
    logger.debug(f"Sentence after full reversal: {''.join(sentence_list)}")
    
    left = 0
    for i in range(len(sentence_list)):
        if sentence_list[i] == ' ':
            reverse_word(sentence_list, left, i - 1)
            logger.debug(f"Sentence after reversing word at index {left} to {i-1}: {''.join(sentence_list)}")
            left = i + 1
    
    reverse_word(sentence_list, left, len(sentence_list) - 1)
    logger.debug(f"Sentence after reversing last word: {''.join(sentence_list)}")
    
    reversed_sentence = ''.join(sentence_list)
    logger.info(f"Reversed sentence (In-Place): '{reversed_sentence}'")
    
    return reversed_sentence




def user_input() -> str:
    while True:
        sentence = input(
            "Please enter the sentence that you want to reverse the words in:\n"
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

    reversed_sentence_split_join = reverse_words_split_join(sentence=sentence)
    logger.info(f"Reversed sentence (Split-Join): '{reversed_sentence_split_join}'")

    reversed_sentence_in_place = reverse_words_in_place(sentence=sentence)
    logger.info(f"Reversed sentence (In-Place): '{reversed_sentence_in_place}'")

if __name__ == "__main__":
    main()



