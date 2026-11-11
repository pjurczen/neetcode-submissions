class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp: dict[int, int] = {}

        def dfs(i: int) -> int:
            if i in dp:
                return dp[i]
            if i >= len(cost):
                return 0
            
            single = dfs(i + 1)
            double = dfs(i + 2)

            dp[i] = cost[i] + min(single, double)
            return dp[i]
        
        return min(dfs(0), dfs(1))