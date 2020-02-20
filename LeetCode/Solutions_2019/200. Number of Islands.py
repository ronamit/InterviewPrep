
def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    n = len(grid)
    if n == 0:
        return 0
    m = len(grid[0])
    if m == 0:
        return 0
    grid = [[int(a) for a in row] for row in grid]
    count = 2
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0 or grid[i][j] > 1:
                continue
            # Run DFS on nodes which were not yet visited:
            neig = [(i,j)]
            while neig != []:
                p = neig.pop()
                r = p[0]
                c = p[1]
                grid[r][c] = count
                if r < n - 1 and grid[r+1][c] == 1:
                    neig += [(r+1, c)]
                if r > 0 and grid[r-1][c] == 1:
                    neig += [(r-1, c)]
                if c < m - 1 and grid[r][c+1] == 1:
                    neig += [(r, c+1)]
                if c > 0 and grid[r][c-1] == 1:
                    neig += [(r, c - 1)]
            count += 1
    # print(grid)
    n_islands = max([max(row) for row in grid]) - 1
    n_islands = max(n_islands, 0)
    return n_islands

self = None
grid = [["1","1","1"],["0","1","0"],["1","1","1"]]
print(numIslands(self, grid))

