"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> 'List[List[int]]':
        outList = []
        if root == None: return []
        q = deque()
        q.append((root, 0))
        while q:
            t, h = q.popleft()
            for c in  t.children:
                q.append((c, h+1))
            if h >= len(outList):
                outList.append([t.val])
            else:
                outList[h] += [t.val]
        return outList