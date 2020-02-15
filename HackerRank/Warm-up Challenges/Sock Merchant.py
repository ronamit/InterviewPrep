#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    colors_counts = {}
    for color in ar:
        if color in colors_counts:
            colors_counts[color] += 1
        else:
            colors_counts[color] = 1
    pair_count = 0
    for col_count in colors_counts.values():
        pair_count += col_count // 2
    return pair_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
