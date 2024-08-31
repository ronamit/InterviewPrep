import math


class Solution:
    def minimumTime(self, jobs: list[int], workers: list[int]) -> int:
        jobs.sort()
        workers.sort()
        days = 0
        n = len(jobs)
        for i in range(n):
            days = max(days, math.ceil(jobs[i] / workers[i]))
        return days
        
