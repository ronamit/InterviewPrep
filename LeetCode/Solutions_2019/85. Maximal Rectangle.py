
class Solution:
    def maximalRectangle(self, matrix):
        # replace each '1' with the index in the streak of '1' from left side
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        for i in  range(m):
            for j in range(n):
                if matrix[i][j] == "0" or j == 0:
                    matrix[i][j] = int(matrix[i][j])
                elif matrix[i][j] == "1":
                    matrix[i][j] = matrix[i][j-1] + 1
        for row in matrix:
            print(row)
        # for each column go from up to down' in each streak of non-zero ave the min-val and the length of streak,
        # the current area is min-val*length
        # keep and return the max area
        max_val = max([max(row) for row in matrix])
        max_area = 0
        for j in range(n):
            for i in range(m):
                if matrix[i][j] != 0:
                   scan_stop = m #min(i + matrix[i][j], m)
                   streak_min = max_val
                   streak_len = 0
                   for ii in range(i,  scan_stop):
                        if matrix[ii][j] == 0:
                           break
                        streak_len += 1
                        streak_min = min(streak_min,  matrix[ii][j])
                        area = streak_len * streak_min
                        max_area = max(max_area, area)
        return max_area


sol = Solution()
matrix = [["0","1","1","0","1"],["1","1","0","1","0"],["0","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["0","0","0","0","0"]]
# matrix = [["0","1"],["0","1"]]
for row in matrix:
    print([int(x) for x in row])
print('-'*20)
print(sol.maximalRectangle(matrix))
#
#
# def maximalRectangle(self, matrix):
#     # replace each '1' with the index in the streak of '1' from left side
#     m = len(matrix)
#     if m == 0: return 0
#     n = len(matrix[0])
#     for i in range(m):
#         for j in range(n):
#             if matrix[i][j] == "0" or j == 0:
#                 matrix[i][j] = int(matrix[i][j])
#             elif matrix[i][j] == "1":
#                 matrix[i][j] = matrix[i][j - 1] + 1
#     for row in matrix:
#         print(row)
#     # for each column go from up to down' in each streak of non-zero ave the min-val and the length of streak,
#     # the current area is min-val*length
#     # keep and return the max area
#     max_val = max([max(row) for row in matrix])
#     max_area = 0
#     for j in range(n):
#         streak_len = 0
#         streak_min = max_val
#         for i in range(m):
#             if matrix[i][j] == 0:
#                 streak_len = 0
#                 streak_min = max_val
#             else:
#                 streak_len += 1
#                 streak_min = min(streak_min, matrix[i][j])
#             area = streak_len * streak_min
#             max_area = max(max_area, area)
#     return max_area
