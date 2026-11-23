class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp: list[int] = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(len(coins)):
            for a in range(coins[i], amount + 1):
                skip = dp[a]
                take = 1 + dp[a - coins[i]]
                dp[a] = min(skip, take)
        
        result = dp[amount]
        return result if result != float('inf') else -1
