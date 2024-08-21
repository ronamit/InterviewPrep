from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        counts = Counter(nums)
        ans = [num for num, cnt in counts.items() if cnt > (n // 3)]
        return ans
# TODO: follow-up with constant space