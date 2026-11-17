class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        total = sum(nums)
        if abs(target) > total:
            return 0
        N, M = len(nums), total * 2 + 1
        dp: list[int] = [0] * M

        dp[total + target] = 1

        for i in range(N - 1, -1, -1):
            tmp = [0] * M
            for c in range(M):
                plus = dp[c + nums[i]] if c + nums[i] < M else 0
                minus = dp[c - nums[i]] if c - nums[i] >= 0 else 0
                tmp[c] = plus + minus
            dp = tmp
        
        return dp[total]