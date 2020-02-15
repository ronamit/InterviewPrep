
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m== 0: return 0
        n = len(grid[0])

        def getArea(grid, i, j):
            dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            area = 0
            stk = [(i, j)]
            while stk:
                i0, j0 = stk.pop()
                if grid[i0][j0] == 2:
                    continue
                grid[i0][j0] = 2  # visited
                area += 1
                for dir in dirs:
                    i1, j1 = i0 + dir[0], j0 + dir[1]
                    if 0 <= i1 < m and 0 <= j1 < n and grid[i1][j1] == 1:
                        stk.append((i1, j1))
            return area

        maxArea = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:  # land not visited
                    area = getArea(grid, i, j)
                    maxArea = max(maxArea, area)
        return maxArea

