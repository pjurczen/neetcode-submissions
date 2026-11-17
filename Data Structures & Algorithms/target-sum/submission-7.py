class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        total = sum(nums)
        if abs(target) > total or (total + target) % 2:
            return 0
        
        P = (total + target) // 2
 
        dp: list[int] = [0] * (P + 1)
        dp[0] = 1

        for n in nums:
            for s in range(P, n - 1, -1):
                dp[s] += dp[s - n]
        
        return dp[P]
