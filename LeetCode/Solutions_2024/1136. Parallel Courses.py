from typing import List

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        # Idea: find the longest path in the graph

        # create graph adjeceny list
        out_edges = [[] for _ in range(n)]
        in_edges =  [[] for _ in range(n)]
        for pair in relations:
            out_edges[pair[0] - 1].append(pair[1] - 1)
            in_edges[pair[1] - 1].append(pair[0] - 1)


        # toplogical sort
        in_deg = [len(e) for e in in_edges]
        sources = [i for i in range(n) if in_deg[i] == 0]
        if len(sources) == 0:
            return -1
        nodes_order = []
        while sources:
            s = sources.pop()
            nodes_order.append(s)
            # reduce the in_deg of each of the childs
            for c in out_edges[s]:
                in_deg[c] -= 1
                if in_deg[c] == 0:
                    sources.append(c)
                
        n_ordered = len(nodes_order)
        if n_ordered < n:
            # no toplogical order is possible - there is a cycle
            return -1
        # find max path
        max_path_from_node = [None for _ in range(n)]
        for i in nodes_order[::-1]:
            cur_max = 1
            for c in out_edges[i]:
                cur_max = max(cur_max, 1 + max_path_from_node[c])
            max_path_from_node[i] = cur_max
        return max(max_path_from_node)
            
            
sol = Solution()
ans = sol.minimumSemesters(5, [[1,2],[3,4],[4,5],[5,2]])
print(ans)