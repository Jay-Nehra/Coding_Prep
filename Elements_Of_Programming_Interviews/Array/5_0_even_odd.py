from typing import List
from icecream import ic

def even_odd(nums: List[int]) -> List[int]:
    left, right = 0, len(nums)-1
    while left < right:
        if nums[left] % 2 == 0:
            left += 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            right = right - 1
            
    return nums


if __name__ == "__main__":
    ip = input("Please enter the array (integrers seperated by a single space) that you want to perform the sorting validation on : \n")
    ip = ip.split()
    ip = [int(num) for num in ip ]
    ic(ip)
    ic(even_odd(ip))