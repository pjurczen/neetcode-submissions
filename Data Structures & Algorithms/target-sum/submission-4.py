class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        total = sum(nums)
        if abs(target) > total:
            return 0
        N, M = len(nums), total * 2 + 1
        dp: list[list[int]] = [[0] * M for _ in range(N + 1)]

        for c in range(M):
            if c - total == target:
                dp[N][c] = 1

        for i in range(N - 1, -1, -1):
            for c in range(M):
                plus = dp[i + 1][c + nums[i]] if c + nums[i] < M else 0
                minus = dp[i + 1][c - nums[i]] if c - nums[i] >= 0 else 0
                dp[i][c] = plus + minus
        
        return dp[0][total]