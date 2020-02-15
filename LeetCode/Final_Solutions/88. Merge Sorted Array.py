def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    if n == 0:
        return
    # move forward the numbers in nums1:
    for i in range(m + n - 1, 0, -1):
        nums1[i] = nums1[i-n]
    i1 = n
    i2 = 0
    # Merge:
    for i in range(m + n):
        if i1 == m + n:
            nums1[i] = nums2[i2]
            i2 += 1
        elif i2 == n:
            nums1[i] = nums1[i1]
            i1 += 1
        elif nums1[i1] > nums2[i2]:
            nums1[i] = nums2[i2]
            i2 += 1
        else:
            nums1[i] = nums1[i1]
            i1 += 1
    return


self = None
#
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3


nums1 = [1,2,4,5,6,0]
m = 5
nums2 = [3]
n =1

merge(self, nums1, m, nums2, n)
print(nums1)


