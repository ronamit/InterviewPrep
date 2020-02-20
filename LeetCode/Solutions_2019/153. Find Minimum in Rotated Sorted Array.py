class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        def FindRec(first, last):
            while last > first:
                mid = (first + last) // 2
                if nums[(mid - 1) % n] > nums[mid]:
                    return mid
                if nums[mid] > nums[last]:
                    first = mid + 1
                else:
                    last = mid - 1
            return (first + last) // 2

        return nums[FindRec(0, n - 1)]
