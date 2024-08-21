
def range_to_str(range_start: int, range_end: int) -> str:
    if range_start == range_end:
        return str(range_start)
    return f"{range_start}->{range_end}"


class Solution:

    def summaryRanges(self, nums: list[int]) -> list[str]:
        ans = []
        if len(nums) == 0:
            return []
        range_start = nums[0]
        range_end = nums[0]
        prev_x = nums[0]
        for x in nums[1:]:
            if x != (prev_x + 1):
                ans.append(range_to_str(range_start, range_end))
                range_start = x
                range_end = x
            else:
                range_end = x
            prev_x = x
        ans.append(range_to_str(range_start, range_end))
        return ans
