from typing import List

class E746:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = 0, 0
        for i in range(len(cost)):
            if i == 0:
                a = cost[i]
            elif i == 1:
                b = cost[i]
            else:
                c = min(a, b) + cost[i]
                a = b
                b = c
        return min(a, b)
    
a = E746()
print(a.minCostClimbingStairs([10, 15, 20]))
print(a.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))