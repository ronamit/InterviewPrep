class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n = len(nums)
        i = 0
        j = n - 1
        while j > i:
            # print(f"(i,j)=({i},{j})")
            mid = (i + j) // 2
            # print(f"mid={mid}")
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid - 1
        if nums[i] < target:
            return i + 1
        return i


sol = Solution()
print(sol.searchInsert([1, 3, 5, 6], 2))
