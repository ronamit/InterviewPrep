class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # to check if some C can be an answer -
        # run with a sliding window of size C over the array and see if at
        # any point we get a sum in the window of C-k, then we return True
        # to get the answer - we do binary search on the range of C
        # 1 <= C <=  min(n, sum(nums) + k)
        # the total complexity is O(n * log(n))

        n = len(nums)
        if n == 0:
            return 0

        def can_fit_window(C: int) -> bool:
            nonlocal nums, k
            if n < C:
                return False
            s = sum(nums[:C])  #  sum of current window 0..(C-1)

            for i in range(n - C + 1):
                j = i + C  # window end index
                if (s + k) >= C:
                    # we can flip k times and get a window with all ones
                    return True
                # update the sliding window sum:
                s -= nums[i]  # remove the first element of the window
                s += nums[j] if j < n else 0 # add the last element of the window
            return False

        # binary search
        low = 0
        high = min(n, sum(nums) + k)
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            can_fit = can_fit_window(mid)
            # print(f"can_fit_window({mid})={can_fit}")
            if can_fit:
                ans = max(ans, mid)
                low = mid + 1
            else:
                high = mid - 1
        return ans


if __name__ == "__main__":
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 0
    print(Solution().longestOnes(nums, k))
