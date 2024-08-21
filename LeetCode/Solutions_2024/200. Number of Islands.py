from collections import deque


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def neighbors(row1: int, col1: int):
            nonlocal grid, m, n
            for d_row, d_col in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                row2 = row1 + d_row
                col2 = col1 + d_col
                if 0 <= row2 < m and 0 <= col2 < n and grid[row2][col2] == "1":
                    yield row2, col2

        def bfs_scan(row: int, col: int):
            nonlocal grid, m, n, visited
            queue = deque([(row, col)])
            while queue:
                row1, col1 = queue.pop()
                visited.add((row1, col1))
                for row2, col2 in neighbors(row1, col1):
                    if (row2, col2) not in visited:
                        queue.append((row2, col2))

        visited = set()
        n_islands = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "0" or (row, col) in visited:
                    continue
                n_islands += 1
                bfs_scan(row, col)
        return n_islands


if __name__ == "__main__":
    sol = Solution()
    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    print(sol.numIslands(grid))
