#see: https://www.geeksforgeeks.org/largest-rectangle-under-histogram/

def largestRectangleArea(self, heights):

    def update_area(stk, max_area, right_ind):
        # calcute the max area when the popped bar as the left index -
        # since the stack in ascending height order heights[i_poped] is the height of the box
        # the right index is one index before the current index (since its height is smaller)
        # the left index - is one after the previous item in stk (also since its height is smaller)
        i_poped = stk.pop()
        if stk:
            left_ind = stk[-1] + 1
        else:
            left_ind = 0
        area = (right_ind - left_ind + 1) * heights[i_poped]
        print(area)
        max_area = max(max_area, area)
        return stk, max_area


    n = len(heights)
    max_area = 0
    stk = []
    # the stack will keep for each height - how far back (from which index) can we go with this height
    i = 0
    while i < n:
        h = heights[i]
        max_area = max(max_area, h) # option for a single bar
        if not stk or heights[stk[-1]] < h:
            stk.append(i)
            i += 1
        else:
            # if the top-in-stack bin is higher than h - we can discard it
            # print([(a,heights[a]) for a in stk])
            stk, max_area = update_area(stk, max_area, i-1)

    # Treat remaining:
    while stk:
        # print([(a, heights[a]) for a in stk])
        stk, max_area = update_area(stk, max_area, n-1)


    return max_area

self = None
heights =  [6, 2, 5, 4, 5, 1, 6]
# heights = [1,2,3,4,5]
print(largestRectangleArea(self, heights))

