# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeQueries(self, root: TreeNode, queries: list[int]) -> list[int]:

        #  list per depth of the nodes in this depth, and their height
        nodes_per_depth = {}  # depth: (height ,val)
        height_per_node = {}  # val: height
        node_to_depth = {}  # val: depth
        node_to_height = {}

        def get_level_heights(node: TreeNode, node_depth):
            if node is None:
                return
            left_height = 0
            right_height = 0
            if node.left:
                get_level_heights(node.left, node_depth + 1)
                left_height = height_per_node[node.left.val]
            if node.right:
                get_level_heights(node.right, node_depth + 1)
                right_height = height_per_node[node.right.val]
            node_height = 1 + max(left_height, right_height)
            height_per_node[node.val] = node_height
            if node_depth not in nodes_per_depth:
                nodes_per_depth[node_depth] = []
            nodes_per_depth[node_depth].append((node_height, node.val))
            node_to_depth[node.val] = node_depth
            node_to_height[node.val] = node_height

        get_level_heights(root, 0)

        # for depth level, find the two hieghst nodes
        heighest_per_depth = {}  # depth: [most_high_val, second_high_val]
        for depth, nodes in nodes_per_depth.items():
            max_height_node = max(nodes)  # (height, val)
            heighest_per_depth[depth] = [max_height_node[1]]
            if len(nodes) > 1:
                # get the second hieghst
                second_heighest = max(
                    [node for node in nodes if node != max_height_node],
                )  # (hieght, val)
                heighest_per_depth[depth].append(second_heighest[1])

        print(heighest_per_depth)
        ans = []
        original_height = node_to_height[root.val]
        for query in queries:
            query_depth = node_to_depth[query]
            highest_node_in_depth = heighest_per_depth[query_depth][0]
            if query != highest_node_in_depth:
                # no change to tree height
                ans.append(original_height - 1)
            elif len(heighest_per_depth[query_depth]) > 1:
                # query is the highest but after its removal the tree height is set by the second hieghts
                second_heightst_node = heighest_per_depth[query_depth][1]
                ans.append(query_depth + node_to_height[second_heightst_node] - 1)
            else:
                # no additional node in this level
                ans.append(query_depth - 1)
        return ans


# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right

# def get_tree_height(node: TreeNode, deleted_node_val: int) -> int:
#     if node is None:
#         return 0
#     left_height = 0
#     right_height = 0
#     if node.left and node.left.val != deleted_node_val:
#         left_height = get_tree_height(node.left, deleted_node_val)
#     if node.right and node.right.val != deleted_node_val:
#         right_height = get_tree_height(node.right, deleted_node_val)
#     return 1 + max(left_height, right_height)


# class Solution:
#     def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
#         # idea 2: for each node in the tree - find how many childs it has in each depth of the original tree
#         ans = []
#         prev_ans = {}
#         for query in queries:
#             if query in prev_ans:
#                 cur_ans =  prev_ans[query]
#             else:
#                 cur_ans = get_tree_height(root, query) - 1
#             prev_ans[query] = cur_ans
#             ans.append(cur_ans)
#         return ans
