class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        min_to_prev_row = matrix[0].copy()  # [n]
        min_to_cur_row = [None for _ in range(n)]
        for i_row in range(1, n):
            for i_col in range(n):
                min_to_here = min_to_prev_row[i_col]
                if i_col > 0:
                    min_to_here = min(min_to_here, min_to_prev_row[i_col - 1])
                if i_col < n - 1:
                    min_to_here = min(min_to_here, min_to_prev_row[i_col + 1])
                min_to_cur_row[i_col] = min_to_here + matrix[i_row][i_col]
            min_to_prev_row = min_to_cur_row.copy()
        return min(min_to_cur_row)
