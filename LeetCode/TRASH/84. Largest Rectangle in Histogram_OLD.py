def largestRectangleArea(self, heights):
    # observation: the roof of the rectangle must contain one of the roofs of one of the bins.
    # so we can check for each bin how large is the max rect that contain it, and then take max

    #TODO: use trick with two pointers starting at 0 and n-1 .
    # use cummalative min from right and left to determine current are
    # make the window smaller by ?

    n = len(heights)
    maxarea = 0
    for i in range(n):
        # find the right and left borders:
        h = heights[i]
        right = i
        while right < n - 1:
            if heights[right+1] >= h:
                right += 1
            else:
                break
        left = i
        while left > 0:
            if heights[left-1] >= h:
                left -= 1
            else:
                break
        area = (right - left + 1) * h
        print(area)
        maxarea = max(maxarea, area)
    return maxarea

self = None
heights = [2,1,5,6,2,3]
print(largestRectangleArea(self, heights))


#
# def largestRectangleArea(self, heights):
#     # observation: the roof of the rectangle must contain one of the roofs of one of the bins.
#     # so we can check for each bin how large is the max rect that contain it, and then take max
#
#     n = len(heights)
#     maxarea = 0
#     for i in range(n):
#         # find the right and left borders:
#         h = heights[i]
#         right = i
#         while right < n - 1:
#             if heights[right+1] >= h:
#                 right += 1
#             else:
#                 break
#         left = i
#         while left > 0:
#             if heights[left-1] >= h:
#                 left -= 1
#             else:
#                 break
#         area = (right - left + 1) * h
#         print(area)
#         maxarea = max(maxarea, area)
#     return maxarea
