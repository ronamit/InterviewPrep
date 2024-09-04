class Solution:
    def visibleMountains(self, peaks: list[list[int]]) -> int:
        n = len(peaks)

        # Monotonic Stack O(n*log(n))
        # Sort by x value
        # If a previous mountain doesn't conceal current mountain, so it can't conceal the next ones, so we can discard it
        # but we need to go in both directions, since next mountains can conceal current

        peaks = [tuple(p) for p in peaks]
        peaks.sort()
        # stack of relevant past mountains:
        stack = []

        def is_conceals(p1: tuple, p2: tuple):
            # does 1 conceals 2
            d = abs(p1[0] - p2[0])  # x-diff
            return p1[1] - d >= p2[1]

        concealed_inds = set()
        for i in range(n):
            # discard all previous that don't conceal
            while stack and not is_conceals(stack[0], peaks[i]):
                stack.pop()
            if stack:
                # exists prev that conceals
                concealed_inds.add(i)
            stack.append(peaks[i])
        # go backwards
        stack = []
        for i in range(n - 1, -1, -1):
            # discard all previous that don't conceal
            while stack and not is_conceals(stack[0], peaks[i]):
                stack.pop()
            if stack:
                # exists prev that conceals
                concealed_inds.add(i)
            stack.append(peaks[i])
        return n - len(concealed_inds)


# # Brute Force
# class Solution:
#     def visibleMountains(self, peaks: List[List[int]]) -> int:
#         n_visibles = 0
#         n = len(peaks)
#         for i in range(n):
#             is_visible = True
#             for j in range(n):
#                 if i == j:
#                     continue
#                 d = abs(peaks[i][0] - peaks[j][0])
#                 if peaks[i][1] <= peaks[j][1] - d:
#                     is_visible = False
#                     break
#             n_visibles += is_visible
#         return n_visibles
