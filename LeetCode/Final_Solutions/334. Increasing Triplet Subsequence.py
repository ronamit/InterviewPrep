def increasingTriplet(self, nums: 'List[int]') -> 'bool':
    n = len(nums)
    if n <= 2:
        return False
    # min_pair = min  increasing subsequence of length 2
    min_pair = None
    min_single = nums[0]
    for i in range(1, n):
        a = nums[i]
        if min_pair and a > max(min_pair):
            return True
        elif min_pair and a < min_pair[1] and a > min_pair[0]:
            min_pair = (min_pair[0], a)
        elif min_pair and a > min_single and (a < min_pair[1]):
            min_pair = (min_single, a)
        elif not min_pair and a > min_single:
            min_pair = (min_single, a)
        min_single = min(a, min_single)
    return False


self = None
nums = [1,2,-10,-8,-7]
print(increasingTriplet(self, nums))


