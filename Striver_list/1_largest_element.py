from typing import List
from icecream import ic


def largest_element(num_list: List[int]) -> int:
    num_list = sorted(num_list)
    return num_list[-1]


if __name__ == "__main__":
    num_list = input("Please enter the space separated list of numbers \n")
    num_list = num_list.split()
    num_list = [int(num) for num in num_list]
    ic(num_list)
    ic(largest_element(num_list=num_list))
