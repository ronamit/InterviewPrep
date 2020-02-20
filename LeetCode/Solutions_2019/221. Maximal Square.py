class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m ==0: return 0
        n = len(matrix[0])
        maxL = ('1' in matrix[0] or '1' in [matrix[i][0] for i in range(m)])
        for i in range(1, m):
            for j in range(1,n):
                if  matrix[i][j] ==  '1':
                    matrix[i][j] = 1 + min( int(matrix[i-1][j]),  int(matrix[i][j-1]), int(matrix[i-1][j-1]))
                    maxL = max(maxL, matrix[i][j])
        return maxL**2