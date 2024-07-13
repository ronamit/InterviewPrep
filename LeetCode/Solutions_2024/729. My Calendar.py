class MyCalendar:

    def __init__(self):
        self.booked = []
        

    def book(self, start: int, end: int) -> bool:
        for p_start, p_end in self.booked:
            if  not (p_end <= start or end <= p_start):
                return False
        self.booked.append((start, end))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)