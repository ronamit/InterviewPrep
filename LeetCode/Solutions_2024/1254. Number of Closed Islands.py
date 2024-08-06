class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        # find connected components with DFS

        def neighbors(i: int, j: int):
            nonlocal m, n, grid
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ii = i + di
                jj = j + dj
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == 0:
                    yield (ii, jj)

        def dfs_is_closed(i: int, j: int):
            nonlocal m, n, grid, visited
            visited.add((i, j))
            is_closed = (i > 0) and (i  < m - 1) and (j > 0) and (j < n - 1)
            for ii, jj in neighbors(i, j):
                if (ii, jj) not in visited:
                    # note: we must continue to DFS even if is_closed == False already, so we cover all the connected component in the DFS run
                    is_neigh_closed = dfs_is_closed(ii, jj)
                    is_closed = is_closed and is_neigh_closed
            return is_closed

        ans = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == 0:
                    ans += dfs_is_closed(i, j)
        return ans


if __name__ == "__main__":
    gird = [
        [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
        [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 0],
    ]
    print(Solution().closedIsland(gird))
