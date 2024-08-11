from typing import List
from loguru import logger


def arrange(ip: List[int]) -> List[int]:
    ip = sorted(ip)

    for i in range(1, len(ip) - 1, 2):
        ip[i], ip[i + 1] = ip[i + 1], ip[i]

    return ip


def arrange_local_swap(ip: List[int]) -> List[int]:
    for i in range(len(ip) - 1):
        if ((i % 2 == 0) and ip[i] > ip[i + 1]) or ((i % 2 == 1) and ip[i + 1] > ip[i]):
            ip[i], ip[i + 1] = ip[i + 1], ip[i]
    return ip


def user_input() -> List[int]:
    while True:
        user_input = input("Please enter the space separated integer arrau. \n")
        try:
            arr = list(map(int, user_input.split()))
            logger.info(f"Given array that we need to arrange :     {arr} \n")
            return arr
        except Exception as e:
            logger.error(
                f"Invalid input. Failed to convert to integer array. Error: {e}"
            )


def main():
    logger.info("Starting the application.")
    arr = user_input()
    zigzag = arrange(arr)
    logger.info(
        f"Resulting list of numbers in the requested zigzag pattern is  with sorted inout : \n {zigzag}"
    )

    zigzag_ls = arrange_local_swap(arr)
    logger.info(
        f"Resulting list of numbers in the requested zigzag pattern is  without sorting the input first : \n {zigzag_ls}"
    )


if __name__ == "__main__":
    main()
