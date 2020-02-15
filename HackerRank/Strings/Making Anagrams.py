#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    diff_count = {}
    for char in a:
        if not char in diff_count:
            diff_count[char] = 0
        diff_count[char] += 1
    for char in b:
        if not char in diff_count:
            diff_count[char] = 0
        diff_count[char] -= 1
    ans = 0
    for char in diff_count:
        ans += abs(diff_count[char])
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
