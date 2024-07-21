class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #  A directed tree is a directed acyclic graph (DAG) whose underlying undirected graph is an undirected tree (connected acyclic undirected graph.)

        # adjecancy list:
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

        # In a tree |E| = |V| - 1 
        if n_edges != n - 1:
            return False
        
        # find sources:
        sources = []
        for i in range(n):
            if len(in_edges[i]) == 0:
                sources.append(i)
        if len(sources) < 1:
            return False
        source = sources[0]

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

        is_connected = dfs_count(source) == n
        return is_connected
