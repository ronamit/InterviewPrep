from TreeClass import TreeNode, stringToTreeNode

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def FlattenRec(t):
            if t is None:
                return None, None
            leftHead, leftTail = FlattenRec(t.left)
            rightHead, rightTail = FlattenRec(t.right)

            head = t
            p = head
            if leftHead:
                p.right = leftHead
                p.left = None
                p = leftTail
            if rightHead:
                p.right = rightHead
                p.left = None
                p = rightTail
            tail = p
            return head, tail

        FlattenRec(root)


sol = Solution()
root = stringToTreeNode("[1, null, 3, 2]")
root.display()
print('-'*20)
sol.flatten(root)
root.display()

