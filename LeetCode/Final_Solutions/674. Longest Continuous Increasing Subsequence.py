def findLengthOfLCIS(self, nums: 'List[int]') -> 'int':
    n = len(nums)
    if n==0: return 0
    maxlen = 1
    currlen = 1
    for i in range(1,n):
        if nums[i] > nums[i-1]:
            currlen += 1
            maxlen = max(maxlen, currlen)
        else:
            currlen = 1
    return maxlen



self = None
nums = [2,3,1]
print( findLengthOfLCIS(self, nums))