


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != (len(s1)+len(s2)):
            return False
        # table that saves computed results:
        T = [[[2 for i3 in range(len(s3)+1)] for i2 in range(len(s2)+1)] for i1 in range(len(s1)+1)]
        def RecFunc(n1, n2, n3):
            if n3 == 0:
                return True
            if T[n1][n2][n3] != 2:
                # if already computed
                return T[n1][n2][n3] == 0
            isValid = (n1 > 0 and s3[n3 - 1] == s1[n1 - 1] and RecFunc(n1 - 1, n2, n3 - 1)) or \
            (n2 > 0 and s3[n3 - 1] == s2[n2 - 1] and RecFunc(n1, n2 - 1, n3 - 1))
            T[n1][n2][n3] = isValid
            return isValid
        return RecFunc(len(s1), len(s2), len(s3))

sol = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
#
# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbbaccc"


print(sol.isInterleave(s1,s2,s3))
