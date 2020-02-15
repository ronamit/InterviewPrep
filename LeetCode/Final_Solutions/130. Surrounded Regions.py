
#### easier solution: DFS on edge-'O' to mark what is connected to edge



class UnionFind:
    # Up-tree implement
    def __init__(self):
        self.parent = []
        self.size = []

    def Find(self, x):
        # find set of element is a set of sets:
        y = x
        while self.parent[y] is not None:
            y = self.parent[y]
        setId = y
        # PATH SQUEEZE:
        y = x
        while self.parent[y] is not None:
            nextY = self.parent[y]
            self.parent[y] = setId
            y = nextY
        return setId

    def Union(self, s1, s2):
        if s1 == s2:
            return
        if self.size[s1] > self.size[s2]:
            self.parent[s2] = s1
            self.size[s1] += self.size[s2]
        else:
            self.parent[s1] = s2
            self.size[s2] += self.size[s1]

    def UnionFind(self, x1, x2):
        if x1 == x2:
            return
        s1 = self.Find(x1)
        s2 = self.Find(x2)
        self.Union(s1, s2)

    def MakeSet(self):
        # add element, it is a new set with index == length of list (before extension)
        elemKey = len(self.parent)
        self.parent.append(None)
        self.size.append(1)
        return elemKey

#
# # Naive (inefficent) implment:
# class UnionFind:
#     def __init__(self):
#         self.sets = set()
#     def Find(self, x):
#         # find set of element is a set of sets:
#         for s in self.sets:
#             if x in s:
#                 return s
#         return None
#     def UnionFind(self, x1, x2):
#         if x1 == x2:
#             return
#         s1 = self.Find(x1)
#         s2 = self.Find(x2)
#         if s1 == s2:
#             return
#         self.sets.add(s1.union(s2))
#         self.sets.remove(s1)
#         self.sets.remove(s2)
#     def MakeSet(self, x):
#         self.sets.add(frozenset([x]))


def solve(self, board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    m = len(board)
    if m == 0: return
    n = len(board[0])
    counter = 1
    # set of regions
    # group with '1' in it: those which touch edge
    sets = UnionFind()
    edgesSetKey = sets.MakeSet()
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'X':
                continue
            if i == 0 or j == 0 or i == m-1 or j == n-1:
                if board[i][j] == 'O':
                    board[i][j] = edgesSetKey
                else:
                    # add to set of reigons that touch edges:
                    sets.UnionFind(edgesSetKey, board[i][j])
            if board[i][j] == 'O':
                newSetKey = sets.MakeSet()
                board[i][j] = newSetKey
            mark = board[i][j]
            dirs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
            for dir in dirs:
                i2 = i + dir[0]
                j2 = j + dir[1]
                if i2 < 0 or i2>=m or j2<0 or j2>= n or board[i2][j2] == 'X':
                    continue
                if board[i2][j2] == 'O':
                    board[i2][j2] = mark
                else:
                    sets.UnionFind(board[i2][j2], mark)
    # for r in board:
    #     print(r)
    # print(sets)

    for i in range(m):
        for j in range(n):
            if board[i][j] == 'X':
                continue
            if sets.Find(board[i][j]) == sets.Find(edgesSetKey):
                board[i][j] = 'O'
            else:
                board[i][j] = 'X'
    return

self = None
# board = [["X","X","X","X"],
#          ["X","O","O","X"],
#          ["X","X","O","X"],
#          ["X","O","O","X"]]
board = \
[["X","O","O","X","X","X","O","X","O","O"],["X","O","X","X","X","X","X","X","X","X"],["X","X","X","X","O","X","X","X","X","X"],["X","O","X","X","X","O","X","X","X","O"],["O","X","X","X","O","X","O","X","O","X"],["X","X","O","X","X","O","O","X","X","X"],["O","X","X","O","O","X","O","X","X","O"],["O","X","X","X","X","X","O","X","X","X"],["X","O","O","X","X","O","X","X","O","O"],["X","X","X","O","O","X","O","X","X","O"]]
for row in board:
    print(row)
print('-'*100)
solve(self, board)
for row in board:
    print(row)


#
#
# # Naive (inefficent) implment:
# class UnionFind:
#     def __init__(self):
#         self.sets = set()
#
#     def Find(self, x):
#         # find set of element is a set of sets:
#         for s in self.sets:
#             if x in s:
#                 return s
#         return None
#
#     def UnionFind(self, x1, x2):
#         if x1 == x2:
#             return
#         s1 = self.Find(x1)
#         s2 = self.Find(x2)
#         if s1 == s2:
#             return
#         self.sets.add(s1.union(s2))
#         self.sets.remove(s1)
#         self.sets.remove(s2)
#
#
#     def MakeSet(self, x):
#         self.sets.add(frozenset([x]))
#
#
# def solve(self, board):
#     """
#     :type board: List[List[str]]
#     :rtype: void Do not return anything, modify board in-place instead.
#     """
#     m = len(board)
#     if m == 0: return
#     n = len(board[0])
#     counter = 1
#     # set of regions
#     # group with '1' in it: those which touch edge
#     sets = UnionFind()
#     sets.MakeSet('1')
#     for i in range(m):
#         for j in range(n):
#             if board[i][j] == 'X':
#                 continue
#             if i == 0 or j == 0 or i == m-1 or j == n-1:
#                 if board[i][j] == 'O':
#                     board[i][j] = '1'
#                 else:
#                     # add to set of reigons that touch edges:
#                     sets.UnionFind('1', board[i][j])
#             if board[i][j] == 'O':
#                 counter += 1
#                 mark = str(counter)
#                 sets.MakeSet(mark)
#                 board[i][j] = mark
#             else:
#                 mark = board[i][j]
#             dirs = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
#             for dir in dirs:
#                 i2 = i + dir[0]
#                 j2 = j + dir[1]
#                 if i2 < 0 or i2>=m or j2<0 or j2>= n or board[i2][j2] == 'X':
#                     continue
#                 if board[i2][j2] == 'O':
#                     board[i2][j2] = mark
#                 else:
#                     sets.UnionFind(board[i2][j2], mark)
#     # for r in board:
#     #     print(r)
#     # print(sets)
#     edgesMarks = sets.Find('1')
#     for i in range(m):
#         for j in range(n):
#             if board[i][j] == 'X':
#                 continue
#             if board[i][j] in edgesMarks:
#                 board[i][j] = 'O'
#             else:
#                 board[i][j] = 'X'
#     return
#
# self = None
# # board = [["X","X","X","X"],
# #          ["X","O","O","X"],
# #          ["X","X","O","X"],
# #          ["X","O","X","X"]]
# board = \
# [["X","O","O","X","X","X","O","X","O","O"],["X","O","X","X","X","X","X","X","X","X"],["X","X","X","X","O","X","X","X","X","X"],["X","O","X","X","X","O","X","X","X","O"],["O","X","X","X","O","X","O","X","O","X"],["X","X","O","X","X","O","O","X","X","X"],["O","X","X","O","O","X","O","X","X","O"],["O","X","X","X","X","X","O","X","X","X"],["X","O","O","X","X","O","X","X","O","O"],["X","X","X","O","O","X","O","X","X","O"]]
# solve(self, board)
# for row in board:
#     print(row)
