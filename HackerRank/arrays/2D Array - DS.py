#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    n = len(arr)
    if n == 0: return 0
    m = len(arr[0])
    max_s = None
    for i in range(1,n-1):
        for j in range(1,m-1):
            s = arr[i][j] + arr[i-1][j-1] + arr[i-1][j] +  arr[i-1][j+1] +  arr[i+1][j-1] + arr[i+1][j] +  arr[i+1][j+1]
            if max_s is None:
                max_s = s
            else:
                max_s = max(max_s, s)
    return max_s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
