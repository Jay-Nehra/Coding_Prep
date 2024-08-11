from typing import List
from loguru import logger
from math import inf


def maximum_profit(prices: List[int]) -> int:
    maximum_profit_so_far, minimum_price_so_far = -inf, inf

    for price in prices:
        todays_profit_max = price - minimum_price_so_far
        if price < minimum_price_so_far:
            minimum_price_so_far = price
        if todays_profit_max > maximum_profit_so_far:
            maximum_profit_so_far = todays_profit_max

    return maximum_profit_so_far


def user_input() -> List[int]:
    while True:
        user_input = input(
            "Please enter the space seperated integer array representing the prices for the stock over the given period. eg '1 2 3'. \n"
        )
        try:
            prices = list(map(int, user_input.split()))
            logger.info(f"This is the price for the given stock: \n{prices}")
            return prices
        except Exception as e:
            logger.error(f"Invaid Input. {e}")


def main():
    logger.info("Starting the Application. Invoking the user input functionality.")
    prices = user_input()
    max_profit = maximum_profit(prices)
    logger.info(
        f"Here is the maximum profit for the stock over the given range:   {max_profit}"
    )


if __name__ == "__main__":
    main()
