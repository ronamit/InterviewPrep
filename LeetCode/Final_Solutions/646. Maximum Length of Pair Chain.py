class Solution:
    def findLongestChain(self, pairs) -> int:
        n = len(pairs)
        # sort by first value of pair:
        pairs.sort(key=lambda x: x[0])
        V = [1 for _ in range(n)] # maximal chain using pairs in i:n-1
        # note: V[n-1] == 0
        for i in range(n-2, -1, -1):
            # we either use this for chain or don't
            # if we don't - the V is the same as the next
            # if we do, we  need to take the V of closest a pair k>i with pairs[k][0]>pairs[i][1]
            # we find with binary search (if not found - then -1)
            vk = -1
            search_start = i+1
            first = i+1
            last = n-1
            go = True
            thresh =  pairs[i][1]
            while go and last >= first:
                k = (last + first) // 2
                if pairs[k][0] > thresh and (k == search_start or pairs[k-1][0] <= thresh):
                    vk = V[k]
                    go = False
                elif pairs[k][0] > thresh:
                    last = k-1
                else:
                    first = k + 1

            V[i] = V[i+1]
            if vk != -1:
                V[i] = max(V[i], 1+vk)
        return V[0]

sol = Solution()

#pairs = [[1,2], [2,3], [3,4]]
pairs =   [[9,10],[9,10],[4,5],[-9,-3],[-9,1],[0,3],[6,10],[-5,-4],[-7,-6]]

print(sol.findLongestChain(pairs))


# class Solution:
#     def findLongestChain(self, pairs) -> int:
#         n = len(pairs)
#         adj = [[] for _ in range(n)]
#         inDeg = [0 for _ in range(n)]
#         # create adjency list
#         for i in range(n):
#             for j in range(n):
#                 if i != j and pairs[i][1] < pairs[j][0]:
#                     adj[i].append(j)
#                     inDeg[j] += 1
#
#         # toplocical ordering
#         sources = []
#         for i in range(n):
#             if inDeg[i] == 0:
#                 sources.append(i)
#         ind = 0
#         order = [0 for _ in range(n)]
#         while sources:
#             s = sources.pop()
#             order[ind] = s
#             ind += 1
#             for j in adj[s]:
#                 inDeg[j] -= 1
#                 if inDeg[j] == 0:
#                     sources.append(j)
#         # dynamic programming to find longes chain (directed path in graph)
#         order.reverse()
#         V = [1 for _ in range(n)]
#         for k in order:
#             maxLen = 1 # length in vertices
#             for j in adj[k]:
#                 maxLen = max(maxLen, 1 + V[j])
#             V[k] = maxLen
#         return max(V)
