def is_divides_string(prefix: str, s:str , i_start: int) -> bool:
    return all(s[i:i + len(prefix)] == prefix for i in range(i_start, len(s), len(prefix)))


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # set str1 as the smaller
        if len(str2) > len(str1):
            str1, str2 = str2, str1
        # go over all prefixes and check if they divide both strings
        for i in range(len(str1), 0, -1):
            prefix = str1[:i]
            if is_divides_string(prefix, str1, i) and is_divides_string(prefix, str2, 0):
                return prefix
        return ""
