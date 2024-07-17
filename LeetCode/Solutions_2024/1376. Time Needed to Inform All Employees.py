from collections import deque

from typing import List

class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        # cread the list of subordinates of each employee
        sub = [[] for _ in range(n)]
        for i_sub, i_manager in enumerate(manager):
            if i_manager != -1:
                sub[i_manager].append(i_sub)

        # Run BFS to find the total time

        time_informed = [None for _ in range(n)]
        q = deque([headID])
        time_informed[headID] = 0
        while q:
            i_employee = q.pop()
            for i_sub in sub[i_employee]:
                # since it is a tree - no need to check if visited
                q.appendleft(i_sub)
                time_informed[i_sub] = (
                    time_informed[i_employee] + informTime[i_employee]
                )

        return max(time_informed)
