import math


import math
from functools import cache



class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        n = len(bloomDay)

        min_days_prev = [0] * n # how many flowers for 0 bouquets using flowers up to index i-1 (including)
        for mm in range(1, m + 1):
            
            # min_days_curr[i] = min days for mm bouquets using flowers up to index i-1 (including)
            min_days_curr = [math.inf] * n
            # note: we can't create a bouquets with less than k * mm flowers

            for i in range(mm * k, n):
                # The min days is a min between two options:
                # we use flower at the i-th index or not
                # If we use - we need to wait the number of days
                # needed for all the k next flowers to bloom ((i-k)..(i-1))
                min_if_use = max([bloomDay[j] for j in range(i - k, i)])
                # (note - max-heap can be used to reduce this step from O(k) to O(log(k)))
                # we need to also check how many days needed for the reset of the bouquets needed
                min_if_use = max(min_if_use, min_days_prev[n - k])
                # If not using the n-1 flower
                min_if_not_use = min_days_curr[i - 1]
                min_days_curr[i] = min(min_if_use, min_if_not_use)
            
            min_days_prev = min_days_curr
        
        ans = min_days_curr[-1]
        if ans == math.inf:
            return -1
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.minDays([1,10,2,9,3,8,4,7,5,6], 4, 2))
    


# class Solution:
#     def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
#         n = len(bloomDay)

#         @cache
#         def get_min_days(mm: int, nn: int):
#             # return min number of to have m_ bouquets from the flowers 0..n_-1
#             if mm == 0:
#                 return 0
#             if nn < k * mm:
#                 # we can't create m_ bosquets of k flowers.
#                 return math.inf
#             if nn == k * mm:
#                 # we must use all flowers.
#                 return max(bloomDay[:nn])

#             # The min days is a min between two options:
#             # we use flower at the (n_ - 1) index or not
#             # If we use - we need to wait the number of days
#             # needed for all the k next flowers to bloom
#             min_if_use = max([bloomDay[j] for j in range(nn - k, nn)])
#             # (note - max-heap can be used to reduce this step from O(k) to O(log(k)))
#             # we need to also check how many days needed for the reset of the. bosqueuts neeed
#             min_if_use = max(min_if_use, get_min_days(mm - 1, nn - k))
#             # If not using the n_ flower
#             min_if_not_use = get_min_days(mm, nn - 1)
#             return min([min_if_use, min_if_not_use])

#         ans = get_min_days(mm=m, nn=n)
#         if ans == math.inf:
#             return -1
#         return ans