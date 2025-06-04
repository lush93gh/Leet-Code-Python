from typing import List
import heapq

class E121:  
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_max_profit = 0
        for i in range(1, len(prices)):
            current_max_profit = max(0, current_max_profit + prices[i] - prices[i - 1])
            max_profit = max(max_profit, current_max_profit)
        return max_profit

    def maxProfitQueue(self, prices: List[int]) -> int:
        max_profit = 0 
        h = []
        heapq.heapify(h)
        for price in prices:
            min = h[0] if len(h) > 0 else price
            max_profit = max(max_profit, price - min)
            heapq.heappush(h, price)
      
        return max_profit
    
a = E121()
print(a.maxProfit([7, 1, 5, 3, 6, 4])) # 5
print(a.maxProfit([7, 6, 4, 3, 1])) # 0