from functools import cache


class Solution:

    def isThereAPath(self, grid: list[list[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        @cache
        def is_path(s_i: int, s_j: int, path_balance: int) -> bool:
            # check if there is a path from (s_i, s_j) to (m-1,n-1) with (num ones - num zeros in path) == path_balance
            nonlocal grid, n, m
            if grid[s_i][s_j] == 1:
                path_balance += 1
            else:
                path_balance -= 1
            if s_i == m - 1 and s_j == n - 1:
                return path_balance == 0
            for i, j in [(s_i + 1, s_j), (s_i, s_j + 1)]:
                if not (0 <= i < m and 0 <= j < n):
                    continue
                if grid[i][j] == -1:
                    continue
                if is_path(i, j, path_balance):
                    return True
            return False

        return is_path(0, 0, 0)
