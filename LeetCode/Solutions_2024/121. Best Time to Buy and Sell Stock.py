class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        left_max = [0 for _ in range(n)]
        left_max[-1] = prices[-1]
        for i in range(n - 2, -1, -1):
            left_max[i] = max(left_max[i + 1], prices[i])
        max_profit = 0
        for i in range(n):
            profit = left_max[i] - prices[i]
            max_profit = max(max_profit, profit)
        return max_profit
