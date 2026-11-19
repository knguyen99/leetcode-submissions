class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [ float("inf") for _ in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            for i in range(coin, len(dp)):
                dp[i] = min(dp[i - coin] + 1, dp[i])
        return -1 if dp[-1] == float("inf") else dp[-1]
                
                