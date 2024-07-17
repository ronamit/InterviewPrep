

import heapq
from typing import List



# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

class Solution:
    def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:
        # put all times in an in a ordered list for each person, with indicator of "start" or "end" for each time.

        schedules_lists = []
        for person_schedule in schedule:
            schedules_lists.append([])
            for interval in person_schedule:
                schedules_lists[-1] += [(interval.start, "s"), (interval.end, "e")]

        # merge all the time intervals lists (while keeping times ordered) using:
        # merge the lists: https://www.geeksforgeeks.org/merge-k-sorted-linked-lists-set-2-using-min-heap/

        h = heapq.merge(*schedules_lists, key=lambda x: x[0])

        # print(list(h))

        # go over the times in ordered manner
        # use some counter to see how many employees are free after each time, and until what time
        n_employees = len(schedule)
        on_break_count = n_employees
        free_times = []
        cur_break = Interval(start=None, end=None)
        for time, indicator in h:
            if indicator == "s":
                # employee is starting
                on_break_count -= 1
            elif indicator == "e":
                # employee is ending
                on_break_count += 1
            if on_break_count == n_employees and cur_break.start is None:
                # first time all employees are free
                cur_break.start = time
            if on_break_count < n_employees and cur_break.start is not None:
                # break is over, add the time to the free times list
                cur_break.end = time
                if cur_break.end > cur_break.start:
                    free_times.append(cur_break)
                cur_break = Interval(start=None, end=None)
        return free_times
