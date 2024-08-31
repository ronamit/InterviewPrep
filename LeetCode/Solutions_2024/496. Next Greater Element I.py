class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # find the next greater element for each number in nums2, using a monotonic stack
        num_in_2_to_nge = {nums2[-1]: -1}
        stk = [nums2[-1]]
        n2 = len(nums2)
        for i in range(n2 - 2, -1, -1):
            x = nums2[i]
            # remove all next items that are smaller (they will not be neede for nge serches left of i since nums[i] will be higher than any of them)
            while stk and x > stk[-1]:
                stk.pop()
            # if we found next greater
            if stk and stk[-1] > x:
                num_in_2_to_nge[x] = stk[-1]
            else:
                num_in_2_to_nge[x] = -1
            stk.append(x)

        ans = [num_in_2_to_nge[x] for x in nums1]
        return ans


#############
# Brute force:
#################
# class Solution:
# def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#     ans = []
#     ind_in_2 = {x: i for i, x in enumerate(nums2)}

#     for x1 in nums1:
#         ans.append(-1)
#         j = ind_in_2[x1]
#         for j_next in range(j+1, len(nums2)):
#             if nums2[j_next] > x1:
#                 ans[-1] =  nums2[j_next]
#                 break
#     return ans
