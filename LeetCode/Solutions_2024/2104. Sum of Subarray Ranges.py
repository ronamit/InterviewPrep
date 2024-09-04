class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        ans = 0
        n = len(nums)
        # then calculate the answer by summing:
        # nums[i] * (n_win_where_it_largest - n_win_where_it_smallest)

        # for each i, find the left and right bounds of the sub-array of elements around it that are <= x[i]
        # i.e., for each i, find j,k  -1 <= j <= i <= k <= n s.t. nums[h] <= x[i] for all h: j < h < k
        
        # for each i, find max j < i s.t x[j] > x[i] (-1 if no such j)
        smaller_left = [-1 for _ in range(n)]
        # for each i, find min k > i s.t x[k] > x[i]  (n if no such k)
        smaller_right = [n for _ in range(n)]
        # indexes of previous elements, in increasing nums[i] values
        stack = []
        for right in range(n + 1):
            while stack and (right == n or nums[stack[-1]] >= nums[right]):
                mid = stack.pop()
                smaller_left[mid] = stack[-1] if stack else -1
                smaller_right[mid] = right
            stack.append(right)

        # for each i, find the left and right bounds of the sub-array of elements around it that are >= x[i]
        # i.e., for each i, find j,k - <= j <= i <= k <= n  s.t. nums[h] >= x[i] for all h:  j < h < k
        
        # for each i, find max j < i s.t x[j] < x[i]  (-1 if no such j)
        larger_left = [-1 for _ in range(n)]
        # for each i, find min i < k s.t x[k] < x[i] (n if no such k)
        larger_right = [n for _ in range(n)]
        # indexes of previous elements, in decreasing nums[i] values
        stack = [] 
        for right in range(n + 1):
            while stack and (right == n or nums[stack[-1]] <= nums[right]):
                mid = stack.pop()
                larger_right[mid] = right
                larger_left[mid] = stack[-1] if stack else -1
            stack.append(right)

        # print(f"nums: {nums}")
        # print(f"Smaller left: {smaller_left}")
        # print(f"Smaller right: {smaller_right}")
        # print(f"Larger left: {larger_left}")
        # print(f"Larger right: {larger_right}")
        ans = 0
        for i in range(n):
            # number of options to left bound * number of options to right bound of the subarray around i that are <= x[i]
            n_where_its_smallest = (smaller_right[i] - i) * (i - smaller_left[i])
            # number of options to left bound * number of options to right bound of the subarray around i that are >= x[i]
            n_where_its_largest = (larger_right[i] - i) * (i - larger_left[i])
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
