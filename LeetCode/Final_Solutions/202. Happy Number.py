def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """
    prev_nums = {}
    seems_happy = True
    s = n
    while (seems_happy):
        x = s
        s = 0
        while (x > 0):
            s += (x % 10) ** 2
            x = x // 10
        if s == 1:
            break
        else:
            if s in prev_nums:
                seems_happy = False
            else:
                prev_nums[s] = s
    # print(prev_nums)
    return seems_happy

self = None
n = 19
print(isHappy(self, n))