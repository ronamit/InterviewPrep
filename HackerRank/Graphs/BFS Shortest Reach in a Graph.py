'''
https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs
'''


class Graph:
    def __init__(self, n):
        self.n = n
        self.edges = [[] for _ in range(n)]

    def connect(self, u, v):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def find_all_distances(self, s: int):
        stk = [s]
        visited = {s}
        d = [-1 for _ in range(self.n)]
        d[s] = 0
        edge_len = 6
        while stk:
            u = stk.pop()
            for v in self.edges[u]:
                if v not in visited:
                    d[v] = d[u] + edge_len
                    stk.append(v)
                    visited.add(v)
        del d[s]
        return d


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x - 1, y - 1)
    s = int(input())
    distances = graph.find_all_distances(s - 1)
    print(' '.join([str(x) for x in distances]))

