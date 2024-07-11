class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        boys = list(range(m))
        girls = list(range(n))

        def get_max(b, g):
            if len(b) == 0 or len(g) == 0:
                return 0
            i = b[0]
            m = 0  # max matches
            for j_ind, j in enumerate(g):
                # check if taking the pair (i,j) improves max
                g_without_j = g[:j_ind] + g[(j_ind + 1) :]
                max_if_match = grid[i][j] + get_max(b[1:], g_without_j)
                m = max(m, max_if_match)
            return m

        return get_max(boys, girls)
