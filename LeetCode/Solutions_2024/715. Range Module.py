# ----------------------------------------------------------------------------------------------------


"""
Since the range of allowed numbers is large we shouldn't use a table of all im range numbers..
Instead we should keep in memory the intervals themselves in a data structure
that allows both fast query and is ordered .
E.g.
Sorted list of all starts of segments.
Because we will merge any overlapping segments, then segments that are ordered by "start" are also ordered by "end".


"""
# ----------------------------------------------------------------------------------------------------
# Auxiliary functions
# ----------------------------------------------------------------------------------------------------


def binary_search_first(a: list, f_check):
    """ "
    we assume that if  f_check(a[i]) == True then all j>i also are True
    vice verse, if  f_check(a[i]) == False, then all j<i are False
    find the first element where check(a[i]) == True
    return None if all are False
    """
    ans = None
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if f_check(a[mid]):
            # we found a candidate to the first True
            ans = mid
            # continue search in lower indexes
            high = mid - 1
        else:
            low = mid + 1
    return ans


# ----------------------------------------------------------------------------------------------------


def binary_search_last(a: list, f_check):
    """ "
    we assume that if  f_check(a[i]) == True then all j>i also are True
    vice verse, if  f_check(a[i]) == False, then all j<i are False
    find the last element where check(a[i]) == True
    return None if all are False
    """
    ans = None
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if f_check(a[mid]):
            # we found a candidate to the first True
            ans = mid
            # continue search in higher indexes
            low = mid + 1
        else:
            high = mid - 1
    return ans


# ----------------------------------------------------------------------------------------------------


