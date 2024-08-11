from typing import List, Tuple
from math import inf
from icecream import ic


def penaltemut(ip: List[int]) -> Tuple[int, int]:
    largest, largest_2, smallest, smallest_2 = -inf, -inf, inf, inf
    for num in ip:
        if num >= largest:
            largest_2 = largest
            largest = num
        elif num >= largest_2:
            largest_2 = num

        if num <= smallest:
            smallest_2 = smallest
            smallest = num
        elif num <= smallest_2:
            smallest_2 = num

    return smallest_2, largest_2


if __name__ == "__main__":
    ip = input(
        "Please enter the array (integrers seperated by a single space) that you want to perform the sorting validation on : \n"
    )
    ip = ip.split()
    ip = [int(num) for num in ip]
    ic(ip)
    ic(penaltemut(ip))
