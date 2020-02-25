from typing import List, Dict, Tuple, Sequence
import itertools, collections



class Solution:
    def superEggDrop(self, K: int, N: int) -> int:

        def NumDrops(k, n, T):
            # k eggs, n floors
            if n <= 0:
                return 0
            elif k <= 0:
                return float('inf')
            elif T[k][n] is not None:
                return T[k][n]
            min_drops = float('inf')
            for dropFloor in range(1, n + 1):
                if T[k][n-1] is not None:
                    dropsNextNotBreaks = T[k][n-1]
                else:
                    dropsNextNotBreaks = NumDrops(k, dropFloor-1, T)
                if T[k-1][n-dropFloor] is not None:
                    dropsNextBreaks = T[k-1][n-dropFloor]
                else:
                    dropsNextBreaks = NumDrops(k-1, n - dropFloor, T)
                drops_next = max(dropsNextNotBreaks, dropsNextBreaks)
                min_drops = min(min_drops, 1 + drops_next)
            T[k][n] = min_drops
            return min_drops

        # table for completed results:
        T = [[None for _ in range(N+1)] for _ in range(K+1)]
        return NumDrops(K, N, T)

sol = Solution()
print(sol.superEggDrop(K=1,N=5))