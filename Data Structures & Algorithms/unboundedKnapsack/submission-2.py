from functools import cache

class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        @cache
        def dfs(i: int, capacity: int) -> int:
            if i == len(profit):
                return 0
            
            skip = dfs(i + 1, capacity)
            take = 0
            newCap = capacity - weight[i]
            if newCap >= 0:
                take = profit[i] + dfs(i, newCap)

            return max(skip, take)
        
        return dfs(0, capacity)