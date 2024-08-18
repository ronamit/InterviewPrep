class Solution:
    def minimumDeletions(self, s: str) -> int:
        # create array that saves for each index how many a's are after it
        # and how many b's are before it
        # loop over the length of s and check how many deletes needed
        # to make it balanced s[:i] and s[i+1:]
        n = len(s)
        cnt_a_pre = [0 for _ in range(n + 1)]  #  for each i how many a's in s[:i]
        for i in range(1, n + 1):
            cnt_a_pre[i] = cnt_a_pre[i - 1] + (s[i - 1] == "a")
        cnt_b_post = [0 for _ in range(n)]  #  for each i how many b's are in s[i:]
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                cnt_b_post[i] = s[i] == "b"
            else:
                cnt_b_post[i] = (s[i] == "b") + cnt_b_post[i + 1]
        cnt_b_post.append(0)
        min_del = n
        for i in range(n + 1):
            # how many deletions needed to make number of 'a' in s[:i] and number of 'b' in s[i:] equal
            dels_pre = i - cnt_a_pre[i]  # need to delete all b's in the prefix [:i]
            del_post = n - i - cnt_b_post[i]  # # need to delete all a's in the postfix [i:]
            min_del = min(min_del, dels_pre + del_post)
        return min_del
