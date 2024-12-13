from functools import lru_cache


class Solution:

    def minCost(self, costs: list[list[int]]) -> int:
        @lru_cache()
        def min_cost_aux(i_house: int, prev_color: int | None) -> int:
            if i_house == len(costs):
                return 0
            min_so_far = float("inf")
            costs_sorted = sorted((costs[i_house][i_color], i_color) for i_color in range(3))
            for color_cost, i_color in costs_sorted:
                if i_color == prev_color or color_cost > min_so_far:
                    continue
                cur_color_cost = color_cost + min_cost_aux(i_house + 1, i_color)
                min_so_far = min(min_so_far, cur_color_cost)
            return min_so_far
                
        return min_cost_aux(i_house=0, prev_color=None)