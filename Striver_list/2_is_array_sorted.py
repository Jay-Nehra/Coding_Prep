from typing import List
from math import inf
from icecream import ic


def is_array_sorted(ip: List[int]) -> bool:
    # status = True
    previous = -(inf)
    for num in ip:
        if num >= previous:
            previous = num
        else:
            return False

    return True


if __name__ == "__main__":
    ip = input(
        "Please enter the array (integrers seperated by a single space) that you want to perform the sorting validation on : \n"
    )
    ip = ip.split()
    ip = [int(num) for num in ip]
    ic(ip)
    ic(is_array_sorted(ip))
