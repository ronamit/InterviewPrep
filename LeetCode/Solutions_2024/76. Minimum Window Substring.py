from collections import Counter


def count_covers(win_counts, t_counts):
    return all(win_counts[char] >= t_counts[char] for char in t_counts)


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        win_counts = Counter()
        t_counts = Counter(t)
        left = 0
        right = 0
        win_counts[s[0]] += 1
        min_win_len = float("inf")
        min_win = None
        while right < len(s):
            while count_covers(win_counts, t_counts) and left <= right:
                cur_win_len = right - left + 1
                if cur_win_len < min_win_len:
                    min_win_len = cur_win_len
                    min_win = (left, right)
                win_counts[s[left]] -= 1
                left += 1
            right += 1
            if right < len(s):
                win_counts[s[right]] += 1

        return "" if min_win is None else s[min_win[0] : min_win[1] + 1]


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))
