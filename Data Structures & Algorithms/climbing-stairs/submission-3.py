class Solution:
    cache: dict[int, int] = {}

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [1, 2]
        for _ in range(3, n+1):
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp
        return dp[1]
