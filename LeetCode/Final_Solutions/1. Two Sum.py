def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # Using Hash-Table
    elems = dict()
    for i, a in enumerate(nums):
        elems[a] = i

    for i, a in enumerate(nums):
        if (target - a) in elems.keys():
            j = elems[target - a]
            if j != i:
                return [j, i]
    return []

self = None
nums = [2, 7, 11, 15]
target = 9
print(twoSum(self, nums, target))



#
# def binarySearch(alist, item):
#     first = 0
#     last = len(alist)-1
#     found = False
#     midpoint = -1
#     while first<=last and not found:
#         midpoint = (first + last)//2
#         if alist[midpoint] == item:
#             found = True
#         else:
#             if item < alist[midpoint]:
#                 last = midpoint-1
#             else:
#                 first = midpoint+1
#     return found, midpoint
#
#
# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#
#         num_t = [(i, a) for i, a in enumerate(nums)]
#         num_t = sorted(num_t, key=lambda x: x[1])
#         indices, L_sorted = zip(*num_t)
#         print(indices)
#         for i, a in enumerate(nums):
#             found, j = binarySearch(L_sorted, target - a)
#             print(a, L_sorted[j])
#             j_orig = indices[j]
#             if found and  i != j_orig:
#                 return [i,j_orig]
#         return []