"""
[Best time to buy and sell stocks](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

from typing import List
from loguru import logger
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


@performance_measure
def profit_maximizer_bruteforce(prices: List[int]) -> int:
    """
    The function uses a nested loop to iterate through all possible buy and sell days, and updates the maximum profit seen so far.
    """
    max_profit: int = 0
    i: int = 0
    j: int = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            max_profit = max(max_profit, prices[j] - prices[i])

    return max_profit


@performance_measure
def profit_maximizer_optimized(prices: List[int]) -> int:
    """
    The function uses a single pass through the list of prices to find the minimum price seen so far, and the maximum profit that can be obtained by buying at the minimum price and selling at the current price. The maximum profit is updated as the function progresses through the list of prices.
    """

    max_profit: int = 0
    min_price: int = float("inf")

    if len(prices) < 2:
        return max_profit

    for price in prices:
        min_price: int = min(min_price, price)
        current_profit: int = price - min_price
        max_profit = max(max_profit, current_profit)

    return max_profit


def main() -> None:
    logger.add("stock_profit_maximizer.log", rotation="100 KB")
    print(
        """
            **Constraints**:  
                - List elements should be space seperated. 
                - Once the list is complete then press ENTER to send the list to the `Profit Maximizer`.
          """
    )

    nums = input("Enter the list of numbers separated by spaces: ")
    try:
        prices: List[int] = [int(x) for x in nums.split()]
    except ValueError:
        logger.error("Invalid input. Please enter integers only.")
        return

    logger.info(f"Input prices: {prices}")

    if len(prices) > 1000:
        logger.warning("Skipping bruteforce solution for large input sizes.")
    else:
        print(profit_maximizer_bruteforce(prices))

    print(profit_maximizer_optimized(prices))


if __name__ == "__main__":
    main()
