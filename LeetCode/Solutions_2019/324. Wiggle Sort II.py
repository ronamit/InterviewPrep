
def wiggleSort(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    if n==0: return
    newarr = [0 for _ in range(n)]
    nums.sort()
    j = 0
    k = 0
    for i in range(n):
        if i % 2 == 0:
            newarr[i] = nums[(n+1)//2 - j - 1]
            j += 1
        else:
            newarr[i] = nums[n - 1 - k]
            k += 1
    for i in range(n):
        nums[i] = newarr[i]


self = None
# nums = [1, 5, 1, 1, 6, 4]
nums = [1,1,2,1,2,2,1]
wiggleSort(self, nums)
print(nums)