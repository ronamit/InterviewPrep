from typing import List

def add_to_dict(d, k):
    if k not in d:
        d[k] = 1
    else:
        d[k] += 1

def get_key_count(d, k):
    if k not in d:
        return 0
    else:
        return d[k]

class DetectSquares:

    def __init__(self):
        self.points_dict = {}
        self.points_per_x = {}
        self.points_per_y = {}
        

    def add(self, point: List[int]) -> None:
        point = tuple(point)
        add_to_dict(self.points_dict, point)
        x,y = point
        if x not in self.points_per_x:
            self.points_per_x[x] = {}
        if y not in self.points_per_y:
            self.points_per_y[y] = {}        
        add_to_dict(self.points_per_x[x], y)
        add_to_dict(self.points_per_y[y], x)

    def count(self, point: List[int]) -> int:
        ans = 0
        point = tuple(point)
        x,y = point
        if x not in self.points_per_x:
            return 0
        for y2 in self.points_per_x[x]:
            n2 = self.points_per_x[x][y2] 
            square_a = abs(y2 - y)
            if square_a == 0:
                continue
            for dx in [-square_a, square_a]:
                x3, y3 = x + dx, y2
                x4, y4 = x  + dx, y
                n3 =  get_key_count(self.points_dict, (x3,y3))
                n4 =  get_key_count(self.points_dict, (x4,y4))
                ans +=  n2 * n3 * n4
        return ans



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)