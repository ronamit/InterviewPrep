class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:

        # adjacency list:
        out_edges = [[] for _ in range(n)]
        in_edges = [[] for _ in range(n)]
        any_edge = [[] for _ in range(n)]
        n_edges = len(edges)
        for e in edges:
            a, b = e
            out_edges[a].append(b)
            in_edges[b].append(a)
            any_edge[a].append(b)
            any_edge[b].append(a)

        # In a tree |E| = |V| - 1  (if more - must be a cycle, if less - not connected)
        if n_edges != n - 1:
            return False
        

        # check connectivity in the underlying undirected graph
        visited = [False for _ in range(n)]

        def dfs_count(i: int) -> int:
            nonlocal visited, any_edge
            visited[i] = True
            count = 1
            for j in any_edge[i]:
                if not visited[j]:
                    count += dfs_count(j)
            return count

        is_connected = dfs_count(0) == n
        return is_connected
