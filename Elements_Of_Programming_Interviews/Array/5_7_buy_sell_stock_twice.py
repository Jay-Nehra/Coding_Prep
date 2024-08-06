from typing import List
from loguru import logger
from math import inf

def maximum_profit(prices: List[int]) -> int:
    logger.info("Starting calculation of maximum profit...")
    maximum_total_profit, minimum_price_so_far = 0, float('inf')
    first_transaction_profit = [0] * len(prices)
    
    logger.info("Starting forward pass...")
    for i, price in enumerate(prices):
        minimum_price_so_far = min(price, minimum_price_so_far)
        maximum_total_profit = max(maximum_total_profit, price - minimum_price_so_far)
        first_transaction_profit[i] = maximum_total_profit
        logger.debug(f"Day {i}: price={price}, minimum_price_so_far={minimum_price_so_far}, "
                     f"maximum_total_profit={maximum_total_profit}")
    
    logger.info("Forward pass completed.")
    
    maximum_total_profit, maximum_price_so_far = 0, float('-inf')
    
    logger.info("Starting backward pass...")
    for i in reversed(range(1, len(prices))):
        maximum_price_so_far = max(maximum_price_so_far, prices[i])
        maximum_profit_today = maximum_price_so_far - prices[i]
        combined_profit = maximum_profit_today + first_transaction_profit[i - 1]
        maximum_total_profit = max(maximum_total_profit, combined_profit)
        logger.debug(f"Day {i}: price={prices[i]}, maximum_price_so_far={maximum_price_so_far}, "
                     f"maximum_profit_today={maximum_profit_today}, combined_profit={combined_profit}")
    
    logger.info("Backward pass completed.")
    logger.info(f"Maximum total profit calculated: {maximum_total_profit}")
    
    return maximum_total_profit

def user_input() -> List[int]:
    while True:
        ui = input("Please Enter the Stock Price History. It should be space seperated interger values. \n")
        try:
            ui = list(map(int, ui.split()))
            logger.info(f"This if the stock price history: {ui}")
            return ui
        except ValueError:
            logger.error(f"Invalid Input. {ValueError}")    

def main():
    prices = user_input()
    max_profit = maximum_profit(prices)
    logger.info(f"Maximum profit for selling and buyin the stock twice is:   {max_profit}")

if __name__ == '__main__':
    main()