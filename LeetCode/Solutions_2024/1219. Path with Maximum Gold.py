from typing import List

class Solution:
    
    def getMaximumGold(self, grid: List[List[int]]) -> int:
            m = len(grid)
            n = len(grid[0])

            def max_gold_from_start(i, j):
                # max possible gold starting from i,j, andwhen already visited some cells
                if i < 0 or i >= m or j < 0 or j >= n:
                    return 0
                if grid[i][j] == 0:
                    return 0
                max_gold_from_path = 0
                cur_gold = grid[i][j]
                # set (i,j) to have zero gold, so we don't visit it again in this path:
                grid[i][j] = 0
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    gold_from_path = max_gold_from_start(i + di, j + dj)
                    max_gold_from_path = max(max_gold_from_path, gold_from_path)
                # set (i,j) back to have cur_gold gold:
                grid[i][j] = cur_gold
                return max_gold_from_path + cur_gold

            # go over all non-zero cells as starting points:
            max_gold = 0
            for i in range(m):
                for j in range(n):
                    max_gold = max(max_gold, max_gold_from_start(i, j))
            return max_gold
