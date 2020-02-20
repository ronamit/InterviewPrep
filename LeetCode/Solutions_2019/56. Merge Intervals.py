# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e




def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
    # for each two intervals - having an intersection is an eqiavlance relation
    # we need to find equivalance classes - i.e, find connected componenets in the equivalance graph
    # so run DFS on each interval to mark all the intervals connected, and then move to the next un-visited interval
    # after all comp are found - build an interval from each

    notVisited = set([(a.start, a.end) for a in intervals])
    outInt = []
    while notVisited:
        v = notVisited.pop()
        stk = [v]
        outInt.append([v[0], v[1]])
        while stk:
            w = stk.pop()
            if w in notVisited:
                notVisited.remove(w)
            # update the start of the merge interval to be the minimum:
            if w[0] < outInt[-1][0]:
                outInt[-1][0] = w[0]
            # update the end of the merge interval to be the maximum:
            if w[1] > outInt[-1][1]:
                outInt[-1][1] = w[1]
            for u in notVisited:
                # check intersection:
                if not ((w[1] < u[0]) or (u[1] < w[0])):
                    stk.append(u)
    return [Interval(a[0],a[1]) for a in outInt]


self = None
# input =  [[1,4],[2,6],[8,10],[15,18]]
input = [[1,4],[0,1], [2,3], [4,5], [3,4]]
intervals = [Interval(a[0],a[1]) for a in input]
out = merge(self, intervals)
print([(a.start, a.end) for a in out])




# # sort the interval by start value:
# intervals.sort(key=lambda intvl: intvl.start)
# # we start from end to start - since it is more efficent to remove from end of list
# outList = []
# keepGo = True
# while keepGo:
#     keepGo = False
#     while (len(intervals) > 1):
#         print([(a.start, a.end) for a in intervals])
#         if intervals[-2].end >= intervals[-1].start:
#             # Merge:
#             intervals[-2].end = max(intervals[-1].end, intervals[-2].end)
#             intervals[-2].start = min(intervals[-1].start, intervals[-2].start)
#             intervals.pop()
#             keepGo = True
#         else:
#             # otherwise - just add to out list
#             outList.append(intervals.pop())
#
# outList += intervals  # add the remaining single interval
# outList.reverse()
# return outList
#
