"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # merge all the time intervaks using:
        # put alll times in an in a ordered list for each person, with indicator of "start" or "end" for each time.
        # merge the lists: https://www.geeksforgeeks.org/merge-k-sorted-linked-lists-set-2-using-min-heap/ 
        # go over the times in ordered manner
        # use some counter to see how many emplotyes are free after each time, and until what time
        #

        