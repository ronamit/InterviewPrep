class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        def IsAdditiveNext(start, first_num):
            if start == n:
                return True
            for i in range(start, n):
                second_num = int(num[start:i+1])
                sm_num = first_num + second_num
                sm_str = str(sm_num)
                sm_len = len(sm_str)
                if num[i + 1:i + sm_len + 1] == sm_str \
                        and IsAdditiveNext(i + sm_len + 1, sm_num):
                    return True
            return False
        for i in range(n-1):
            prefix = num[:i+1]
            first_num = int(prefix)
            if IsAdditiveNext(i + 1, first_num):
                return True
        return False

sol = Solution()
print(sol.isAdditiveNumber("112358"))