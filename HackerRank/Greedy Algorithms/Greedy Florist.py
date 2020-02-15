#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    # the stratedgy: start with high and go down, each friend buys one at his turn
    c.sort(reverse=True)
    min_price = 0
    for i in range(n):
        # previous purchases made by current buyer
        purchases_made =   i // k
        min_price += (1 + purchases_made) * c[i]
    return min_price


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
