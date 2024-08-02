class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        # we can look at the problem as a graph - and check what coords can get to both oceans.
        # start a DFS search from each (not yet visited) (i,j) and check which oceasns are reachable
        
        # TODO: more efficient - start from ocean tiles.
        m = len(heights)
        n = len(heights[0])

        def neighbors(i: int, j: int):
            # get all tiles that we can flow to
            nonlocal heights, m, n
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                i2 = i + di
                j2 = j + dj
                if 0 <= i2 < m and 0 <= j2 < n and heights[i2][j2] <= heights[i][j]:
                    yield i2, j2

        def dfs(i: int, j: int) -> tuple[bool]:
            nonlocal m, n, visited
            visited.add((i, j))
            can_pacf = (i == 0) or (j == 0)
            can_atl = (i == (m - 1)) or (j == (n - 1))
            for i2, j2 in neighbors(i, j):
                if (i2, j2) in visited:
                    continue
                can_pacf2, can_atl2 = dfs(i2, j2)
                can_pacf = can_pacf or can_pacf2
                can_atl = can_atl or can_atl2
            return can_pacf, can_atl

        answer = []
        for i in range(m):
            for j in range(n):
                visited = set()
                can_pacf, can_atl = dfs(i, j)
                if can_pacf and can_atl:
                    answer.append([i, j])
        return answer
