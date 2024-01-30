from typing import List
import heapq

class E703:
    k = 0
    heap = []
    lastResult = -float('inf')

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        if(val < self.lastResult):
            return self.lastResult
        heapq.heappush(self.heap, val)
        
        for i in range(len(self.heap) - self.k):
            heapq.heappop(self.heap)

        return self.heap[0]
    

a = E703(3, [4, 5, 8, 2])
print(a.add(3))
print(a.add(5))
print(a.add(10))
print(a.add(9))
print(a.add(4))