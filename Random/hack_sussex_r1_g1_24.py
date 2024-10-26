"""
Problem Statement:
    - You have a list of city pairs. Each pair `[cityA, cityB]` means there is a direct flight from `cityA` to `cityB`.
    - The goal is to find the city that no other city flies to, meaning it's the final stop in any journey and has no outgoing flights to another city.
    - There is only one such city, and it's guaranteed that the paths will form a straight line without any loops (no circular routes).

    Example:
        Given the paths:
        - `["London", "New York"]`
        - `["New York", "Lima"]`
        - `["Lima", "Sao Paulo"]`

    The destination city is `"Sao Paulo"` because it's the last city in the line and has no flights going out from it.

Key Points:
- Start at any city in the list, and follow the direct flights.
- The last city you reach, which doesn't have any flights leading to another city, is your answer.
"""

from typing import List
from loguru import logger


def destination_city(paths: List[List[str]]) -> str:
    logger.info(f"Received paths: {paths}")

    starting = set(city[0] for city in paths)
    end = set(city[1] for city in paths)

    logger.info(f"Starting cities: {starting}")
    logger.info(f"Ending cities: {end}")

    for city in end:
        if city not in starting:
            logger.info(f"Destination city found: {city}")
            return city

    logger.error("No destination city found. There might be an error in the paths.")
    return None


def user_input() -> List[List[str]]:
    while True:
        try:
            user_paths = input(
                "Please enter a list of paths (e.g., London->New York, New York->Lima). For the default value for the paths just press Enter.: \n"
            )
            if not user_paths.strip():
                logger.warning("No input received, using default paths.")
                return [
                    ["Berlin", "London"],
                    ["London", "Paris"],
                    ["Paris", "Madrid"],
                    ["Madrid", "Lisbon"],
                ]

            paths = [path.split("->") for path in user_paths.split(", ")]
            if all(len(path) == 2 for path in paths):
                return paths
            else:
                raise ValueError(
                    "Each path should contain exactly two cities separated by '->'."
                )
        except ValueError as e:
            logger.error(f"Invalid input format: {e}. Please try again.")


def main():
    paths = user_input()
    logger.info(f"Paths for processing: {paths}")

    dest = destination_city(paths=paths)

    if dest:
        logger.info(f"The last city of the given path is: {dest}")
        print("Last city of the given path is:", dest)
    else:
        logger.error("Unable to determine the destination city.")


if __name__ == "__main__":
    main()
