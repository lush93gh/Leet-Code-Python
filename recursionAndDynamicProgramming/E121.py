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
    
    def maxProfitRecursive(self, price_delta: List[int]) -> int:
        if len(price_delta) == 0:
            return 0
        if len(price_delta) == 1:
            return max(price_delta[0], 0)
        mid = len(price_delta) // 2

        left_recursive = self.maxProfitRecursive(price_delta[: mid])
        right_recursive = self.maxProfitRecursive(price_delta[mid:])
        left_max = 0
        left_sum = 0
        for i in range(mid - 1, -1, -1):
            left_sum += price_delta[i]
            if left_sum > left_max:
                left_max = left_sum
        
        right_max = 0
        right_sum = 0
        for i in range(mid, len(price_delta)):
            right_sum += price_delta[i]
            if right_sum > right_max:
                right_max = right_sum

        cross_max = left_max + right_max
        return max(max(left_recursive, right_recursive), cross_max)

    
    def maxProfitDivideAndConquer(self, prices: List[int]) -> int:
        price_delta = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        return self.maxProfitRecursive(price_delta)
    
    def maxProfit(self, prices: List[int]) -> int:
        price_delta = [prices[i] - prices[i - 1]for i in range(1, len(prices))]
        max_profit = 0
        local_max = 0
        for price in price_delta:
            local_max += price
            if local_max < 0:
                local_max = 0
            if local_max > max_profit:
                max_profit = local_max
        
        return max_profit

    
a = E121()
print(a.maxProfit([7, 1, 5, 3, 6, 4])) # 5
print(a.maxProfit([7,6,4,3,1])) # 0
print(a.maxProfit([2,1,2,1,0,1,2])) # 2
print(a.maxProfit([9,9,0,3,0,7,7,7,4,1,5,0,1,7])) # 7
print(a.maxProfit([2, 1])) # 0