class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total: int = sum(nums)
        if total % 2 != 0:
            return False
        
        half: int = total // 2
        N, M = len(nums), half + 1
        dp: list[bool] = [False] * M

        dp[half] = True

        for i in range(N - 1, -1, -1):
            tmp = [False] * M
            for c in range(M - 1):
                skip = dp[c]
                newCur = c + nums[i]
                take = newCur <= half and dp[newCur]
                tmp[c] = skip or take
            dp = tmp
        
        return dp[0]