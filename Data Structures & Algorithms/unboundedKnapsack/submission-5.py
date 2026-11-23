class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        
        N, M = len(profit), capacity + 1
        dp: list[int] = [0] * M

        for c in range(weight[0], M):
            dp[c] = profit[0] + dp[c - weight[0]]

        for i in range(1, N):
            for c in range(1, M):
                skip = dp[c]
                take = 0
                newCap = c - weight[i]
                if newCap >= 0:
                    take = profit[i] + dp[newCap]
                dp[c] = max(skip, take)
        
        return dp[M - 1]
