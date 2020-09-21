from typing import List, Dict, Tuple, Sequence

# https://leetcode.com/explore/featured/card/fun-with-arrays/511/in-place-operations/3261/

class Solution:

	def sortedSquares(self, A: List[int]) -> List[int]:
		n = len(a)
		first_nonnegg = -1
		for i, a in enumerate(A):
			if a >= 0:
				first_nonnegg = i
				break
			# end if
		# end for
		for i in range(n):
			A[i] = A[i]**2
		# end for
		i = first_nonnegg - 1
		j = first_nonnegg
		while i >= 0 and j < n:
			if A[j] > A[i]:
				A[i], A[j] = A[j], A[i]

		return A





