from typing import List, Dict, Tuple, Sequence
import itertools, collections

class Solution:
    def minWindow(self, S: str, T: str) -> str:
        S_len = len(S)
        T_len = len(T)
        def minWindowRec(S_start, T_start):
            if S_start >= S_len:
                return 0, float('inf')
            if T_start >= T_len:
                return 0, 0
            Win_start = S_start
            W = float('inf')
            for i in range(S_start, S_len):
                # we for reverse with i so we get the leftmost solution
                if S[i] == T[T_start]:
                    start_n, w_n = minWindowRec(i+1, T_start+1)
                    if (1 + w_n) < W:
                        W = 1 + w_n
                        Win_start = i
            return Win_start, W

        start, W = minWindowRec(0, 0)
        if W == float('inf'):
            return ""
        else:
            return S[start:start+W]


S = "abcdebdde"
T = "bde"
# S =  "jmeqksfrsdcmsiwvaovztaqenprpvnbstl"
# T = "k"
sol = Solution()
print(sol.minWindow(S,T))