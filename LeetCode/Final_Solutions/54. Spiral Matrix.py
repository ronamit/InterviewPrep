def spiralOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
    m = len(matrix)
    if m == 0: return []
    n = len(matrix[0])
    X = min([min(row) for row in matrix]) - 1
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    n_dirs = len(dirs)
    c_dir = 0
    i = 0
    j = 0
    out = []
    for k in range(m*n):
        out += [matrix[i][j]]
        matrix[i][j] = X
        good_move = False
        n_tries = 0
        while not good_move and n_tries < n_dirs:
            n_tries += 1
            ii = i + dirs[c_dir][0]
            jj = j + dirs[c_dir][1]
            if (ii >= 0) and (ii < m) and (jj >= 0) and (jj < n)\
                    and matrix[ii][jj] > X:
                good_move = True
            else:
                c_dir = (c_dir + 1) % n_dirs
        if not good_move:
            break
        else:
            i = ii
            j = jj
    return out

self = None
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print(spiralOrder(self, matrix))
