# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: TreeNode) -> int:

        # recoursive function that counts the number of nodes in each subtree, and total coins in subtree

        # number of moves given root =
        # how many moves so that each child subtree has total coins  == num nodes
        # + recursive calls of the function to each of two child

        def scan_tree(r):
            if r is None:
                return 0, 0, 0
            n_nodes = 1
            n_coins = r.val
            n_moves = 0
            n_nodes_l, n_coins_l, n_moves_l = scan_tree(r.left)
            n_nodes_r, n_coins_r, n_moves_r = scan_tree(r.right)
            n_nodes += n_nodes_l + n_nodes_r
            n_coins += n_coins_l + n_coins_r
            n_moves = abs(n_nodes_l - n_coins_l) + abs(n_nodes_r - n_coins_r) + n_moves_l + n_moves_r
            return n_nodes, n_coins, n_moves

        _, _, n_moves = scan_tree(root)
        return n_moves
