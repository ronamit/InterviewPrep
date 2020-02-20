class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        paths = [[0 for _ in range(n)] for _ in range(m)]
        paths[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if j > 0:
                        paths[i][j] += paths[i][j - 1]
                    if i > 0:
                        paths[i][j] += paths[i - 1][j]
        return paths[m - 1][n - 1]

