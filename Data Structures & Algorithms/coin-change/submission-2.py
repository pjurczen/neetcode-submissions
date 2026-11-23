class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp: list[list[int]] = [[0] * (amount + 1) for _ in range(len(coins))]

        for i in range(len(coins)):
            for a in range(1, amount + 1):
                skip = dp[i - 1][a] if i - 1 >= 0 else float('inf')
                take = float('inf')
                if a - coins[i] >= 0:
                    take = 1 + dp[i][a - coins[i]]
                dp[i][a] = min(skip, take)
        
        result = dp[len(coins) - 1][amount]
        return result if result != float('inf') else -1
