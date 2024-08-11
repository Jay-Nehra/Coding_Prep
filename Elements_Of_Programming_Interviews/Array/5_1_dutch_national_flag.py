from typing import List
from icecream import ic


def dutch_flag_partition_bf(nums: List[int], pivot_index: int) -> List[int]:
    pivot = nums[pivot_index]

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                break
            ic(nums, i)

    for i in reversed(range(len(nums))):
        for j in reversed(range(i)):
            if nums[j] > pivot:
                nums[i], nums[j] = nums[j], nums[i]
                break
            ic(nums, i)

    return nums


def dutch_flag_partition_optimal_time(nums: List[int], pivot_index: int) -> List[int]:
    pivot = nums[pivot_index]
    smaller, larger = 0, len(nums) - 1

    for i in range(len(nums)):
        if nums[i] < pivot:
            nums[i], nums[smaller] = nums[smaller], nums[i]
            smaller += 1
        ic(nums, i)

    for i in reversed(range(len(nums))):
        if nums[i] > pivot:
            nums[i], nums[larger] = nums[larger], nums[i]
            larger -= 1
        ic(nums, i)

    return nums


def dutch_flag_partition(nums: List[int], pivot_index: int) -> List[int]:
    pivot = nums[pivot_index]

    smaller, equal, larger = 0, 0, len(nums)

    while equal < larger:
        ic(nums, smaller, equal, larger)
        if nums[equal] < pivot:
            nums[smaller], nums[equal] = nums[equal], nums[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif nums[equal] == pivot:
            equal += 1
        else:
            larger -= 1
            nums[larger], nums[equal] = nums[equal], nums[larger]

    return nums


if __name__ == "__main__":
    try:
        nums = input(
            "\nPlease enter the array that we want to sort. each element in the array should be only a number and they should be separated by space \n"
        )
        nums = nums.split()
        nums = [int(num) for num in nums]

        pivot_index = input("\nEnter the pivot index: \n")
        pivot_index = int(pivot_index)

        # ic(dutch_flag_partition_bf(nums, pivot_index))
        ic(dutch_flag_partition_optimal_time(nums=nums, pivot_index=pivot_index))
        ic(dutch_flag_partition(nums=nums, pivot_index=pivot_index))
    except ValueError:
        print("Error: Please enter valid integers for the array and the pivot index.")
    except IndexError:
        print("Error: The pivot index is out of range. Please enter a valid index.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
