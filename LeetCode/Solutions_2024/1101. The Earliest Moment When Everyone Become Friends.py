from typing import List

class UnionFind:

    def __init__(self, n: int):
        self.up_tree = list(range(n))
        self.class_size = [1 for _ in range(n)]
        self.n_classes = n

    def find(self, x: int) -> int:
        # go up the tree to the root, keep list of visited nodes to point them at root
        a = x
        path = [a]
        while self.up_tree[a] != a:
            path.append(a)
            a = self.up_tree[a]
        for p in path:
            self.up_tree[p] = a
        return a

    def union(self, root1: int, root2: int):
        if self.find(root1) == self.find(root2):
            return
        self.n_classes -= 1
        # merge the smaller class into the larger
        if self.class_size[root1] < self.class_size[root2]:
            self.class_size[root2] += self.class_size[root1]
            self.up_tree[root1] = root2
        else:
            self.class_size[root1] += self.class_size[root2]
            self.up_tree[root2] = root1

    def connect(self, x: int, y: int) -> int:
        self.union(self.find(x), self.find(y))


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        # Sort the logs by time stamp (if needed?)
        logs.sort(key=lambda log: log[0])

        uf = UnionFind(n)

        # Create a Union-Find with up-trees using array:
        # in init, each node a singleton class

        for log in logs:
            t, x, y = log
            # connect x and y Union(Find(x), Find(y))
            uf.connect(x, y)
            if uf.n_classes == 1:
                return t
        return -1
