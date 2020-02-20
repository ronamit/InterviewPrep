from TreeClass import TreeNode, stringToTreeNode


def zigzagLevelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
    # Run BFS
    from collections import deque
    q = deque([(root, 0)])
    outlist = []
    while q:
        # print([a[0].val if a[0] else 'None' for a in q])
        p, h = q.popleft()
        if p is None:
            continue
        if len(outlist) <= h:
            outlist.append([p.val])
        else:
            outlist[h] += [p.val]
        q.append((p.left, h + 1))
        q.append((p.right, h + 1))
    for i in range(1, len(outlist), +2):
        outlist[i].reverse()
    return outlist

self = None
input = '[3,9,20,null,null,15,7]'
root = stringToTreeNode(input)
root.display()
print(zigzagLevelOrder(self, root))