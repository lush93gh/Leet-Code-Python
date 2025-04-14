from typing import List
import heapq

class H239:
    def __init__(self):
        self.removed_handle = {}
    
    def queue_remove(self, value: int):
        count = self.removed_handle.get(value, 0) + 1
        self.removed_handle[value] = count

    def queue_get(self, q):
        front = q[0] 
        while self.removed_handle.get(front, 0) > 0:
            heapq.heappop(q)
            count = self.removed_handle.get(front, 0) - 1
            self.removed_handle[front] = count
            front = q[0] if len(q) > 0 else 0

        return front

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dimension = len(nums) - k + 1
        max_pooling = [0 for _ in range(dimension)]
        window = [-1 * nums[i] for i in range(k)]
        heapq.heapify(window)

        for i in range(dimension):
            max_pooling[i] = -1 * self.queue_get(window)
            self.queue_remove(-1 * nums[i])
            if i + k < len(nums):
                heapq.heappush(window, -1 * nums[i + k])

        return max_pooling
    
a = H239()
print(a.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))  # [3,3,5,5,6,7]
a = H239()
print(a.maxSlidingWindow(nums=[1], k=1)) # [1]
a = H239()
print(a.maxSlidingWindow(nums=[1, 3, 1, 2, 0, 5], k=3))  # [3,3,2,5]
