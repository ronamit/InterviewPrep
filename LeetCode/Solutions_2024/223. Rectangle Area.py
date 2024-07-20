class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # Find the overlap
        ax = ax2 - ax1
        bx = bx2 - bx1
        cx = min(max(0, ax2 - bx1), max(0, bx2 - ax1), ax, bx)
        ay = ay2 - ay1
        by = by2 - by1
        cy = min(max(0, ay2 - by1), max(0, by2 - ay1), ay, by)
        return ax * ay + bx * by - cx * cy
