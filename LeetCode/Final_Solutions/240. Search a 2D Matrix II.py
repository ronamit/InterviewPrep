


def IsValidInds(matrix, i1, i2, j1, j2):
    m = len(matrix)
    n = len(matrix[0])
    if i1 > i2 or j1 > j2:
        return False
    for j in [j1, j2]:
        if j > n - 1 or j < 0:
            return False
    for i in [i1, i2]:
        if i > m - 1 or i < 0:
            return False
    return True

def SearchRow(matrix, target, i, j1, j2):
    if not IsValidInds(matrix, i, i, j1, j2):
        return False
    mid_j = (j1 + j2) // 2
    a = matrix[i][mid_j]
    if a == target:
        return True
    elif a > target:
        return SearchRow(matrix, target, i, j1, mid_j - 1)
    else:
        return SearchRow(matrix, target, i, mid_j+1, j2)


def SearchCol(matrix, target, i1, i2, j):
    m = len(matrix)
    n = len(matrix[0])
    if not IsValidInds(matrix, i1, i2, j, j):
        return False
    mid_i = (i1 + i2) // 2
    a = matrix[mid_i][j]
    if a == target:
        return True
    elif a > target:
        return SearchCol(matrix, target, i1, mid_i-1, j)
    else:
        return SearchCol(matrix, target, mid_i + 1, i2, j)


def Search(matrix, target, i1, i2, j1, j2):
    # O(log(m) + log(n))
    print(i1, i2, j1, j2)
    m = len(matrix)
    if m == 0: return False
    n = len(matrix[0])
    if not IsValidInds(matrix, i1, i2, j1, j2):
        return False
    imid = (i1 + i2) // 2
    jmid = (j1 + j2) // 2

    print(matrix[imid][jmid])
    if matrix[imid][jmid] == target:
        return True
    if i1 == i2 or j1 == j2:
        return SearchRow(matrix, target, i1, 0, n-1) or\
               SearchCol(matrix, target, 0, m-1, j1)
    elif matrix[imid][jmid] < target:
        return Search(matrix, target, imid + 1, i2, jmid + 1, j2) or \
               Search(matrix, target, i1, imid-1, jmid + 1, j2) or\
               Search(matrix, target, imid + 1, i2, j1, jmid-1)
    else:
        return Search(matrix, target, i1, imid, j1, jmid) or \
               Search(matrix, target, i1, imid - 1, jmid + 1, j2) or \
               Search(matrix, target, imid + 1, i2, j1, jmid - 1)

def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    # O(log(max(m,n))
    m = len(matrix)
    if m==0:
        return False
    n = len(matrix[0])
    if n == 0: return False
    return Search(matrix, target, 0, m-1, 0, n-1)

self = None
# matrix = [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# matrix = [[-1,3]]
# target = 3

# matrix = [[5],[6]]
# target = 6
# matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# target = 20


matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11,12,13,14,15],
          [16,17,18,19,20],
          [21,22,23,24,25]]
target = 15

print(searchMatrix(self, matrix, target))