# Complete the largestRectangle function below.
def largestRectangle(h):
    s = []
    n = len(h)
    maxRect  = 0
    for i in range(n):
        i_start = i
        # while currrent h is smaller than the top of stack:
        while s and h[i] < s[-1][0]:
            hp, ip = s.pop()
            i_start = ip
            d = (i-1) - ip + 1
            area = hp * d
            maxRect = max(maxRect, area)
        s.append((h[i], i_start))
    while s:
        hp, ip = s.pop()
        d = n-1 - ip + 1
        area = hp * d
        maxRect = max(maxRect, area)
    return maxRect

h = [6320, 6020, 6098, 1332, 7263, 672, 9472, 2838, 3401, 9494]
# # h = [5,4,3,2,1]
print(largestRectangle(h))


#
# def largestRectangle(h):
#     i = 0
#     j = len(h) - 1
#     maxRect = 0
#     while j >= i:
#         range_h = [h[u] for u in range(i,j+1)]
#         cur_h = min(range_h)
#         cur_area =  cur_h * (j-i+1)
#         print((i,j), cur_area)
#         maxRect = max(maxRect, cur_area)
#         if h[i] < h[j]:
#             i += 1
#         else:
#             j -= 1
#     return maxRect