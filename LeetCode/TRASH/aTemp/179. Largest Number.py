def largestNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    # Radix sort:
    n = len(nums)
    # index 0 = no digit
    # index 1 = 0 digit..
    n_digits = [len(str(x)) for x in nums]
    max_digit = max(n_digits)
    for i in range(max_digit):
        # do a bucket-sort according to the i-th place digit from start
        ql = [[] for i in range(11)]
        for k, a in enumerate(nums):
            # we are looking for a digit index from left to right
            digit_to_look = i - (max_digit - n_digits[k])
            if digit_to_look < 0:
                # in this case this number doen't have this digit index
                ql[10].append(a)
            else:
                d = (a // 10 ** (digit_to_look)) % 10
                ql[d].append(a)
        print(ql)
        nums = []
        for q in ql:
            nums += q
        print(nums)
        n_digits = [len(str(x)) for x in nums]
    outStr = ''
    # go reverse since sorted in increasing order;
    for k in range(n-1,-1,-1):
        outStr += str(nums[k])
    return outStr



self = None
nums = [3,30,34,5,9]
print( largestNumber(self, nums))