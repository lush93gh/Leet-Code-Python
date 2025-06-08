from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.q = deque()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.q.remove(key)
        self.q.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.q.remove(key)
        elif len(self.cache) == self.capacity:
            lru = self.q.popleft()
            del self.cache[lru]
        self.cache[key] = value
        self.q.append(key)

lRUCache = LRUCache(2)
lRUCache.put(1, 1) # cache is {1=1}
lRUCache.put(2, 2) # cache is {1=1, 2=2}
lRUCache.get(1)    # return 1
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2)    # returns -1 (not found)
lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1)    # return -1 (not found)
lRUCache.get(3)    # return 3
lRUCache.get(4)    # return 4

