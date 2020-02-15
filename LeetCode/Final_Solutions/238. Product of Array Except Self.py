def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    out_arr = [1] * n
    for i in range(n - 2, -1, -1):
        out_arr[i] = out_arr[i + 1] * nums[i+1]
    cum_mult = 1
    for i in range(n):
        out_arr[i] = cum_mult * out_arr[i]
        cum_mult *= nums[i]
    return out_arr

self = None
input = [1,2,3,4]
print(productExceptSelf(self, input))