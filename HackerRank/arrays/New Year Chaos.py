#!/bin/python3

import math
import os
import random
import re
import sys

#TODO: see linear time  solution

# Complete the minimumBribes function below.
def minimumBribes(q):
    n = len(q)

    for i in range(n):
        if q[i] - (i + 1) > 2:
            print('Too chaotic')
            return

    n_swaps = 0
    for i in range(n):
        no_swaps = True
        for j in range(n-1,i,-1):
            if q[j-1] > q[j]:
                q[j - 1], q[j] = q[j], q[j-1]
                n_swaps += 1
                no_swaps = False
        if no_swaps:
            break
    print(n_swaps)
    return

if __name__ == '__main__':
    q = [2, 1, 5, 3, 4]

    minimumBribes(q)
