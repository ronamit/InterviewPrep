from string import ascii_uppercase


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # let's first solve easier question: can we get a substring of length w? O(n)
        # then we can do a binary search to get the max viable w: in total O(n*log(n)
        n = len(s)

        def can_create_length(w: int) -> bool:
            nonlocal s, k, n
            if w > n:
                return False
            # use a sliding window of length w and keep a counter for each word in ABC inside the window, if some word gets to count of (w - min{k, |S|-w}) return True
            counts = {c: 0 for c in ascii_uppercase}
            for i in range(w):
                counts[s[i]] += 1
                if counts[s[i]] + k >= w:
                    return True
            i = 1
            while i + w <= n:
                old_char = s[i - 1]
                new_char = s[i + w - 1]
                counts[old_char] -= 1
                counts[new_char] += 1
                if counts[new_char] + k >= w:
                    return True
                i += 1
            return False

        left = 0
        right = n
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if can_create_length(mid):
                ans = max(ans, mid)
                left = mid + 1
            else:
                right = mid - 1
        return ans
