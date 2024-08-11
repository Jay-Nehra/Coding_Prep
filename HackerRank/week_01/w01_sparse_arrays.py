#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#


def matchingStrings(strings, queries):
    query_freq = [0] * len(queries)

    for i, q in enumerate(queries):
        for s in strings:
            if q == s:
                query_freq[i] += 1

    return query_freq


def matchingStrings_2(strings, queries):
    string_freq = {}

    for s in strings:
        if s in string_freq:
            string_freq[s] += 1
        else:
            string_freq[s] = 1

    query_freq = []
    for q in queries:
        query_freq.append(string_freq.get(q, 0))

    return query_freq


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings_2(strings, queries)

    fptr.write("\n".join(map(str, res)))
    fptr.write("\n")

    fptr.close()
