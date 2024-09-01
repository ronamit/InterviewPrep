class Solution:
    def minSwaps(self, data: list[int]) -> int:
        
        n = len(data)
        cum_sum = [data[0]]
        for i in range(1, n):
            cum_sum.append(data[i] + cum_sum[-1])
        n_ones_tot = cum_sum[-1]
        n_zeros_tot = n - n_ones_tot
        if n_zeros_tot == 0 or n_ones_tot == 0:
            return 0
        min_swaps = float("inf")
        for i in range(n - n_ones_tot + 1):
            # check how many swaps needed to put all the ones
            # in the windows [i, i+n_ones_tot-1]
            sum_before_win = cum_sum[i - 1] if i > 0 else 0
            n_ones_in_win = cum_sum[i + n_ones_tot - 1] - sum_before_win
            n_swaps = n_ones_tot - n_ones_in_win
            min_swaps = min(min_swaps, n_swaps)
        return min_swaps
