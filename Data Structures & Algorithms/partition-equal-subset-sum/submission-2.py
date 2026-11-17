class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total: int = sum(nums)
        if total % 2 != 0:
            return False
        
        half: int = total // 2
        N, M = len(nums), half + 1
        dp: list[list[bool]] = [[False] * M for _ in range(N + 1)]

        for i in range(N + 1):
            dp[i][half] = True

        for i in range(N - 1, -1, -1):
            for c in range(M - 1):
                skip = dp[i + 1][c]
                newCur = c + nums[i]
                take = newCur <= half and dp[i + 1][newCur]
                dp[i][c] = skip or take
        
        return dp[0][0]