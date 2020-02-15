
def findDuplicate(self, nums: 'List[int]') -> 'int':

    nums.sort()
    n = len(nums)
    for i in range(1, n):
        if nums[i] == nums[i - 1]:
            return nums[i]
    return 0


self = None
nums = [1,3,4,2,2]
print(findDuplicate(self, nums))