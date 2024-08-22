from collections import deque


class Solution:
    def wallsAndGates(self, rooms: list[list[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # use multi-source BFS

        m = len(rooms)
        n = len(rooms[0])

        # add  all gates locations to starting queue
        queue = deque()
        visited = set()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.appendleft((i, j, 0))  # (row, col, min_dist_to_gate)
                    visited.add((i, j))
        EMPTY_ROOM = 2147483647
        while queue:
            i, j, dist = queue.pop()
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                i2 = i + di
                j2 = j + dj
                if (0 <= i2 < m) and (0 <= j2 < n) and (i2, j2) not in visited and rooms[i2][j2] == EMPTY_ROOM:
                    visited.add((i2, j2))
                    queue.appendleft((i2, j2, dist + 1))
                    rooms[i2][j2] = dist + 1
