
def maxProduct(self, nums):
    n = len(nums)
    maxProd = nums[0]
    prodFromLastNeg = 1
    prodFromPrevNeg =
    for a in nums:

    return maxProd

self = None
nums = [2,-5,-2,-4,3]
print(maxProduct(self, nums))



#
# def maxProduct(self, nums):
#     n = len(nums)
#     stk = []
#     maxProd = nums[0]
#     for a in nums:
#         if a == 0:
#             stk = []
#         elif not stk:
#             stk.append(a)
#         elif stk[-1] > 0 and a > 0:
#             stk[-1] *= a
#         elif stk[-1] < 0 and a < 0:
#             stk[-1] *= a
#             while len(stk) > 1 and stk[-2] > 0:
#                 stk[-2] *= stk[-1]
#                 stk.pop()
#         elif stk[-1] > 0 and a < 0:
#             stk.append(a)
#             if len(stk) > 2:
#                 p = 1
#                 while stk:
#                     p *= stk.pop()
#                 stk.append(p)
#         elif stk[-1] < 0 and a > 0:
#             stk.append(a)
#         print(stk)
#         if stk:
#             maxProd = max(maxProd, stk[-1])
#         else:
#             maxProd = max(maxProd, 0)
#     return maxProd
