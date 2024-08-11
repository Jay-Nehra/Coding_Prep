#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def lonelyinteger(a):
    # Write your code here
    ele_freq = {}
    for ele in a:
        if ele in ele_freq:
            ele_freq[ele] += 1
        else:
            ele_freq[ele] = 1

    value_to_find = 1
    key_with_value = None
    for key, value in ele_freq.items():
        if value == value_to_find:
            key_with_value = key
            return key_with_value


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + "\n")

    fptr.close()
