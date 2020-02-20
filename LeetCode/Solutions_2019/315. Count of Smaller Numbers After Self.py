class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.right = None
        self.left = None

def countSmaller(self, nums):
    # TODO: balance the tree in each insert - to get O(nlogn) in worst case
    n = len(nums)
    count = [0] * n
    def update_and_count(t, key):
        if t is None:
            return TreeNode(key, 1), 0
        t.val += 1
        if t.left is None:
            l_val = 0
        else:
            l_val = t.left.val
        # if key == t.key:
        #     # in this case we just add a count to the node - no need to create a new node
        #     return t, l_val
        # TODO: handle the key == t.key with counting duplicates
        if key <= t.key:
            next_t, next_val = update_and_count(t.left, key)
            t.left = next_t
            return t, next_val
        elif key > t.key:
            next_t, next_val = update_and_count(t.right, key)
            t.right = next_t
            return t, next_val + l_val + 1
    # go from right to left in nums
    # add the number to the tree and count how many elements are smaller than the inserted num
    # and also update the extra info field - how many nodes in sub-tree of each node
    #
    root = None
    for i in range(n-1,-1,-1):
        root, cc = update_and_count(root, nums[i])
        count[i] = cc
        # root.display(showVal=True)
        # print('searched = ' + str(nums[i]))
        # print('count = ' + str(count[i]))
        # print('-'*100)
    return count




self = None
nums = [5,2,6,1]
print(countSmaller(self, nums))

#
#
# def countSmaller(self, nums):
#     n = len(nums)
#     count = [0] * n
#     for i in range(n):
#         for k in range(i + 1, n):
#             count[i] += (nums[k] < nums[i])
#     return count