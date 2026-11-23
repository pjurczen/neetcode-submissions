class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp: list[int] = [float('inf')] * (amount + 1)

        for i in range(len(coins)):
            tmp: list[int] = [0] * (amount + 1)
            for a in range(1, amount + 1):
                skip = dp[a]
                take = float('inf')
                if a - coins[i] >= 0:
                    take = 1 + tmp[a - coins[i]]
                tmp[a] = min(skip, take)
            dp = tmp
        
        result = dp[amount]
        return result if result != float('inf') else -1
