# class Solution:
#     def maximumInvitations(self, grid: List[List[int]]) -> int:
#         m = len(grid)
#         n = len(grid[0])
#         boys = list(range(m))
#         girls = list(range(n))

#         def get_max(b, g):
#             if len(b) == 0 or len(g) == 0:
#                 return 0
#             i = b[0]
#             m = 0  # max matches
#             for j_ind, j in enumerate(g):
#                 # check if taking the pair (i,j) improves max
#                 g_without_j = g[:j_ind] + g[(j_ind + 1) :]
#                 max_if_match = grid[i][j] + get_max(b[1:], g_without_j)
#                 m = max(m, max_if_match)
#             return m

#         return get_max(boys, girls)

# https://www.geeksforgeeks.org/maximum-bipartite-matching/
# https://leetcode.com/problems/maximum-number-of-accepted-invitations/solutions/1978859/python-hungarian-algorithm-easy-to-understand/

from typing import List

class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        matches = {}  # Stores matches formed. key = girl, value = boy.

        def dfs(boy: int, visited: set) -> bool:
            """A depth first search function to match a boy at index `boy` with potential girls.

            DFS will go through all of the boy's options and choose the one that maximizes global
            optimum.
            """

            for girl in range(N):

                # Rule 1. Only ask that girl if you haven't asked her before already.
                # Rule 2. If you wish to ask a girl that's taken, she will only go with you
                #         if her current partner finds a new girl.

                if grid[boy][girl] and girl not in visited:
                    visited.add(girl)

                    if girl not in matches or dfs(matches[girl], visited):
                        matches[girl] = boy
                        return True

            return False

        for boy in range(M):
            dfs(boy, set())

        return len(matches)
