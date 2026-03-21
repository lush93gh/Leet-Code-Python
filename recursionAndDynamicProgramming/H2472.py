class Solution:
    def check(self, s: str) -> bool:
        for i in range((len(s) - 1) // 2 + 1):
            if s[i] != s[len(s) - 1 -i]:
                return False
        return True

    def maxPalindromes(self, s: str, k: int) -> int:
        dp = [0] * len(s) + 1
        for i in range(len(s) + 1):
            if i < k:
                dp[i] = 0
            else:
                if self.check(s[i-k+1:i+1]):
                    dp[i] = dp[i-k] + 1
                elif i-k >=0 and self.check(s[i-k:i+1]):
                    dp[i] = dp[i-k-1] + 1
                else:
                    dp[i] = dp[i - 1]
