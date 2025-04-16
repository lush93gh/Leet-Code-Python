from typing import List

class M322:
    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [float('inf') for _ in range(amount + 1)]
        table[amount] = 0
        for i in range(amount, -1, -1):
            if table[i] != float("inf"):
                for coin in coins:
                    remains = i - coin 
                    if remains >= 0:
                        table[remains] = min(table[i] + 1, table[remains])
        return table[0] if table[0] != float("inf") else -1


    def coinChangeDFS(self, coins: List[int], amount: int) -> int:
        self.dp = {}
        coins.sort()
        coins.reverse()
        if amount == 0: 
            return 0
        self.min_number = float('inf')
        for coin in coins:
            number = self.dfs(1, coins, amount - coin)
            if number > 0:
                self.min_number = min(self.min_number, number)
        return self.min_number if self.min_number != float("inf") else -1
    
    def dfs(self, depth: int, coins: List[int], amount: int) -> int:
        if (amount, depth) in self.dp.keys():
            return self.dp[(amount, depth)]
        elif amount == 0:
            return depth
        elif amount < 0:
            return 0
        else:
            min_number = float("inf")
            for coin in coins:
                if depth + 1 >= self.min_number:
                    number = self.min_number
                else:
                    number = self.dfs(depth + 1, coins, amount - coin)
                if number > 0:
                    min_number = min(min_number, number)
            self.dp[(amount, depth)] = min_number if min_number != float("inf") else -1
            return self.dp[(amount, depth)] 
        
a = M322()
print(a.coinChange(coins=[1, 2, 5], amount=11)) # 3
print(a.coinChange(coins=[2], amount=3)) # -1
print(a.coinChange(coins=[1], amount=0)) # 0
print(a.coinChange(coins=[1, 2, 5], amount=100)) # 20 
print(a.coinChange(coins=[3, 7, 405, 436], amount=8839)) # 25
        