"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1


Constraints:
1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""

from loguru import logger
from typing import List
from collections import Counter


def single_number(nums: List[int]) -> List[int]:
    freq = Counter(nums)
    result = [num for num, count in freq.items() if count % 2 != 0]

    return result


"""
Using `Counter`:
   - The `Counter` counts the occurrences of each element in the list.
   - we iterate over the key-value pairs to check which element has exactly one occurrence.
   - If we find more than one element with one occurrence, we return `-1`.

Complexity:
- Time Complexity:
  - Creating the `Counter` takes (O(n)) because it iterates through the entire list once.
  - Iterating through the `Counter` items takes (O(k)), where (k) is the number of unique elements (potentially equal to (n) in the worst case).
  - Total time: (O(n) for creation + (O(k)) for iteration. In the worst case, (O(n + n) = O(n)).

- Space Complexity:
  - The `Counter` stores the count of every unique element, which takes (O(k)) space (could be (O(n)) in the worst case).

  

- The key challenge is reducing space usage. `Counter` keeps extra data in memory, which makes it inefficient for "constant space" requirements.
- XOR eliminates the need to track counts.


XOR : is valid only when the each duplicate element only appears twice.

"""


def single_number_xor(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result


"""
When elements appear arbitrarily many times (e.g., three times, four times, etc.), XOR alone won't work. we will need to use bit-counting logic.

Modified Problem: Find the Unique Number When All Others Appear Thrice (or any arbitrary `k` times)
For [1, 1, 2, 3, 2, 3, 1]:

Count how many times each bit is set to 1 across all numbers.
If a bit’s count is not divisible by 3, it belongs to the unique number.
"""


def single_number_k_times(nums: List[int], k: int) -> int:
    """
    Creates a list bit_count with 32 zeros, one for each possible bit position in a 32-bit integer.
    We’ll use this list to count how many times each bit position is set to 1 across all numbers.
    """
    bits_count = [0] * 32

    """For each bit position i: Extract the 𝑖i-th bit:(num >> i) shifts the number num right by i positions so that the 𝑖 i-th bit becomes the least significant bit (rightmost). & 1 checks if the least significant bit is 1. Update the count: bit_count[i] is incremented by 1 if the  𝑖 i-th bit is 1."""

    for num in nums:
        for i in range(32):
            bits_count[i] += (num >> i) & 1

    result = 0
    """(1 << i) shifts 1 left by i positions, creating a mask with only the  𝑖 i-th bit set (e.g., for 𝑖 = 2  i=2, it’s 100).  result |= (1 << i) sets the   𝑖  i-th bit in result."""
    for i in range(32):
        if bits_count[i] % k != 0:
            result |= 1 << i

    return result


def main() -> None:
    logger.info("Starting the Application.")
    options = """
    Select an option:
    1. Find the single number (duplicates appear twice except one element).
    2. Find the single number when duplicates appear k times.
    """
    print(options)
    option = input("Enter your choice (1 or 2): ").strip()

    if option == "1":
        constraints = """
        1. Input should be a space-separated array of integers.
        2. Each element in the array appears twice except for one element.
        """
        print(constraints)
        nums = input("Enter the numbers: ").strip()
        try:
            nums = [int(x) for x in nums.split()]
            result = single_number_xor(nums)
            logger.info(f"Single number is: {result}")
        except ValueError:
            logger.error("Invalid input. Please enter integers only.")

    elif option == "2":
        constraints = """
        1. Input should be a space-separated array of integers.
        2. Specify how many times elements are repeated (k).
        """
        print(constraints)
        nums = input("Enter the numbers: ").strip()
        k = input("Enter the value of k: ").strip()
        try:
            nums = [int(x) for x in nums.split()]
            k = int(k)
            result = single_number_k_times(nums, k)
            logger.info(f"Single number is: {result}")
        except ValueError:
            logger.error("Invalid input. Please enter integers only.")

    else:
        logger.error("Invalid option. Please select 1 or 2.")


if __name__ == "__main__":
    main()
