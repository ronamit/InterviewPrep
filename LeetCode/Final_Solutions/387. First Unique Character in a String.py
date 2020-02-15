def firstUniqChar(self, s):
    """
    :type s: str
    :rtype: int
    """
    chars = {}
    for a in s:
        if a not in chars:
            chars[a] = 1
        else:
            chars[a] += 1
    print(chars)
    for i, a in enumerate(s):
        if chars[a] == 1:
            return i
    return -1

self = None

s = "loveleetcode"
print(firstUniqChar(self, s))