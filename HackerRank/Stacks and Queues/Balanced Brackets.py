#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stk = []
    for c in s:
        if c in ['(', '[', '{']:
            stk.append(c)
        else:
            if not stk:
                return 'NO'
            op_cand = stk.pop()
            if (op_cand, c) not in [ ('(', ')'), ('[', ']'), ('{', '}')]:
                return 'NO'
    if len(stk) == 0:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
