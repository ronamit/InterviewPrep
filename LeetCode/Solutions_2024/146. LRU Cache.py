from dataclasses import dataclass

# ------------------------------------------------------------------------------------------------------------------------------------


@dataclass
class Node:
    key: int = None
    value: int = None
    next: int = None
    prev: int = None


# ------------------------------------------------------------------------------------------------------------------------------------


class DoublyLinkedList:
    def __init__(self):
        # dummy nodes:
        self.head_dummy = Node()
        self.tail_dummy = Node()
        self.head_dummy.prev = self.tail_dummy
        self.tail_dummy.next = self.head_dummy
        self.nodes: dict[int, Node] = {}  # map key: Node

    def is_key_exists(self, key: int):
        return key in self.nodes

    def add_to_front(self, key: int, value: int):
        # remove if exist and add new item to the head of list
        self.remove_by_key(key)
        node = Node(key=key, value=value, next=self.head_dummy, prev=self.head_dummy.prev)
        self.head_dummy.prev.next = node
        self.head_dummy.prev = node
        self.nodes[key] = node

    def remove_by_key(self, key: int):
        if key not in self.nodes:
            return
        node = self.nodes[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.nodes[key]

    def remove_tail(self):
        old_tail_node = self.tail_dummy.next
        self.remove_by_key(old_tail_node.key)

    def get_value(self, key):
        if key not in self.nodes:
            return None, False
        return self.nodes[key].value, True

    def __len__(self):
        return len(self.nodes)

    def __repr__(self) -> str:
        return str([(k, node.value) for k, node in self.nodes.items()])


# ------------------------------------------------------------------------------------------------------------------------------------


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = DoublyLinkedList()

    def put(self, key: int, value: int) -> None:
        # if key exists - update the value and move to head of queue
        if self.items.is_key_exists(key):
            # remove if exist and add new item to the head of list
            self.items.add_to_front(key=key, value=value)
        else:
            # if full - remove least recently used (the tail of the queue)
            if len(self.items) >= self.capacity:
                self.items.remove_tail()
            # create new node and add it as new head
            self.items.add_to_front(key=key, value=value)

    def get(self, key: int) -> int:
        value, exists = self.items.get_value(key)
        if not exists:
            return -1
        # the key was used - move it to front
        self.items.add_to_front(key=key, value=value)
        return value


# ------------------------------------------------------------------------------------------------------------------------------------

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    actions = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    all_outs = []
    for i in range(len(actions)):
        print("-" * 10 + f" i={i} " + "-" * 10)
        print(f"{actions[i]}({args[i]})")
        all_outs.append(None)
        if actions[i] == "LRUCache":
            cache = LRUCache(*args[i])
        elif actions[i] == "put":
            cache.put(*args[i])
        elif actions[i] == "get":
            out = cache.get(*args[i])
            print("Output", out)
            all_outs[-1] = out
        print(f"cache items: {cache.items}")
    print("-" * 10 + " Done " + "-" * 10)
    print("all_outs:", all_outs)
# ------------------------------------------------------------------------------------------------------------------------------------
