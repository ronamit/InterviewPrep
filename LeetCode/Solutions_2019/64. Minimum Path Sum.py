
def minPathSum(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    m = len(grid)
    if m == 0:
        return 0
    n = len(grid[0])
    inf_val =  max([max(a) for a in grid]) + 1
    V = [[None for _ in range(n)] for _ in range(m)]
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            a = grid[i][j]
            pathVals = []
            if i == m -1 and j == n-1:
                pathVals = [a]
            else:
                if i < m-1:
                    pathVals += [a + V[i+1][j]]
                if j < n - 1:
                    pathVals += [a + V[i][j+1]]
            V[i][j] = min(pathVals)
    return V[0][0]


self = None
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(minPathSum(self, grid))
#
#
# def minPathSum(self, grid):
#     """
#     :type grid: List[List[int]]
#     :rtype: int
#     """
#     from heapq import heappop, heappush
#     m = len(grid)
#     if m == 0:
#         return 0
#     n = len(grid[0])
#     inf_val = max([max(a) for a in grid]) + 100
#     heap = []
#     for i in range(m):
#         for j in range(n):
#             if (i == j == 0):
#                 continue
#             heappush(heap, (inf_val, i, j))
#
#     p = (0, 0)
#     while heap:
#         # find neigbours:
#         neig = []
#         if p[0] < m - 1:
#             neig += [(p[0] + 1, p[1])]
#         if p[1] < n - 1:
#             neig += [(p[0], p[1] + 1)]
#
#         # relaxation for neighbours of p:
#         for i, j in neig:
#
#
# self = None