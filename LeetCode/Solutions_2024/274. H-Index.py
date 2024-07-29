class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i, c in enumerate(citations):
            # the number of papers with at least c citations is (i+1)
            if c >= (i + 1):
                h = i + 1
        return h
    
sol = Solution()
print(sol.hIndex([3,0,6,1,5]))
