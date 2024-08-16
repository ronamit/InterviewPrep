class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        lo = 0
        hi = m * n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            row = mid // n
            col = mid % n
            val = matrix[row][col]
            if val == target:
                return True
            if val < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return False
