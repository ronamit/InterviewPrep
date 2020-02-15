#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    n = len(arr)
    V = [0 for _ in range(n)]
    V[n-1] = max(arr[n-1], 0)
    for i in range(n-2, -1, -1):
        if i == n-2:
            V[i] = max(arr[i], V[i+1])
        else:
            V[i] = max(arr[i]+V[i+2], V[i+1])
    return max(V)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
