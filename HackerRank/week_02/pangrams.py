#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def pangrams(user_input):

    # alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
    # user_input = user_input.lower()
    # return 'pangram' if alphabet_set <= set(user_input) else 'not pangram'

    alphabet = [0] * 26
    for s in user_input.lower():
        if "a" <= s <= "z":
            alphabet[ord(s) - ord("a")] = 1

    return "not pangram" if 0 in alphabet else "pangram"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = pangrams(s)

    fptr.write(result + "\n")

    fptr.close()
