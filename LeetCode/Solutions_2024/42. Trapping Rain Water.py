class Solution:
    def trap(self, height: list[int]) -> int:
        trapped_water = 0
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        left_max[0] = height[0]
        for i in range(n - 1):
            left_max[i] = max(left_max[i - 1], height[i])
        right_max[-1] = height[-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        for i in range(1, n - 1):
            trapped_water += min(left_max[i], right_max[i]) - height[i]
        return trapped_water



# class Solution:
#     def trap(self, height: list[int]) -> int:
#         trapped_water = 0
#         n = len(height)
#         prev_water = [False for _ in range(n)]
#         prev_terrain = [True for _ in range(n)]
#         max_height = max(height)
#         for cur_height in range(1, max_height + 1):
#             cur_terrain = [h >= cur_height for h in height]
#             # check for each index of it (maybe) can trap water
#             cur_water = [None for _ in range(n)]
#             # note: the fist and last index can't trap water
#             cur_water[0] = False
#             cur_water[-1] = False
#             for i in range(1, n - 1):
#                 cur_water[i] = (prev_terrain[i] or prev_water[i]) and not cur_terrain[i]
#             # now we go from the sides and "eliminate" water boxes that are not supported from sides
#             for i in range(1, n - 1):
#                 if not cur_terrain[i] and not cur_water[i - 1] and not cur_terrain[i - 1]:
#                     cur_water[i] = False
#             for i in range(n - 2, 0, -1):
#                 if not cur_terrain[i] and not cur_water[i + 1] and not cur_terrain[i + 1]:
#                     cur_water[i] = False
#             trapped_water += sum(cur_water)
#             # print([int(x) for x in cur_water])
#             prev_water = cur_water
#             prev_terrain = cur_terrain
#         return trapped_water
