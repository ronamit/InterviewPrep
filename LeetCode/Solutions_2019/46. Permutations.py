def sort_part(nums, j):
    # we use a trick to sort in-place, only the values  j+1,..,n
    n = len(nums)
    range_vals = max(nums) - min(nums)
    for k in range(j + 1):
        nums[k] -= (n - k) * 10 * range_vals
    nums.sort()
    for k in range(j + 1):
        nums[k] += (n - k) * 10 * range_vals
    return


def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """

    n = len(nums)
    if n == 1:
        return
    # start with j=n-2 and go down to 0,
    # swap nums[j] with the next in ascending order (which is right of j) and sort the part right of j.
    # if you don't succeed [no next in order right to j] go down j = j -1
    # if you don't succeed in any j -return sorted array
    j = n - 2
    while j >= 0:
        next_val = nums[j]
        next_id = j
        found = False
        for i in range(j + 1, n):
            a = nums[i]
            if a > nums[j]:
                if found:
                    if a < next_val:
                        next_id = i
                        next_val = a
                else:
                    found = True
                    next_id = i
                    next_val = a
        if found:
            # increase nums[j] to the next in order:
            nums[j], nums[next_id] = nums[next_id], nums[j]
            # sort values right of j
            sort_part(nums, j)
            return nums
        else:
            j -= 1
    nums.sort()
    return nums


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = [nums]
        n = len(nums)
        for i in range(math.factorial(n) - 1):
            nums = copy.deepcopy(nums)
            nextPermutation(nums)
            out += [nums]
        return out
