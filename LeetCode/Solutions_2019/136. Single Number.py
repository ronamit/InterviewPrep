def singleNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    out = 0
    for a in nums:
        # XOR:
        out ^= a
    return  out


self = None
nums = [4,1,2,1,2]
print(singleNumber(self, nums))