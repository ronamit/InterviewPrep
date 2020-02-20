class Solution:
    def canWinNim(self, n: int) -> bool:
        return (n <= 3) or (n % 4 != 0)
#
# class Solution:
#     def canWinNim(self, n: int) -> bool:
#
#         V = [False for _ in range(n)]
#         for i in range(min(n, 3)):
#             V[i] = True
#         for i in range(3, n):
#             stones0 = i + 1
#             iCanWin = False
#             for myTake in range(1, 4):
#                 stone1 = stones0 - myTake
#                 if stone1 <= 0:
#                     iCanWin = True
#                     break
#                 rivalCanWin = V[stone1-1]
#                 if not rivalCanWin:
#                     iCanWin = True
#                     break
#             V[i] = iCanWin
#         return V[-1]
#

sol = Solution()
n = 5
print(sol.canWinNim(n))