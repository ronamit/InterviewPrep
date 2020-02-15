#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    m_d = {}
    for c in magazine:
        if c not in m_d:
            m_d[c] = 0
        m_d[c] += 1
    n_d = {}
    for c in note:
        if c not in n_d:
            n_d[c] = 0
        n_d[c] += 1
    for c in n_d:
        if c not in m_d or m_d[c] < n_d[c]:
            print('No')
            return
    print('Yes')


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
