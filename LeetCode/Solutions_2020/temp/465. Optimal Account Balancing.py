from typing import List, Dict, Tuple, Sequence
import itertools

# https://leetcode.com/problems/optimal-account-balancing/

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:

        # check balance for each person

        # while not all balanced
        # run DFS starting from the most postive (gets back most) - x
        # Run DFS to find all edges connected to x
        # all the negative - tranfer to x, starting from most negatrive
        # until settled


