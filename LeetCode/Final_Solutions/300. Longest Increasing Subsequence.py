

def lengthOfLIS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n == 0: return 0
    # seq_len[i] = The maximal increasing seq len which ends at i
    seq_len = [0 for _ in range(n)]
    seq_len[0] = 1

    for i in range(1, n):
        seq_len_c = 1
        for j in range(0, i):
            if nums[i] > nums[j] and (seq_len[j] + 1) > seq_len_c:
                seq_len_c = (seq_len[j] + 1)
        seq_len[i] = seq_len_c
    print(seq_len)
    return max(seq_len)



#==============================================================================================#
self = None
# nums = [10,9,2,5,3,7,101,18]
nums = [-2,-1]
print(lengthOfLIS(self, nums))