class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        ans = 0
        n = len(nums)
        # then calculate the answer by summing:
        # nums[i] * (n_win_where_it_largest - n_win_where_it_smallest)

        # Monotonic stack of array elements of increasing sizes

        def get_leftmost_arrays(array: list[int], scan_dir: int):
            nonlocal n
            leftmost_smallest_arr = [None for _ in range(n)]
            leftmost_largest_arr = [None for _ in range(n)]
            up_stack = []
            down_stack = []
            scan_range = range(n) if scan_dir == 1 else range(n - 1, -1, -1)
            for i in scan_range:
                x = array[i]
                # find the leftmost element that is smaller than x
                j = None
                while up_stack and up_stack[-1][1] >= x:
                    j, _ = up_stack.pop()
                leftmost_smallest_arr[i] = j if j is not None else i
                up_stack.append((i, x))
                j = None
                # find the leftmost element that is larger than x
                while down_stack and down_stack[-1][1] <= x:
                    j, _ = down_stack.pop()
                leftmost_largest_arr[i] = j if j is not None else i
                down_stack.append((i, x))
            return leftmost_smallest_arr, leftmost_largest_arr

        leftmost_smallest_arr, leftmost_largest_arr = get_leftmost_arrays(nums, scan_dir=1)
        rightmost_smallest_arr, rightmost_largest_arr = get_leftmost_arrays(nums, scan_dir=-1)

        ans = 0
        for i in range(n):
            n_where_its_largest = (rightmost_largest_arr[i] - i)  * (i - leftmost_largest_arr[i])
            n_where_its_smallest = (rightmost_smallest_arr[i] - i) * (i - leftmost_smallest_arr[i])
            ans += nums[i] * (n_where_its_largest - n_where_its_smallest)
        return ans


# # Brute force:
# class Solution:
#     def subArrayRanges(self, nums: List[int]) -> int:
#         ans = 0
#         n = len(nums)
#         for i in range(n):
#             for j in range(i,n):
#                 sub_arr = nums[i:(j+1)]
#                 ans += max(sub_arr) - min(sub_arr)
#         return ans


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().subArrayRanges(nums))
