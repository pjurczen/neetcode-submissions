class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        total = sum(nums)
        N, M = len(nums), total * 2 + 1
        dp: list[list[int | None]] = [[None] * M for _ in range(N)]

        def dfs(i: int, cur: int) -> int:
            if i == len(nums):
                if cur == target:
                    return 1
                else:
                    return 0
            if dp[i][cur + total] != None:
                return dp[i][cur + total]
            
            dp[i][cur + total] = dfs(i + 1, cur - nums[i]) + dfs(i + 1, cur + nums[i])
            return dp[i][cur + total]

        res = dfs(0, 0)
        return res
            