class Solution:

    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if n == 0:
            return "0"
        if k == 0:
            return num
        if n <= k:
            # since in this case we can remove all digits
            return "0"
        min_x = None
        for i in range(n):
            num_new = num[:i] + num[i + 1 :]
            # remove trailing zeros:
            num_new = num_new.lstrip("0")
            new_x = self.removeKdigits(num=num_new, k=k - 1)
            if min_x is None or (len(new_x), new_x) < (len(min_x), min_x):
                min_x = new_x
        return min_x
