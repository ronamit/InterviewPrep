import functools
import operator


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        # flatten to a time list with (t, is_start) elements
        intervals = [[(a[0], True), (a[1], False)] for a in intervals]
        all_times = functools.reduce(operator.iadd, intervals, [])

        # sort by time - and put "start" after "end" if same time
        all_times.sort(key=lambda a: (a[0], a[1]))
        # print(all_times)
        max_rooms = 0
        cur_rooms = 0
        for t, is_start in all_times:
            if is_start:
                cur_rooms += 1
            else:
                cur_rooms -= 1
            max_rooms = max(max_rooms, cur_rooms)
        return max_rooms
