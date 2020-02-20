def rotate(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """

    n = len(matrix)
    # First transpose:
    # go over upper triangle:
    for i in range(n):
        for j in range(i+1, n):
            # swap:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Then reverse lines:
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    return

self = None
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
rotate(self, matrix)
print(matrix)