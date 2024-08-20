# print binary tree layers

from collections import deque


def print_in_layers(root: TreeNode) -> None:
    
    q = deque([root])
    while q:
        t = q.pop()
        print(t.val)
        if t.left is not None:
            q.appendleft(t.left)
        if t.right is not None:
            q.appendleft(t.right)
        
        

def print_in_layers(root: TreeNode) -> None:
    
    q_prev = deque([root])
    stk = []
    while q_prev:
        if not q_prev:
            print()
            q_prev = list(stk)
        t = q_prev.pop()
        print(t.val)
        if t.left is not None:
            stk.append(t.left)
        if t.right is not None:
            stk.append(t.right)

            
    
