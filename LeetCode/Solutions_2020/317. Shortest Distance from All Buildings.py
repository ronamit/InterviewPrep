from typing import List, Dict, Tuple, Sequence
import itertools, collections


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def neig(i,j):
            for (i2,j2) in [(i-1,j),(i+1,j),(i,j-1), (i,j+1)]:
                if 0<=i2<=n-1 and 0<=j2<=m-1 and grid[i2][j2] == 0:
                    yield (i2,j2)

        # Find buildings

        total_dist = [[0 for _ in range(m)] for _ in range(n)]
        reached_count =  [[0 for _ in range(m)] for _ in range(n)]

        buildings = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    buildings.append((i,j))

        n_buildings = len(buildings)
        # Run BFS from each building + accumulate dist to building
        for (i,j) in buildings:
            d = 0
            q = collections.deque([(i,j,d)])
            visited = [[False for _ in range(m)] for _ in range(n)]
            visited[i][j] = True
            while q:
                (i,j,d) = q.popleft()
                d += 1
                for (i2, j2) in neig(i,j):
                    if visited[i2][j2]:
                        continue # already visited
                    visited[i2][j2] = True
                    total_dist[i2][j2] += d
                    reached_count[i2][j2] += 1
                    q.append((i2,j2,d))

        best = float('inf')
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    continue
                if reached_count[i][j] < n_buildings:
                    # this spot not reached from all buildings
                    continue
                best = min(best, total_dist[i][j])

        if best == float('inf'):
            # means no empty places
            best = -1
        return best


grid = [[1,1,1,1,1,0],[0,0,0,0,0,1],[0,1,1,0,0,1],[1,0,0,1,0,1],[1,0,1,0,0,1],[1,0,0,0,0,1],[0,1,1,1,1,0]]
sol = Solution()
print(sol.shortestDistance(grid))