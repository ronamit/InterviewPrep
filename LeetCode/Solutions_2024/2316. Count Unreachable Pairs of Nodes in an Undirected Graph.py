class Solution:
    from typing import List

    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # idea: 1. find the sizes of connected components, 2. compute the answer

        # create adjecency list
        adj = [[] for _ in range(n)]
        for e in edges:
            adj[e[0]].append(e[1])
            adj[e[1]].append(e[0])

        # run DFS from each node, counting how many are connected
        visited = [False for _ in range(n)]

        def dfs_count(i):
            if visited[i]:
                return 0
            cnt = 1
            visited[i] = True
            for j in adj[i]:
                if not visited[j]:
                    cnt += dfs_count(j)
            return cnt

        comp_sizes = []
        for i in range(n):
            if not visited[i]:
                comp_sizes.append(dfs_count(i))

        n_comp = len(comp_sizes)
        if n_comp == 1:
            # one connected comp - all nodes are connected
            return 0

        # go over all pairs of componenets
        # for i1 in range(n_comp):
        #     for i2 in range(i1 + 1, n_comp):
        #         cnt += comp_sizes[i1] * comp_sizes[i2]

        # more efficent calculation O(n_comp) - using law of distribution
        #  sum_i sum_j c_i c_j =  (sum_i c_i) (sum_j c_j)
        # so  sum_i sum_{j > i} c_i c_j =  0.5 * [(sum_i c_i) **2 - sum {c_i^2}]
        cnt = 0.5 * (pow(sum(comp_sizes), 2) - sum([c**2 for c in comp_sizes]))
        cnt = int(cnt)

        # note: simpler solution:
        #         for (int i = 0; i < n; i++) {
        #     if (!visit[i]) {
        #         sizeOfComponent = bfs(i, adj, visit);
        #         numberOfPairs += sizeOfComponent * (remainingNodes - sizeOfComponent);
        #         remainingNodes -= sizeOfComponent;
        #     }
        # }
        # return cnt
