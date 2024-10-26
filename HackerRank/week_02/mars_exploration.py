#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def marsExploration(s):
    count = 0
    sos = "SOS"

    for i in range(0, len(s), 3):
        for j in range(3):
            if s[i + j] != sos[j]:
                count += 1

    return count


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()
    result = marsExploration(s)

    fptr.write(str(result) + "\n")

    fptr.close()
