

def canJump(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    n =len(nums)
    # minimal good index (from which we can reach  last)
    gi = n-1
    for i in range(n - 2, -1, -1):
        ijump = i + nums[i]
        if ijump >= gi:
            gi = i
    return (gi==0)



self = None
nums = [3,2,1,0,4]
print(canJump(self, nums))

# v = [False for _ in nums]
# v[-1] = True
# n = len(nums)
# for i in range(n-2,-1,-1):
#     # print(v)
#     for jump in range(1, nums[i]+1):
#         ijump = i + jump
#         if (ijump < n-1 and v[ijump]) or (ijump == n-1):
#             v[i] = True
#             break
# return v[0]