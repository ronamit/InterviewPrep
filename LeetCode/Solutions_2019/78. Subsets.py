def bits_inds(m):
    k = 0
    inds = []
    while m:
        if m % 2 == 1:
            inds += [k]
        m = m // 2
        k += 1
    return inds


def subsets(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    pset = []
    n = len(nums)
    for i in range(2**n):
        inds = bits_inds(i)
        c_set = [nums[k] for k in inds]
        pset += [c_set]
    return pset

self = None
nums = [1,2,3]
print(subsets(self, nums))