class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        
        N, M = len(profit), capacity + 1
        dp: list[int] = [0] * M

        for c in range(weight[0], M):
            dp[c] = profit[0] + dp[c - weight[0]]

        for i in range(1, N):
            for c in range(weight[i], M):
                dp[c] = max(dp[c], profit[i] + dp[c - weight[i]])
        
        return dp[M - 1]
