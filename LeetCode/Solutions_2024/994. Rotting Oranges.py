import math
from collections import deque


class Solution:

    def orangesRotting(self, grid: list[list[int]]) -> int:
        # Run BFS from eech fresh orange, mark the rotting times
        m = len(grid)
        n = len(grid[0])

        def fresh_neighbors(i1: int, j1: int, t1: int):
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                i2 = i1 + di
                j2 = j1 + dj
                if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] == 1:
                    yield (i2, j2, t1 + 1)

        # dict that holds for any fresh orange the time it took for it to rot
        rot_time = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rot_time[(i, j)] = math.inf
                elif grid[i][j] == 2:
                    rot_time[(i, j)] = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 2:
                    continue
                # Start BFS from a rotten orange:
                q = deque([(i, j, 0)])
                visited = set()
                while q:
                    i1, j1, t1 = q.pop()
                    # mark the earliest time as rotting time
                    rot_time[(i1, j1)] = min(t1, rot_time[(i1, j1)])
                    for i2, j2, t2 in fresh_neighbors(i1, j1, t1):
                        if (i2, j2) not in visited:
                            q.appendleft((i2, j2, t2))
                    visited.add((i1, j1))
        if len(rot_time) == 0:
            return 0  # no fresh oranges
        # check if any remaining fresh oranges:
        max_t = max(rot_time.values())
        if max_t == math.inf:
            return -1
        return max_t
