# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:

        to_delete_set = set(to_delete)

        def scan_tree(t: TreeNode):
            if t is None:
                return None, []
            if t.val in to_delete_set:
                return None, [t]
            l_t_pruned, l_deleted = scan_tree(t.left)
            r_t_pruned, r_deleted = scan_tree(t.right)
            t_pruned = TreeNode(val=t.val, left=l_t_pruned, right=r_t_pruned)
            deleted = l_deleted + r_deleted
            return t_pruned, deleted

        roots_list = []
        starts_stack = [root]
        while starts_stack:
            t = starts_stack.pop()
            if t is None:
                continue
            t_pruned, deleted = scan_tree(t)
            if t_pruned is not None:
                roots_list.append(t_pruned)
            for d in deleted:
                starts_stack += [d.left, d.right]
        return roots_list
