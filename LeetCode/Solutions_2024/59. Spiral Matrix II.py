class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        a = [[None for _ in range(n)] for _ in range(n)]
        row = 0
        col = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i_dir = 0
        for i in range(1, n**2 + 1):
            a[row][col] = i
            valid_move = False
            i_attempt = 0
            while not valid_move and i_attempt < 4:
                row_n = row + dirs[i_dir][0]
                col_n = col + dirs[i_dir][1]
                if 0 <= row_n < n and 0 <= col_n < n and a[row_n][col_n] is None:
                    valid_move = True
                else:
                    i_dir = (i_dir + 1) % len(dirs)
                    i_attempt += 1
            row = row_n
            col = col_n
        return a
