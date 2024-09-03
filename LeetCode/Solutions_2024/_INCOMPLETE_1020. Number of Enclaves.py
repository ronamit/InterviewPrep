class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        ans = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or (i, j) in visited:
                    continue
                is_enclave = True
                component_size = 0
                # DFS
                stack = [(i, j)]
                visited = {(i, j)}
                while stack:
                    (i1, j1) = stack.pop()
                    component_size += 1
                    is_enclave = is_enclave and 0 < i1 < (m - 1) and 0 < j1 < (n - 1)
                    for (di, dj) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        i2 = i1 + di
                        j2 = j1 + dj
                        if (not 0 <= i2 < m) or (not 0 <= j2 < n) or (grid[i2][j2] == 0) or ((i2, j2) in visited):
                            continue
                        visited.add((i2, j2))
                        stack.append((i2, j2))
                # finished scan of the connected component
                ans += is_enclave * component_size
        return ans


if __name__ == "__main__":
    grid = [[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    print(Solution().numEnclaves(grid))
