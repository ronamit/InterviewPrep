from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def is_closed_dfs(x, y):
            nonlocal grid 
            # always started on 0 cell (not visited land)
            ans = True
            grid[x][y] = -1 # mark visited
            for (dx, dy) in [(-1,0), (1,0), (0,1), (0,-1)]:
                x2 = x + dx
                y2 = y + dy
                if (x2 < 0 or x2 >= m or y2 < 0 or y2 >= n):
                    # the land cell is near border - all the island is not closed
                    ans = False
                elif grid[x2][y2] != 0:
                    # already visited or water
                    continue
                else: # 0 cell
                    ans = ans and is_closed_dfs(x2, y2)
            return ans
            

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    # if water or visited
                    continue
                is_closed = is_closed_dfs(i, j)
                # if closed - count it
                cnt += is_closed
        return cnt
                
        