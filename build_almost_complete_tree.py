#
# class Node:
#     def __init__(self, key=None, data=None):
#         self.key = key
#         self.data = data
#         self.left = None
#         self.right = None
#
import math

from TreeClass3 import TreeNode


def build_complete_tree(h):
    if h == -1:
        return None
    v = TreeNode(0)
    v.left = build_complete_tree(h - 1)
    v.right = build_complete_tree(h - 1)
    return v


def is_leaf(t):
    return t and t.right is None and t.left is None


def delete_k_rightmost_leaves(v: TreeNode, tree_depth: int, k: int, depth: int = 0):
    if k <= 0:
        return 0, False
    if tree_depth == depth:
        # reached leaf of original tree and k>=1  - so delete node
        del v
        return 1, True
    n_deleted_r, is_r_deleted = delete_k_rightmost_leaves(v.right, tree_depth, k, depth + 1)
    if is_r_deleted:
        v.right = None
    n_deleted_l, is_l_deleted = delete_k_rightmost_leaves(v.left, tree_depth, k - n_deleted_r, depth + 1)
    if is_l_deleted:
        v.left = None
    return n_deleted_r + n_deleted_l, False


def build_almost_complete_tree(n):
    print('n = ', n)
    h = math.ceil(math.log2(n)) - 1
    print('h =', h)
    t = build_complete_tree(h)
    n_nodes_in_complete_tree = 2 ** (h + 1) - 1
    n_leaves_to_delete = n_nodes_in_complete_tree - n
    print('n_leaves_to_delete', n_leaves_to_delete)
    delete_k_rightmost_leaves(t, h, n_leaves_to_delete)
    return t


###################################

if __name__ == "__main__":
    n = 5
    t = build_almost_complete_tree(n)
    t.display()
