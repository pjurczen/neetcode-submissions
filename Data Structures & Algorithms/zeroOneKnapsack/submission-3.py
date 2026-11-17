class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity + 1
        dp: list[list[int]] = [[0] * M for _ in range(N)]
        
        for c in range(M):
            if weight[0] <= c:
                dp[0][c] = profit[0]
        
        for i in range(1, N):
            for c in range(1, M):
                skip = dp[i - 1][c]
                take = 0
                newCap = c - weight[i]
                if newCap >= 0:
                    take = profit[i] + dp[i - 1][newCap]
                dp[i][c] = max(skip, take)

        return dp[N - 1][M - 1]
