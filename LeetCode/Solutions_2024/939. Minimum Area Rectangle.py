class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points = [tuple(p) for p in points]
        points = sorted(points)
        points_set = set(points)
        min_area = None
        for i1, p1 in enumerate(points):
            for p2 in points[(i1+1):]:
                x1, y1 = p1
                x2, y2 = p2
                if not (x2 > x1 and y2 > y1):
                    continue
                if (x1, y2) in points_set and (x2, y1) in points_set:
                    area = (y2 - y1) * (x2 - x1)
                    if min_area is None:
                        min_area = area
                    else:
                        min_area = min(area, min_area)
        if min_area is None:
            return 0
        return min_area
                