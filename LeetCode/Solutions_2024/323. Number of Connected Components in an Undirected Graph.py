class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        adj = [[] for _ in range(n)]
        for edge in edges:
            node1, node2 = edge
            adj[node1].append(node2)
            adj[node2].append(node1)

        visited = [False for _ in range(n)]
        n_comp = 0
        for source in range(n):
            if visited[source]:
                continue
            n_comp += 1
            # DFS
            stack = [source]
            visited[source] = True
            while stack:
                node1 = stack.pop()
                for node2 in adj[node1]:
                    if visited[node2]:
                        continue
                    visited[node2] = True
                    stack.append(node2)

        return n_comp
