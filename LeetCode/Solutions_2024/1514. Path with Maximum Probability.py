import heapq
import math


class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:

        adj_list = [[] for _ in range(n)]
        neg_log_probs = [math.log(1 / prob) for prob in succProb]
        for i_edge, edge in enumerate(edges):
            adj_list[edge[0]].append((edge[1], neg_log_probs[i_edge]))
            adj_list[edge[1]].append((edge[0], neg_log_probs[i_edge]))

        # use Dijkstra's algorithm to find path with min weight from start to end
        # weight_{i,j} = -log(prob(i->j))

        # init min-heap with infinity to all nodes except start_node
        nodes_dists_dict = {node: float("inf") for node in range(n)}
        nodes_dists_dict[start_node] = 0
        nodes_dists_heap = [(float("inf"), i) for i in range(n) if i != start_node]
        heapq.heappush(nodes_dists_heap, (0, start_node))

        while nodes_dists_heap:
            dist, node = heapq.heappop(nodes_dists_heap)
            for neig_node, edge_weight in adj_list[node]:
                proposed_dist = dist + edge_weight
                if proposed_dist < nodes_dists_dict[neig_node]:
                    nodes_dists_dict[neig_node] = proposed_dist
                    heapq.heappush(nodes_dists_heap, (proposed_dist, neig_node))
        if nodes_dists_dict[end_node] == float("inf"):
            return 0
        return math.exp(-nodes_dists_dict[end_node])
