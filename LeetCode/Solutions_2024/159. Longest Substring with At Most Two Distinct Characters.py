from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        left = 0
        right = 0
        char_count = defaultdict(lambda: 0)
        char_count[s[left]] += 1
        n_distinct = 1
        ans = -1
        while right < n:
            if n_distinct <= 2:
                ans = max(ans, right - left + 1)
            while n_distinct > 2 and left <= right:
                if char_count[s[left]] == 1:
                    n_distinct -= 1
                char_count[s[left]] -= 1
                left += 1
            right += 1
            if right < n:
                char_count[s[right]] += 1
                if char_count[s[right]] == 1:
                    n_distinct += 1
        return ans


if __name__ == "__main__":
    s = "eceba"
    print(Solution().lengthOfLongestSubstringTwoDistinct(s))
