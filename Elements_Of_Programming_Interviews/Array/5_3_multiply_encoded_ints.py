from typing import List
from icecream import ic


def multiply_encoded_array_ints(num1: List[int], num2: List[int]) -> List[int]:
    sign = -1 if ((num1[0] < 0) ^ (num2[0] < 0)) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0] * (len(num2) + len(num1))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    # remove the leading zero,
    # thought process: use the enumerate and next to find the first index with non zero element

    result = result[
        next((i for i, x in enumerate(result) if x != 0), len(result)) :
    ] or [0]
    result[0] *= sign
    return result


if __name__ == "__main__":
    try:
        nums1 = input(
            "\nPlease enter the first number each digit should be seperated by space \n"
        )
        nums1 = nums1.split()
        nums1 = [int(num) for num in nums1]

        nums2 = input(
            "\n\nPlease enter the Second number each digit should be seperated by space \n"
        )
        nums2 = nums2.split()
        nums2 = [int(num) for num in nums2]

        ic(multiply_encoded_array_ints(nums2, nums1))

    except ValueError:
        print("Error: Please enter valid integers for the array and the pivot index.")
    except IndexError:
        print("Error: The pivot index is out of range. Please enter a valid index.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
