class Solution:
    def countBits(self, num: int) -> List[int]:
        oneCnt = [0]
        for i in range(1, num + 1):
            cntr = oneCnt[i // 2] + (i % 2)
            oneCnt.append(cntr)
        return oneCnt

