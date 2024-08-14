import heapq
from collections import deque


class Solution:

    def set_dists_from_thieves(self, grid: list[list[int]]):
        # Set in the grid:  distance from closest thief (thieves will have value zero)
        # use multi-source BFS

        n = len(grid)
        # find all thieves positions
        thieves_pos = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
        # The items in the queue are (i,j, min_dist_from_thief)
        q = deque([(i, j, 0) for (i, j) in thieves_pos])
        visited = set(thieves_pos)
        while q:
            i, j, dist = q.pop()
            grid[i][j] = dist
            for ii, jj in self.neighbors(i, j, n):
                if (ii, jj) in visited:
                    continue
                visited.add((ii, jj))
                q.appendleft((ii, jj, dist + 1))

    def neighbors(self, i: int, j: int, n: int):
        for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ii = i + di
            jj = j + dj
            if 0 <= ii < n and 0 <= jj < n:
                yield (ii, jj)

    def is_path_with_safety_factor(self, grid: list[list[int]], safe_fac: int) -> bool:
        # check if there is a path with only dists >= safe_fac
        if grid[0][0] < safe_fac:
            print(f"No path with safety factor {safe_fac}")
            return False
        n = len(grid)
        # BFS
        q = deque([(0, 0)])
        visited = set()
        while q:
            i, j = q.pop()
            for ii, jj in self.neighbors(i, j, n):
                if grid[ii][jj] < safe_fac:
                    # can't pass in cells with min dist to thief < safe_fac
                    continue
                if (ii, jj) in visited:
                    continue
                if (ii, jj) == (n - 1, n - 1):
                    print(f"Found path with safety factor {safe_fac}")
                    return True
                q.appendleft((ii, jj))
                visited.add((ii, jj))
        print(f"No path with safety factor {safe_fac}")
        return False

    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        self.set_dists_from_thieves(grid)
        print("Dists from thieves \n", grid)

        # find the the highest safety factor, where there is still a a path
        # use bisect
        lo = 0
        hi = n
        ans = 0
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            print(f"lo {lo}, hi {hi}, mid {mid}")
            if self.is_path_with_safety_factor(grid=grid, safe_fac=mid):
                ans = max(ans, mid)
                lo = mid + 1
            else:
                hi = mid - 1
        return ans

    def maximumSafenessFactor_DIJKSTRA(self, grid: list[list[int]]) -> int:
        n = len(grid)
        self.set_dists_from_thieves(grid)
        print("Dists from thieves \n", grid)

        # Dijkstra algorithm variant.
        # Each node weight is minus the dist to closest thief
        # we want a path from (0,0) that has minimal weighted path to (n-1,n-1), where path weight = (max over the nodes along the path)

        min_weight_to_cell = [[float("inf") for _ in range(n)] for _ in range(n)]
        min_weight_to_cell[0][0] = -grid[0][0]
        h = [(-grid[0][0], 0, 0)] + [(float("inf"), i, j) for i in range(n) for j in range(n)]
        heapq.heapify(h)
        visited = set()
        while h:
            min_to_cur, i, j = heapq.heappop(h)
            if (i, j) == (n - 1, n - 1):
                return -min_weight_to_cell[-1][-1]
            if (i, j) in visited:
                continue
            visited.add((i, j))
            for ii, jj in self.neighbors(i, j, n):
                # check if we can improve the min dist path to (ii,jj) through (i,j)
                old_val = min_weight_to_cell[ii][jj]
                tentative_val = max(min_to_cur, -grid[ii][jj])
                if tentative_val < old_val:
                    min_weight_to_cell[ii][jj] = tentative_val
                    heapq.heappush(h, (tentative_val, ii, jj))
                    # note: we don't need to worry that (ii, jj, old_val) will be poped. since (tentative_val, ii, jj) will be poped first and mark (ii, jj) as visited
        return -min_weight_to_cell[-1][-1]


if __name__ == "__main__":
    sol = Solution()
    grid = [[0, 0, 1], [0, 0, 0], [0, 0, 0]]
    print(sol.maximumSafenessFactor(grid))
