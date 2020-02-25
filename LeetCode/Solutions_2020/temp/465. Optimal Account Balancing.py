from typing import List, Dict, Tuple, Sequence
import itertools, collections

# https://leetcode.com/problems/optimal-account-balancing/

def update_balance(balances, a, update):
    if a not in balances.keys():
        balances[a] = update
    else:
        balances[a] += update

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:

        # check balance for each person
        balances = {}
        for (a,b, money) in transactions:
            update_balance(balances, a, -money)
            update_balance(balances, b, +money)

        pass

        # while not all balanced
        debts = [[a, balances[a]] for a in balances.keys() if balances[a] != 0]

        def min_trans_rec(debts):
            n_debts = len(debts)
            positives = [i for i in range(n_debts) if debts[i][1] > 0]
            negatives = [i for i in range(n_debts) if debts[i][1] < 0]
            min_trans = float('inf')
            if len(positives) == 0:
                return 0
            for ia in positives:
                for ib in negatives:
                    # try a -> b
                    b_gets = debts[ib][1]
                    debts[ia][1] += b_gets
                    debts[ib][1] = 0
                    min_trans = min(min_trans, 1 + min_trans_rec(debts))
                    # shift array back (backtrack)
                    debts[ia][1] -= b_gets
                    debts[ib][1] = b_gets

            return min_trans

        return  min_trans_rec(debts)








        # debts.sort(key=lambda pair: pair[1])
        #
        # n_debts = len(debts)
        # i = 0
        # j = n_debts - 1
        # n_trans = 0
        # while j >= i:
        #     print(debts)
        #     if debts[i][1] == 0:
        #         i += 1
        #     elif debts[j][1] == 0:
        #         j -= 1
        #     elif -debts[i][1] > debts[j][1]:
        #         n_trans += 1
        #         debts[i][1] += debts[j][1]
        #         debts[j][1] = 0
        #         j -= 1
        #     else:
        #         n_trans += 1
        #         debts[j][1] += debts[i][1]
        #         debts[i][1] = 0
        #         i += 1
        # return n_trans



        # run DFS starting from the most postive (gets back most) - x
        # Run DFS to find all edges connected to x
        # all the negative - tranfer to x, starting from most negatrive
        # until settled


transactions = [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
# transactions = [[1,5,8],[8,9,8],[2,3,9],[4,3,1]]
sol = Solution()
print(sol.minTransfers(transactions))