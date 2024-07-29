# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: list[list[int]]) -> TreeNode:

        all_vals = set()
        for v_parent, v_child, _ in descriptions:
            all_vals.add(v_parent)
            all_vals.add(v_child)

        all_vals = list(all_vals)
        n = len(all_vals)  # number of nodes

        val_to_ind = {v: i for i, v in enumerate(all_vals)}

        parents = [None for _ in range(n)]
        childs = [[None, None] for _ in range(n)]

        for v_parent, v_child, is_left in descriptions:
            i_parent = val_to_ind[v_parent]
            i_child = val_to_ind[v_child]
            parents[i_child] = i_parent
            childs[i_parent][1 - is_left] = i_child

        def create_tree(i_root: int):
            v_root = all_vals[i_root]
            i_left, i_right = childs[i_root]
            t_left = create_tree(i_left) if i_left is not None else None
            t_right = create_tree(i_right) if i_right is not None else None
            t = TreeNode(val=v_root, left=t_left, right=t_right)
            return t

        # the root is the only one without parent
        i_root = next(i for i, p in enumerate(parents) if p is None)

        return create_tree(i_root)
