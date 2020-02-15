def maxRegion(grid):
    n = len(grid)
    m = len(grid[0])
    count = 0
    max_size = 0
    cur_size = 0
    dirs = [(-1,0), (1,0), (0,1), (0,-1), (1,1), (1, -1), (-1,1), (-1,-1)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                cur_size = 0
                count += 1
                s = [(i,j)]# stack
                while s:
                    (i1, j1) = s.pop()
                    if grid[i1][j1] == 2:
                        continue # already visited
                    cur_size += 1
                    grid[i1][j1] = 2 # mark visited
                    for dir in dirs:
                        i2 = i1 + dir[0]
                        j2 = j1 + dir[1]
                        if (0 <= i2 <= n-1) and (0 <= j2 <= m-1) \
                                and grid[i2][j2] == 1:  # if new
                            s.append((i2, j2))
            max_size = max(max_size, cur_size)
    return max_size


grid = [[1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 0]]
print( maxRegion(grid))