def searchRange(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    n = len(nums)
    # Find First:
    r = n - 1
    l = 0
    first = -1
    while (r >= l):
        mid = (r + l) // 2
        if nums[mid] == target and (mid == 0 or nums[mid-1] != target):
            first = mid
            break
        elif nums[mid] > target or (mid > 0 and nums[mid-1]) == target:
            r = mid - 1
        else:
            l = mid + 1
    last = -1
    r = n - 1
    l = 0
    while (r >= l):
        mid = (r + l) // 2
        if nums[mid] == target and (mid == n-1 or nums[mid + 1] != target):
            last = mid
            break
        elif nums[mid] < target or (mid < n-1 and nums[mid + 1] == target):
            l = mid + 1
        else:
            r = mid - 1
    return [first, last]




self = None
# nums = [5,7,7,8,8,10]
# target = 7
nums = [1]
target = 0
print(searchRange(self, nums, target))