from TreeClass import TreeNode,  stringToTreeNode

def isValidBST(self, root: 'TreeNode') -> 'bool':
    # idea: in in-order scan, it should be sorted
    preval = None
    def validateRec(p):
        nonlocal preval
        if not p:
            return True
        left_ans = validateRec(p.left)
        if not left_ans:
            return False
        if preval != None and p.val <= preval:
            return False
        preval = p.val
        right_ans = validateRec(p.right)
        return right_ans
    ans = validateRec(root)
    return ans


self = None
root = stringToTreeNode('[1,1]')
# root = stringToTreeNode('[5,1,4,null,null,3,6]')
root.display()
print(isValidBST(self, root))