class RangeModule:
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def __init__(self):
        # We keep a list of tuples for each segment (start, end)
        # All segments are non-overlapping (we merge overlaps)
        # The list is ordered by "start" and also by "end" (since there are  no overlaps)
        self.segments = []

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def find_overlapping(self, left: int, right: int):
        # Requirements for overlap (seg[0] <= right and left <= seg[1])
        # So we need the first binary search to find the index of the last segment with seg[0] <= right (if any)
        # and the  second binary search to find the first segment with  left <= seg[1] (if any)
        # and then we the intersection of the indexes says what segments have overlap with [left,right)
        i1 = binary_search_last(self.segments, lambda seg: seg[0] <= right)
        i0 = binary_search_first(self.segments, lambda seg: seg[1] >= left)
        if i0 is None or i1 is None or i0 > i1:
            # no overlapping segments
            return None
        assert 0 <= i0 < len(self.segments)
        assert 0 <= i1 < len(self.segments)
        return (i0, i1)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def addRange(self, left: int, right: int) -> None:
        if left >= right:
            return
        # Find all overlapping segments -  and then replace them all with a single unified segments
        overlap_inds = self.find_overlapping(left, right)
        new_left = left
        new_right = right
        if overlap_inds is not None:
            # i0_overlap to  i1_overlap in  self.segments are overlapping to  [left,right)
            new_left = min(new_left, self.segments[overlap_inds[0]][0])
            new_right = max(new_right, self.segments[overlap_inds[1]][1])
            # delete pre-unification segments:
            del self.segments[overlap_inds[0] : (overlap_inds[1] + 1)]
        # add the the new segment in the correct location:
        i = binary_search_first(self.segments, lambda seg: new_left < seg[0])
        if i is None:
            # add as last:
            self.segments = [*self.segments, (new_left, new_right)]
        else:
            # add at location i
            self.segments = [*self.segments[:i], (new_left, new_right), *self.segments[i:]]

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def queryRange(self, left: int, right: int) -> bool:
        # return true if there is a ny segments that [left, right) is entirely included in it

        # # Inefficient search:
        # for seg in self.segments:
        #     if (seg[0] <= left and right <= seg[1]):
        #         print("Segment containing:", seg)
        #         return True

        if not self.segments:
            return False

        # Find first index where right <= seg[1]
        i0 = binary_search_first(self.segments, lambda seg: right <= seg[1])

        # Find last index where seg[0] <= left
        i1 = binary_search_last(self.segments, lambda seg: seg[0] <= left)

        # print("i0: ", i0, "i1:", i1)

        return i0 is not None and i1 is not None and i0 <= i1

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    def removeRange(self, left: int, right: int) -> None:
        overlap_inds = self.find_overlapping(left, right)
        if overlap_inds is None:
            return
        new_segments = []
        for i in range(overlap_inds[0], overlap_inds[1] + 1):
            seg = self.segments[i]
            if (right <= seg[0]) or (seg[1] <= left):
                new_segments.append(seg)  # no overlap
            elif seg[0] <= left and right <= seg[1]:
                # query is inside - need to create two new segments instead
                new_segments += [(seg[0], left), (right, seg[1])]
            elif right >= seg[1]:
                # remove right part of the segment
                new_segments.append((seg[0], left))
            elif left <= seg[0]:
                new_segments.append((right, seg[1]))
        # Remove old segments
        del self.segments[overlap_inds[0] : (overlap_inds[1] + 1)]
        # Add the new replacing segments:
        for seg in new_segments:
            self.addRange(left=seg[0], right=seg[1])

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ----------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    actions = [
        "RangeModule",
        "queryRange",
        "queryRange",
        "addRange",
        "addRange",
        "queryRange",
        "queryRange",
        "queryRange",
        "removeRange",
        "addRange",
        "removeRange",
        "addRange",
        "removeRange",
        "removeRange",
        "queryRange",
        "queryRange",
        "queryRange",
        "queryRange",
        "removeRange",
        "addRange",
        "removeRange",
        "queryRange",
        "addRange",
        "addRange",
        "removeRange",
        "queryRange",
        "removeRange",
        "removeRange",
        "removeRange",
        "addRange",
        "removeRange",
        "addRange",
        "queryRange",
        "queryRange",
        "queryRange",
        "queryRange",
        "queryRange",
        "addRange",
        "removeRange",
        "addRange",
        "addRange",
        "addRange",
        "queryRange",
        "removeRange",
        "addRange",
        "queryRange",
        "addRange",
        "queryRange",
        "removeRange",
        "removeRange",
        "addRange",
        "addRange",
        "queryRange",
        "queryRange",
        "addRange",
        "addRange",
        "removeRange",
        "removeRange",
        "removeRange",
        "queryRange",
        "removeRange",
        "removeRange",
        "addRange",
        "queryRange",
        "removeRange",
        "addRange",
        "addRange",
        "queryRange",
        "removeRange",
        "queryRange",
        "addRange",
        "addRange",
        "addRange",
        "addRange",
        "addRange",
        "removeRange",
        "removeRange",
        "addRange",
        "queryRange",
        "queryRange",
        "removeRange",
        "removeRange",
        "removeRange",
        "addRange",
        "queryRange",
        "removeRange",
        "queryRange",
        "addRange",
        "removeRange",
        "removeRange",
        "queryRange",
    ]
    inputs = [
        [],
        [21, 34],
        [27, 87],
        [44, 53],
        [69, 89],
        [23, 26],
        [80, 84],
        [11, 12],
        [86, 91],
        [87, 94],
        [34, 52],
        [1, 59],
        [62, 96],
        [34, 83],
        [11, 59],
        [59, 79],
        [1, 13],
        [21, 23],
        [9, 61],
        [17, 21],
        [4, 8],
        [19, 25],
        [71, 98],
        [23, 94],
        [58, 95],
        [12, 78],
        [46, 47],
        [50, 70],
        [84, 91],
        [51, 63],
        [26, 64],
        [38, 87],
        [41, 84],
        [19, 21],
        [18, 56],
        [23, 39],
        [29, 95],
        [79, 100],
        [76, 82],
        [37, 55],
        [30, 97],
        [1, 36],
        [18, 96],
        [45, 86],
        [74, 92],
        [27, 78],
        [31, 35],
        [87, 91],
        [37, 84],
        [26, 57],
        [65, 87],
        [76, 91],
        [37, 77],
        [18, 66],
        [22, 97],
        [2, 91],
        [82, 98],
        [41, 46],
        [6, 78],
        [44, 80],
        [90, 94],
        [37, 88],
        [75, 90],
        [23, 37],
        [18, 80],
        [92, 93],
        [3, 80],
        [68, 86],
        [68, 92],
        [52, 91],
        [43, 53],
        [36, 37],
        [60, 74],
        [4, 9],
        [44, 80],
        [85, 93],
        [56, 83],
        [9, 26],
        [59, 64],
        [16, 66],
        [29, 36],
        [51, 96],
        [56, 80],
        [13, 87],
        [42, 72],
        [6, 56],
        [24, 53],
        [43, 71],
        [36, 83],
        [15, 45],
        [10, 48],
    ]
    for i in range(len(actions)):
        print(f"{actions[i]}({inputs[i]})")
        if actions[i] == "RangeModule":
            r = RangeModule()
        elif actions[i] == "addRange":
            r.addRange(*inputs[i])
        elif actions[i] == "removeRange":
            r.removeRange(*inputs[i])
        elif actions[i] == "queryRange":
            print(r.queryRange(*inputs[i]))
        else:
            raise ValueError(f"Invalid action {actions[i]}")
        print(f"Segments: {r.segments}")

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
