from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = deque()
        self.cur_sum = 0
        self.cur_n = 0
        

    def next(self, val: int) -> float:
        self.q.append(val)
        self.cur_sum += val
        self.cur_n += 1
        if  self.cur_n > self.size:
            old_val = self.q.popleft()
            self.cur_n -= 1
            self.cur_sum -= old_val
        return self.cur_sum /  self.cur_n 
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)