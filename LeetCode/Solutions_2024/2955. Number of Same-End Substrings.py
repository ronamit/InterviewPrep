from string import ascii_lowercase


class Solution:
    def sameEndSubstringCount(self, s: str, queries: list[list[int]]) -> list[int]:
        # n_subs = len of str
        # for each char if count(char) >= 2, n_subs += count(char) choose 2
        # to get counts in range, substrcat cummalative counts on end and start
        n = len(s)
        counts = [[0 for _ in ascii_lowercase] for _ in range(n)]  # [n x Sigma]
        char_to_int = {c: i for i, c in enumerate(ascii_lowercase)}
        n_alphabet = len(ascii_lowercase)
        for i in range(n):
            i_cur_char = char_to_int[s[i]]
            for i_char in range(n_alphabet):
                prev_count = counts[i - 1][i_char] if i > 0 else 0
                counts[i][i_char] = prev_count + (i_char == i_cur_char)

        ans = []
        for query in queries:
            ans.append(0)
            left, right = query
            for i_char in range(n_alphabet):
                pre_count = counts[left - 1][i_char] if left > 0 else 0
                q_count = counts[right][i_char] - pre_count
                if q_count == 0:
                    continue
                if q_count == 1:
                    ans[-1] += 1
                else:
                    # sum all possible 1-length substring and all possible length >=2 (n choose 2)
                    ans[-1] += q_count + q_count * (q_count - 1) // 2
        return ans
