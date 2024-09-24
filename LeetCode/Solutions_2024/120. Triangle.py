class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n_rows = len(triangle)
        for i_row in range(1, n_rows):
            cur_row = triangle[i_row]
            cur_n_cols = len(cur_row)
            for i_col in range(cur_n_cols):
                cur_val = triangle[i_row][i_col]
                path_a = float("inf")
                path_b = float("inf")
                if i_col < len(triangle[i_row - 1]):
                    path_a = cur_val + triangle[i_row - 1][i_col]
                if i_col > 0:
                    path_b = cur_val + triangle[i_row - 1][i_col - 1]
                triangle[i_row][i_col] = min(path_a, path_b)
        return min(triangle[-1])
