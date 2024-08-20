from functools import cache


class Solution:

    def splitArray(self, nums: list[int], k: int) -> int:
        # Idea: for k==2 it is easy to solve with prefix and postfix sum
        # For k==4, we can check all splits to 2-arrays and solve for k==2 for them

        # Naive/DP solution
        # loop over the first subarray end and find recusive solution for k-1 in the rest of the array, and take the max between this and the sum of the first subarray
        # and then take the min  max_sum from all iterations
        # complexity: O(k*n^2) (The function is called k*n times)
        @cache
        def split_part(i_start: int, k_c: int):
            nonlocal nums
            nums_c = nums[i_start:]
            n = len(nums_c)
            if k_c > n:
                return float("inf")
            if k_c == n:
                return max(nums_c)
            if k_c == 1:
                return sum(nums_c)
            if n == 0:
                return 0
            first_sub_sum = 0
            ans = +float("inf")
            for i in range(1, n + 2 - k_c):
                # nums_c[:i] is the first subarray (non-empty)
                first_sub_sum += nums_c[i - 1]
                # Min split if we take nums_c[:i]  as the first subarry
                rest_minmax_sum = split_part(i_start + i, k_c - 1)
                if rest_minmax_sum == float("inf"):
                    continue
                max_sum_cur = max(first_sub_sum, rest_minmax_sum)
                ans = min(ans, max_sum_cur)
            return ans

        return split_part(0, k)


if __name__ == "__main__":
    sol = Solution()
    print(sol.splitArray([2, 3, 1, 2, 4, 3], 5))
