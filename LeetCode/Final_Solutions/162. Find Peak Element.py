


def argmax(arr):
    max_v = arr[0]
    max_i = 0
    for i,a in enumerate(arr):
        if a > max_v:
            max_v = a
            max_i = i
    return max_i

def findPeakElementR(arr):
    n = len(arr)
    if n == 1:
        return 0
    elif n == 2 or n == 3:
        return argmax(arr)
    m = n//2
    if arr[m+1] <= arr[m] and arr[m-1] <= arr[m]:
        return m
    if arr[m+1] > arr[m]:
        return m + 1 + findPeakElementR(arr[m+1:])
    else:
        return findPeakElementR(arr[:m])

def findPeakElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return findPeakElementR(nums)

self = None
# nums =  [1,2,1,3,5,6,4]
nums = [1]
print(findPeakElement(self, nums))