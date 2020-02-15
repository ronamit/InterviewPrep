

def nextPermutation(self, nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """

    # IDEA:
    # start with LSB, if it is not the max num, then it can be increased

    n = len(nums)
    if n == 1:
        return

    j = n - 1

    # otherwise, swap nums[j] with the next in order and sort the rest
    #start with j and go down to 0, if you don't suceed in any - return sorted array
    run_loop = True
    while j >= 0 and run_loop:
        next_val = nums[j]
        next_id = j
        found = False
        for i in range(n):
            if i == j:
                continue
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
            run_loop = False
        else:
            j -= 1

    # sort values right of j
    #### nums = nums[:j+1] + sorted(nums[j+1:])
    # we use a trick to sort in-place, only the values right of j:
    range_vals = max(nums) - min(nums)
    for k in range(j + 1):
        nums[k] -= (n - k) * 10 * range_vals
    nums.sort()
    for k in range(j + 1):
        nums[k] += (n - k) * 10 * range_vals

    return


self = None
nums = [2,1,3]
print(nums)

for _ in range(1):
    nextPermutation(self, nums)
    print(nums)


# n = len(nums)
# if n == 1:
#     return nums
# for j in range(n-1, 0, -1):
#     for i in range(j-1, 0, -1):
#         if nums[i] < nums[j]:
#             # swap
#             nums[i], nums[j] = nums[j], nums[i]
# #             return nums
#
# return sorted(nums)

