def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """

    # Idea: the optimal water level is some a_i
    # so we find the max-water for each level a_i
    # by finding the farthest right and farthest left we can go without spill, and take max
    # i.e, we need to check the indexes of a_j which are higher - what is the max and min j in this set
    # so we will find a ruining min and max of the indexes when going in a descending order of the ordered a_j's

    n = len(height)
    # sort the indexes (0,..,n-1) by the heights a_i
    sorted_i = sorted(range(n), key=height.__getitem__)

    # find the
    run_max = sorted_i[n-1]
    run_min = sorted_i[n-1]
    max_area = 0
    # note: we can start from n-2, since if we have a single highest lime, it can't be the level of the solution
    for k in range(n-2, -1, -1):
        i = sorted_i[k]
        level = height[i]
        run_max = max(run_max, i)
        run_min = min(run_min, i)
        # find the maximal dist for this water level:
        dist = max(run_max - i, i - run_min)
        # max area for this level:
        max_area_lvl = dist * level
        max_area = max(max_area, max_area_lvl)

    return max_area

self = None
height = [1,2,3,4,5,6,7,8,9,10]
print(maxArea(self, height))



# BRUTE FORCE
# n = len(height)
# max_area = 0
# for i in range(n):
#     for j in range(i + 1, n):
#         area = (j - i) * min(height[i], height[j])
#         max_area = max(max_area, area)
# return max_area

## wrong:
#     n = len(height)
#     # sort the indexes (0,..,n-1) by the heights a_i
#     sorted_i = sorted(range(n), key=height.__getitem__)
#     max_area = 0
#     for k in range(1,n):
#         i1 = sorted_i[k - 1]
#         i2 = sorted_i[k]
#         area = abs(i2 - i1) * min(height[i1], height[i2])
#         max_area = max(max_area, area)
#     return max_area
#
