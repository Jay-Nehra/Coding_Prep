""" 
    Problem Statement:
        - The `Look and Say` Sequence starts with 1. Subsequent numbers are derived by describing the previous number in terms of consecutive digits. 
        - To generate the next entry of the sequence from the previous entry, read off the digits of the previous entry, counting the number of digits in the groups of the same digit. 
        - Write a program that takes as input an integer `n` and returns the nth integer in the look-and-say sequence. Return result as a sequence.
"""

from loguru import logger


def user_input() -> int:
    while True:
        user_number = input(
            "Please enter a positive integer for the Look-and-Say sequence: "
        )
        try:
            number = int(user_number)
            if number <= 0:
                raise ValueError("Input must be a positive integer.")
            logger.info(f"User input accepted: {number}")
            return number
        except ValueError as e:
            logger.error(f"Invalid input: {e}. Please try again.")


def look_and_say(number: int) -> str:
    if number <= 1:
        return str(1)

    sequence = [0] * number
    sequence[0] = "1"

    for i in range(1, number):
        previous = sequence[i - 1]
        result = ""
        count = 1
        digit = previous[0]

        for j in range(1, len(previous)):
            if previous[j] == digit:
                count += 1
            else:
                result += str(count) + digit
                digit = previous[j]
                count = 1

        result += str(count) + digit
        sequence[i] = result

        logger.info(f"Generated sequence up to {i+1}: {sequence[i]}")

    return sequence[number - 1]


def main():
    number = user_input()

    logger.info(f"Calculating the {number}th term in the Look-and-Say sequence.")
    result = look_and_say(number)

    logger.info(f"The {number}th term in the Look-and-Say sequence is: {result}")
    print(f"The {number}th term in the Look-and-Say sequence is: {result}")


if __name__ == "__main__":
    main()
