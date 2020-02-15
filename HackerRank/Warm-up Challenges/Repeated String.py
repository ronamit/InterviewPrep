#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    a_count_s = 0
    for c in s:
        if c == 'a':
            a_count_s += 1
    res_len = n % len(s)
    a_count_all = (n // len(s)) * a_count_s
    for i in range(res_len):
        if s[i] == 'a':
            a_count_all += 1
    return a_count_all

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
