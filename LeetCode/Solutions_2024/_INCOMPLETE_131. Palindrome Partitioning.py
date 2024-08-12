from functools import cache


class Solution:
    def is_palindrome(self, s):
        return s == s[::-1]

    @cache  # noqa: B019
    def partition(self, s: str) -> list[list[str]]:
        if len(s) == 0:
            return []
        # check if the original string is palindorme
        if self.is_palindrome(s):
            res = [s]
        else:
            res = []
        # check if any s[:i] is palindrome (and then concate the possible paritions of the rest of the string)
        for i in range(1, len(s) + 1):
            if self.is_palindrome(s[:i]):
                rest_part_options = self.partition(s[i:])
                for rest_part in rest_part_options:
                    full_part = [s[:i], *rest_part]
                    res.append(full_part)
        return res


if __name__ == "__main__":
    sol = Solution()
    s = "bb"
    print(sol.partition(s))
