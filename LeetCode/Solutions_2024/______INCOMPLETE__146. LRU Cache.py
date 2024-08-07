class Item:
    def __init__(self, key: int, value: int, n_uses: int, next_up_key: int):
        self.key
        self.value = value
        self.n_uses = n_uses
        self.next_up_key = next_up_key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = {}
        self.lest_used_key = None

        

    def get(self, key: int) -> int:
        if key not in self.items:
            return -1
        self.items[key].n_uses += 1
        if  self.least_used_key == key:
            # checj if the number of uses surpassed the "next up"
        return = self.items[key].value
        

    def put(self, key: int, value: int) -> None: 
        self.items[key] = value
        self.q.appendleft(key)
        if len(self.q) > self.capacity:
            key_to_remove = self.q.pop()
            del self.items[key_to_remove]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)