# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        def pathSumAux(t, hist_sum):
            if t is None:
                return []
            hist_sum = hist_sum + t.val
            if not t.left and not t.right:
                if hist_sum == sum:
                    return [[t.val]]
                else:
                    return []
            else:
                l_paths = pathSumAux(t.left, hist_sum)
                r_paths = pathSumAux(t.right, hist_sum)
                # add current node to paths
                paths = l_paths + r_paths
                for p in paths:
                    p.append(t.val)
                return paths

        paths = pathSumAux(root, 0)
        for p in paths:
            p.reverse()
        return paths

