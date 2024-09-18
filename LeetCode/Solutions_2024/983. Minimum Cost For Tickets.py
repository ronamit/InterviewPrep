from functools import cache


class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        @cache
        def get_min_cost(i_start: int):
            nonlocal days, costs
            if i_start == len(days):
                return 0
            # check the costs for each of the 3 options:
            # 1-day ticket:
            cur_day = days[i_start]
            cost_1day = costs[0] + get_min_cost(i_start + 1)
            # 7-day ticket:
            i_next = i_start + 1
            while i_next < len(days) and days[i_next] < cur_day + 7:
                i_next += 1
            cost_7day = costs[1] + get_min_cost(i_next)
            # 30-day ticket:
            i_next = i_start + 1
            while i_next < len(days) and days[i_next] < cur_day + 30:
                i_next += 1
            cost_30day = costs[2] + get_min_cost(i_next)
            return min(cost_1day, cost_7day, cost_30day)

        return get_min_cost(0)
