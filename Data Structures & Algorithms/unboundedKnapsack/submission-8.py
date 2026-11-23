class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        dp: list[int] = [0] * (capacity + 1)

        for p, w in zip(profit, weight):
            for c in range(w, capacity + 1):
                dp[c] = max(dp[c], p + dp[c - w])
        
        return dp[capacity]
