
def criticalConnections(self, n: int, connections):
    def edge_pair(e):
        return (min(e), max(e))

    # prepare adjacency list:
    adj = [[] for i in range(n)]
    for e in connections:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])

    is_critical = {}
    for e in connections:
        is_critical[edge_pair(e)] = True

    is_visited_edge = {}
    for e in connections:
        is_visited_edge[edge_pair(e)] = False

    visited = [False for i in range(n)]

    def DFS(s, stk):
        if not visited[s]:
            visited[s] = True
            for v in adj[s]:
                edge = edge_pair([s,v])
                if not is_visited_edge[edge]:
                    is_visited_edge[edge] = True
                    DFS(v, stk + [v])
        else:  # s was already visited
            # in this case we got back to s by going on a circuit
            # we need to mark all the corresponding
            # edges in the circuit as “not critical”

            # now stk contains s as the last element
            # we need to start from the previous one and go back until we find s again
            # (and the circuit is completed)
            u = stk[-1]
            for v in stk[-2::-1]:
                # mark {u,v} as not critical
                e = [u, v]
                is_critical[edge_pair(e)] = False
                u = v
                if v == s:
                    break # circuit is completed
    DFS(0, [0])
    output = []
    for e in connections:
        if is_critical[edge_pair(e)]:
            output.append(e)
    return output



n = 6
connections = [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]

# n = 4
# connections = [[0,1],[1,2],[2,0],[1,3]]
self = None
print(criticalConnections(self, n, connections))