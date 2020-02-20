from TreeClass import TreeNode, build_tree

# def sortedArrayToBST(self, nums):
#     """
#     :type nums: List[int]
#     :rtype: TreeNode
#     """
#
#     def CreateTree(arr):
#         n = len(arr)
#         if n == 0: return None
#         t = TreeNode(arr[n // 2])
#         t.left = CreateTree(arr[:n // 2])
#         t.right = CreateTree(arr[n // 2 + 1:])
#         return t
#
#     return CreateTree(nums)


def sortedArrayToBST(self, nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """

    def CreateTree(start, end):
        n = end - start
        if n == 0: return None
        t = TreeNode(nums[start + n // 2])
        t.left = CreateTree(start, start + n // 2 )
        t.right = CreateTree(start+n // 2 + 1, end)
        return t

    n = len(nums)
    return CreateTree(0, n)

self = None
nums = [-10,-3,0,5,9]
t = sortedArrayToBST(self, nums)
t.display()