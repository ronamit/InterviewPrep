class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        n = len(arr)

        def is_peak(i: int) -> bool:
            return 0 < i < (n - 1) and arr[i - 1] < arr[i] and arr[i] > arr[i + 1]

        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            # print(left, mid, right)
            if is_peak(left):
                return left
            if is_peak(right):
                return right
            if is_peak(mid):
                return mid
            if arr[mid] < arr[mid + 1]:
                # mid is still in the ascending part
                # - look right half
                left = mid + 1
            else:
                right = mid - 1
        return mid
