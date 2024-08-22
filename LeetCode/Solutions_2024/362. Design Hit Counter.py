class HitCounter:

    def __init__(self):
        self.hits_count = {}

    def hit(self, timestamp: int) -> None:
        self.hits_count[timestamp] = self.hits_count.get(timestamp, 0) + 1

    def getHits(self, timestamp: int) -> int:
        n_hits = 0
        for i in range(timestamp - 300 + 1, timestamp + 1):
            n_hits += self.hits_count.get(i, 0)
        return n_hits


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
