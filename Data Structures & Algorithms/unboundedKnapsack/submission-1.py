class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        
        N, M = len(profit) - 1, capacity + 1
        dp: list[list[int]] = [[None] * M for _ in range(N + 1)]

        def dfs(i: int, capacity: int) -> int:
            if i == len(profit):
                return 0
            if dp[i][capacity] is not None:
                return dp[i][capacity]
            
            skip = dfs(i + 1, capacity)
            take = 0
            newCap = capacity - weight[i]
            if newCap >= 0:
                take = profit[i] + dfs(i, newCap)
            
            dp[i][capacity] = max(skip, take)
            return dp[i][capacity]
        
        return dfs(0, capacity)