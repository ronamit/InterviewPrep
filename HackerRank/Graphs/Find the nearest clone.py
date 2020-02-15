from collections import deque


# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # solve here
    adj_list = [[] for _ in range(graph_nodes)]
    for i, u  in enumerate(graph_from):
        adj_list[u-1].append(graph_to[i]-1)
        adj_list[graph_to[i] - 1].append(u - 1)
    minDist = -1
    # print(adj_list)
    for s in range(graph_nodes):
        if ids[s] == val:
            # print('S:', s+1)
            # Run BFS
            visited = [False for _ in range(graph_nodes)]
            q = deque([(s, 0)])
            visited[s] = True
            while q:
                (u, d) = q.popleft()
                # print('u: ', u+1)
                for v in adj_list[u]:
                    if not visited[v]:
                        visited[v] = True
                        vd = d+1  # distance of v from s
                        q.append((v, vd))
                        if ids[v] == val:
                            print((s,v), vd)
                            if minDist == -1 or vd < minDist:
                                minDist = vd
    return minDist

graph_from = [1, 1, 2, 3]
graph_to = [2,3,4,5]
ids = [1,2,3,3,2]
val = 2
graph_nodes = 5
print(findShortest(graph_nodes, graph_from, graph_to, ids, val))
