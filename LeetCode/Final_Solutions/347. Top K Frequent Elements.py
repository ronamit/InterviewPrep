def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    # counts dictionary:
    cd = {}
    for a in nums:
        if a in cd:
            cd[a] += 1
        else:
            cd[a] = 0
    print(cd)
    counts = list(cd.values())
    counts.sort()
    thresh = counts[-k]
    out_lst = []
    for a in cd.keys():
        if cd[a] >= thresh:
            out_lst += [a]
    return out_lst






self = None
nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(self, nums, k))
