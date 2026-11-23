from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def dfs(i: int, target: int) -> int:
            if target == 0:
                return 0
            if i == len(coins) or target < 0:
                return float('inf')
            
            skip = dfs(i + 1, target)
            take = 1 + dfs(i, target - coins[i])

            return min(skip, take)

        result = dfs(0, amount)
        return result if result != float('inf') else -1