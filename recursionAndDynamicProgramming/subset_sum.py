class SubsetSum:
    def isSubsetSum (self, arr, sum):
        self.prev_dp = [-1 for _ in range(sum + 1)]
        self.current_dp = [-1 for _ in range(sum + 1)]
        self.prev_dp[0] = 1

        for i in range(len(arr)):
            num = arr[i]
            for j in range(sum + 1):
                if j == 0:
                    self.current_dp[j] = 1
                elif (j >= num and self.prev_dp[j - num] == 1) or self.prev_dp[j] == 1:
                        self.current_dp[j] = 1
            for k in range(sum + 1):
                self.prev_dp[k] = self.current_dp[k]

        return self.current_dp[sum] == 1

a= SubsetSum()
print(a.isSubsetSum(arr=[3, 34, 4, 12, 5, 2], sum = 9)) # True
print(a.isSubsetSum(arr=[3, 34, 4, 12, 5, 2], sum = 30)) # False
print(a.isSubsetSum(arr=[1, 2, 3], sum = 6)) # True
print(a.isSubsetSum(arr=[6, 1, 2, 3, 3 , 6], sum = 9)) # True
