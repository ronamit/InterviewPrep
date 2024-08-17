class Solution:
    def numTeams(self, rating: list[int]) -> int:
        n = len(rating)
        n_teams = 0
        for j in range(1, n - 1):
            # count how many lower rating are before rating[j]
            # (the rest of the j-n_low must be higher since rating are unique)
            n_low_pre = 0
            for i in range(j):
                n_low_pre += rating[i] < rating[j]
            n_high_pre = j - n_low_pre
            n_low_post = 0
            for k in range(j + 1, n):
                n_low_post += rating[k] < rating[j]
            n_high_post = n - 1 - j - n_low_post
            n_teams += n_low_pre * n_high_post + n_high_pre * n_low_post
        return n_teams
