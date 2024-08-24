from collections import deque


class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        # the queue contains (i,j, min_elimnation_to_here, dist_to_here)
        queue = deque([(0, 0, 0, 0)])

        # dict of (i,j): min_elimnation_to_here
        min_elim_to_each = {(0, 0): 0}
        min_dist_to_each = {(0, 0): 0}
        while queue:
            i1, j1, min_elim_to_1, dist_to_1 = queue.pop()

            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                i2 = i1 + di
                j2 = j1 + dj
                if not (0 <= i2 < m and 0 <= j2 < n):
                    continue
                min_elim_to_2 = min_elim_to_1 + grid[i2][j2]
                dist_to_2 = dist_to_1 + 1
                if min_elim_to_2 > k:
                    continue
                if (i2, j2) not in min_dist_to_each:
                    min_dist_to_each[(i2, j2)] = dist_to_2
                else:
                    min_dist_to_each[(i2, j2)] = min(
                        min_dist_to_each[(i2, j2)],
                        dist_to_2,
                    )
                if (i2, j2) not in min_elim_to_each or min_elim_to_each[(i2, j2)] > min_elim_to_2:
                    min_elim_to_each[(i2, j2)] = min_elim_to_2
                    queue.appendleft((i2, j2, min_elim_to_2, dist_to_2))
        return min_dist_to_each.get((m - 1, n - 1), -1)
