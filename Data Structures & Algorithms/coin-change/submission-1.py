class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp: list[list[int]] = [[None] * (amount + 1) for _ in range(len(coins) + 1)]
        
        def dfs(i: int, target: int) -> int:
            if target == 0:
                return 0
            if i == len(coins) or target < 0:
                return float('inf')
            if dp[i][target] != None:
                return dp[i][target]
            
            skip = dfs(i + 1, target)
            take = 1 + dfs(i, target - coins[i])

            result = min(skip, take)
            dp[i][target] = result
            return result


        result = dfs(0, amount)
        return result if result != float('inf') else -1