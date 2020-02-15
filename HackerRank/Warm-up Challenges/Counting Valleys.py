#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    h = 0
    count = 0
    for i in range(n):
        prev_h = h
        if s[i] == 'U':
            h += 1
        else:
            h -= 1
        if h < 0 and prev_h >= 0:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
