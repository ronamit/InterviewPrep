

def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    shift = 0
    n = len(nums)
    if n <= 1:
        return
    for i in range(1, n):
        if nums[i] == nums[i-1]:
            shift += 1
        else:
            nums[i - shift] = nums[i]

    del nums[n-shift:]
    return





self = None
nums = [0,0,1,1,1,2,2,3,3,4]
removeDuplicates(self, nums)
print(nums)