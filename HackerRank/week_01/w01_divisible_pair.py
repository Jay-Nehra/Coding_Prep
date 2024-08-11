#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'divisibleSumPairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY ar
#


def divisibleSumPairs(n, k, ar):
    # Write your code here
    total_pair = 0
    for i, a in enumerate(ar):
        for j in range(i + 1, n):
            obj = a + ar[j]
            total_pair = total_pair + 1 if obj % k == 0 else total_pair

    return total_pair


def divisibleSumPairs_optimized(n, k, ar):
    freq_remainder = [0] * k

    for num in ar:
        remainder = num % k
        freq_remainder[remainder] += 1

    total_pair = 0
    total_pair += (freq_remainder[0] * (freq_remainder[0] - 1)) // 2
    for i in range(1, (k // 2) + 1):
        if i != k - i:
            total_pair += freq_remainder[i] * freq_remainder[k - i]

    # If k is even, handle the middle remainder
    if k % 2 == 0:
        total_pair += (freq_remainder[k // 2] * (freq_remainder[k // 2] - 1)) // 2

    return total_pair


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs_optimized(n, k, ar)

    fptr.write(str(result) + "\n")

    fptr.close()
