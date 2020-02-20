def setZeroes(self, matrix: 'List[List[int]]') -> 'None':
    """
    Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)
    if m == 0: return
    n = len(matrix[0])
    mx =  max([max(row) for row in matrix])
    del_col_token = mx + 10
    del_row_token = mx + 20
    del_both_token = mx + 30
    tokens = [del_col_token, del_row_token, del_both_token]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                if matrix[0][j] in [del_row_token, del_both_token]:
                    matrix[0][j] = del_both_token
                else:
                    matrix[0][j] = del_col_token
                if matrix[i][0] in [del_col_token, del_both_token]:
                    matrix[i][0] = del_both_token
                else:
                    matrix[i][0] = del_row_token
    print(matrix)
    for i in range(m):
        if matrix[i][0] in [del_row_token, del_both_token]:
            for j in range(n):
                if matrix[i][j] not in tokens:
                    matrix[i][j] = 0
    for j in range(n):
        if matrix[0][j] in [del_col_token, del_both_token]:
            for i in range(m):
                if matrix[i][j] not in tokens:
                    matrix[i][j] = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] in tokens:
                matrix[i][j] = 0
    return


self = None
matrix = [[0, 1, 2, 0],
          [3, 4, 5, 2],
          [1, 3, 1, 5]]
print(matrix)
setZeroes(self, matrix)
print('Output:')
print(matrix)