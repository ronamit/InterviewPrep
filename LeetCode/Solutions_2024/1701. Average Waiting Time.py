
class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        n = len(customers)
        t = 0
        wait_times = [-1] * n
        for i_customer, c in enumerate(customers):
            t_arrival, work_time = c
            t = max(t, t_arrival)
            t += work_time
            wait_times[i_customer] = t - t_arrival
        return sum(wait_times) / n
