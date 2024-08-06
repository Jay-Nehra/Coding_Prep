#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    n_bin = bin(n)[2:]
    n_32bit = n_bin.zfill(32)
    flipped_bits = ['0' if bit == '1' else '1' for bit in n_32bit]
    flipped_binary_string = ''.join(flipped_bits)
        
    return int(flipped_binary_string, 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
