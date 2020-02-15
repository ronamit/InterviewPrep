def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    max_sub = nums[0]
    W_prev = nums[0]
    M = 0
    for i in range(1, n):
        # find the cumulative sum:
        W = W_prev + nums[i]
        # find the cumulative min of W (min_{j<i} W[j-1))
        if i == 1:
            M = W_prev
        else:
            M = min(W_prev, M)
        max_sub = max(max_sub, W - M, W)
        W_prev = W
    return max_sub


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# nums = [1,2]
self = None
print(maxSubArray(self, nums))

#
# def maxSubArray(self, nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     n = len(nums)
#     if n == 0:
#         return 0
#     if n == 1:
#         return nums[0]
#     # find the cumulative sum:
#     W = [a for a in nums]
#     for i in range(1, n):
#         a = nums[i]
#         W[i] = W[i-1] + a
#     # find the cumulative min of W (min_{j<i} W[j-1))
#     M = [0 for _ in nums]
#     for i in range(1, n):
#         if i == 1:
#             M[i] = W[i-1]
#         else:
#             M[i] = min(W[i-1], M[i-1])
#     max_sub = W[0]
#     print(W)
#     print(M)
#     for i in range(1, n):
#         max_sub = max(max_sub, W[i] - M[i], W[i])
#     return max_sub
#
