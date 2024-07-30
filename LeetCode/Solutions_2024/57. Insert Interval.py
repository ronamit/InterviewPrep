import math


class Solution:
    def insert(
        self,
        intervals: list[list[int]],
        newInterval: list[int],
    ) -> list[list[int]]:
        new_start, new_end = newInterval
        new_list = []
        prev_end = -math.inf
        i = 0
        n = len(intervals)
        already_inserted = False
        while i < n:
            cur_start, cur_end = intervals[i]
            if already_inserted or cur_end < new_start:
                # interval unchanged
                new_list.append(intervals[i])
            elif prev_end < new_start and not already_inserted:
                if new_end < cur_start:
                    # insert without merge:
                    new_list.append([new_start, new_end])
                    new_list.append(intervals[i])
                    already_inserted = True
                else:
                    # we need to insert the new interval here
                    # and possibly merge some existing interval
                    keep_merging = new_end >= cur_start
                    while keep_merging:
                        new_start = min(new_start, cur_start)
                        new_end = max(new_end, cur_end)
                        if i < (n - 1) and new_end >= intervals[i + 1][0]:
                            i += 1
                            cur_start, cur_end = intervals[i]
                        else:
                            keep_merging = False
                    new_list.append([new_start, new_end])
                    already_inserted = True
                # end if
            # end if
            prev_end = cur_end
            i += 1
        if not already_inserted:
            new_list.append([new_start, new_end])
        return new_list
