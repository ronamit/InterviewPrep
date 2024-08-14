from collections import deque


class Solution:

    def neighbors(self, grid, i: int, j: int):
        n = len(grid)
        for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ii = i + di
            jj = j + dj
            if 0 <= ii < n and 0 <= jj < n and grid[ii][jj] == 0:
                yield (ii, jj)

    def is_path(self, grid: list[list[int]]) -> bool:
        # check if there is a path with only zeros from (0,0) to (n-1,n-1)
        if grid[0][0] == 1:
            return False
        n = len(grid)
        # BFS
        q = deque([(0, 0)])
        visited = set()
        while q:
            i, j = q.pop()
            for ii, jj in self.neighbors(grid, i, j):
                if (ii, jj) in visited:
                    continue
                if (ii, jj) == (n - 1, n - 1):
                    return True
                q.appendleft((ii, jj))
                visited.add((ii, jj))
        return False

    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        d = -1
        edge_cells = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
        # TODO: replace the linear scan with binary search, instead of changing the grid, say that a valid neighbor is that with dist >= d
        # after doing an initial BFS on the grid to set all the dists from thieves
        while d < n:
            d += 1
            if self.is_path(grid) is False:
                return d
            new_edge_cells = []
            for i, j in edge_cells:
                for ii, jj in self.neighbors(grid, i, j):
                    grid[ii][jj] = 1
                    new_edge_cells.append((ii, jj))
            edge_cells = new_edge_cells
        return d


if __name__ == "__main__":
    sol = Solution()
    grid = [[0, 0, 1], [0, 0, 0], [0, 0, 0]]
    print(sol.maximumSafenessFactor(grid))
