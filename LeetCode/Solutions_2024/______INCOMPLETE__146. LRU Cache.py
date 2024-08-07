class Item:
    def __init__(self, key: int, value: int, n_uses: int, next_up_key: int):
        self.key = key
        self.value = value
        self.n_uses = n_uses
        self.next_up_key = next_up_key

    def __repr__(self) -> str:
        return f"Item(key={self.key}, value={self.value}, n_uses={self.n_uses}, next_up_key={self.next_up_key})"


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items: dict[int, Item] = {}
        self.least_used_key = None

    def get(self, key: int) -> int:
        if key not in self.items:
            return -1
        self.increase_usage_count(key)
        return self.items[key].value

    def increase_usage_count(self, key: int):
        cur_item = self.items[key]
        cur_item.n_uses += 1
        if self.least_used_key == key:
            # check if the number of uses surpassed the "next up"
            next_up_key = cur_item.next_up_key
            if next_up_key is not None and cur_item.n_uses >= self.items[next_up_key].n_uses:
                # replace the least_used_key with next_up_key:
                self.least_used_key = next_up_key
                # the new least used will point to the currently retrieved key as "next up"
                self.items[self.least_used_key].next_up_key = key

    def put(self, key: int, value: int) -> None:
        if key in self.items:
            # if the value 
            self.items[key].value = value
            self.increase_usage_count(key)
        else:
            # add new key to the LRU
            #  if no space for it - remove least used
            if len(self.items) >= self.capacity:
                key_to_remove = self.least_used_key
                print("Evicts ", key_to_remove)
                self.least_used_key = self.items[key_to_remove].next_up_key
                del self.items[key_to_remove]
            self.items[key] = Item(key=key, value=value, n_uses=-1, next_up_key=self.least_used_key)
            self.least_used_key = key
            self.increase_usage_count(key) # we first set -1 usages and then update the count so the more recent item will have priority in case of same num usage


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    actions = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    for i in range(len(actions)):
        print("-" * 10 + f"i={i}" + "-" * 10)
        print(f"{actions[i]}({args[i]})")
        if actions[i] == "LRUCache":
            cache = LRUCache(*args[i])
        elif actions[i] == "put":
            cache.put(*args[i])
        elif actions[i] == "get":
            print(cache.get(*args[i]))
        print(f"cache items: {cache.items}, least used key: {cache.least_used_key}")
