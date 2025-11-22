from typing import List
import heapq

class E121:
    def heappop(self, h, removed):
        while len(h) > 0 and removed.get(h[0], 0) > 0:
            s = heapq.heappop(h)
            removed[s] = max(0, removed[s] - 1)
        return h[0] if len(h) > 0 else None
    
    def maxProfitHeapWithRemove(self, prices: List[int]) -> int:
        h = prices.copy()
        heapq.heapify(h)
        removed = {}
        max_profit = 0
        for i in range(len(prices) - 1, -1, -1):
            price = prices[i]
            removed_count = removed.get(price, 0)
            removed[price] = removed_count + 1
            s = self.heappop(h, removed)
            if s is not None and price - s > max_profit:
                max_profit = price - s
        return max_profit
    
a = E121()
print(a.maxProfit([7, 1, 5, 3, 6, 4])) # 5
print(a.maxProfit([7,6,4,3,1])) # 0
print(a.maxProfit([2,1,2,1,0,1,2])) # 2
print(a.maxProfit([9,9,0,3,0,7,7,7,4,1,5,0,1,7])) # 7