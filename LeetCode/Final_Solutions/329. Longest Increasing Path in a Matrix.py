
def longestIncreasingPath(self, matrix: 'List[List[int]]') -> 'int':

    m = len(matrix)
    if m == 0: return 0
    n = len(matrix[0])
    # Do toplogical ordering:
    # note circle is not possible in this problem

    # First find in-degree of each node
    # and create a stack of nodes with 0-in degree (sources)
    sourcesStk = []
    inDeg = [[0] * n for i in range(m)]
    neigs = [(0,1), (0, -1), (1, 0), (-1, 0)]

    for i in range(m):
        for j in range(n):
            for dir in neigs:
                i2 = i+dir[0]
                j2 = j+dir[1]
                if 0 <= i2 < m and 0 <= j2 < n \
                        and matrix[i][j] > matrix[i2][j2]:
                    inDeg[i][j] += 1
            if inDeg[i][j] == 0:
                sourcesStk.append((i,j))

    ordered = []
    ordMat = [[0] * n for i in range(m)]
    curOrd = 0
    while sourcesStk:
        (i,j) = sourcesStk.pop()
        # add node to the oredered list
        ordered.append((i,j))
        ordMat[i][j] = curOrd
        curOrd += 1
        # remove node form graph - update in-deg of neighbours
        for dir in neigs:
            i2 = i + dir[0]
            j2 = j + dir[1]
            if 0 <= i2 < m and 0 <= j2 < n \
                    and matrix[i][j] < matrix[i2][j2]:
                inDeg[i2][j2] -= 1
                if inDeg[i2][j2] == 0:
                    sourcesStk.append((i2, j2))

    # Use Dynamic-Programming to find max path, when going according to ordering
    maxPath = [0 for _ in range(n*m)]
    totMax = 0
    for k in range(n*m-1, -1, -1):
        i,j = ordered[k]
        maxNext = 0
        for dir in neigs:
            i2 = i + dir[0]
            j2 = j + dir[1]
            if 0 <= i2 < m and 0 <= j2 < n  \
                    and matrix[i][j] < matrix[i2][j2]:
                maxNext = max(maxNext, maxPath[ordMat[i2][j2]])
        maxPath[k] = 1 + maxNext
        totMax = max(totMax, maxPath[k])

    return totMax



self = None
matrix = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
print(longestIncreasingPath(self, matrix))