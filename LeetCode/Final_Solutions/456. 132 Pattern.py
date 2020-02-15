
def find132pattern(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    n = len(nums)
    if n < 3: return False
    minFromEnd = [None for _ in range(n)]
    minFromEnd[n - 1] = nums[n - 1]
    for i in range(n - 2, -1, -1):
        minFromEnd[i] = min(minFromEnd[i + 1], nums[i])
    maxFromEnd = [None for _ in range(n)]
    maxFromEnd[n - 1] = nums[n - 1]
    for i in range(n - 2, -1, -1):
        maxFromEnd[i] = max(maxFromEnd[i + 1], nums[i])

    a0 = nums[0] # first number is the past min
    i0 = 0
    i1 = 1
    for i1 in range(1, n - 1):
        # check if in the range [i1+1,n-1] there is a number nums[i2]
        # s.t nums[i2] > curMin and nums[i2] < nums[i1]
        a1 = nums[i1]
        if a1 > a0:
            if not (a0 < maxFromEnd[i1 + 1]
                    and a1 > minFromEnd[i1 + 1]):
                continue
            for i2 in range(i1+1, n):
                a2 = nums[i2]
                if a2 > a0 and a2 < a1:
                    return True

        if nums[i1] < a0:
            a0 = nums[i1]
            i0 = i1
    return False

self = None
nums = [1,2,4,3]
print(find132pattern(self, nums))