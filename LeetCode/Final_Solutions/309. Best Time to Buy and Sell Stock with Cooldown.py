

def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    n = len(prices)
    if n == 0: return 0
    # Dynamic-prog
    V = [0 for _ in range(n)]
    max_margin = -prices[0]

    for i in range(1, n):
        curr_margin = -prices[i]
        if i >= 2:
            # add the maximal profit we could get before the 2 days before day of buy (j) (cooldown)
            curr_margin += V[i - 2]
        max_margin = max(max_margin, curr_margin)
        maxprof = prices[i] + max_margin
        # take the max between (buying on j and selling in i) to (don't do anything)
        V[i] = max(maxprof, V[i - 1])
    # print(V)
    return (V[n - 1])



self = None
prices = [1,2,3,0,2]
print(maxProfit(self, prices))



#
# def maxProfit(self, prices):
#     """
#     :type prices: List[int]
#     :rtype: int
#     """
#     n = len(prices)
#     if n == 0: return 0
#     # Dynamic-prog
#     V = [0 for _ in range(n)]
#
#     for i in range(1, n):
#         maxprof = 0
#         # run on buy time (0..i-1):
#         for j in range(0, i):
#             profit = prices[i] - prices[j]
#             if j >= 1:
#                 # add the maximal profit we could get before the 2 days before day of buy (j) (cooldown)
#                 profit += V[j - 2]
#             if profit > maxprof:
#                 maxprof = profit
#         # take the max between (buying on j and selling in i) to (don't do anything)
#         V[i] = max(maxprof, V[i-1])
#     print(V)
#     return (V[n-1])
