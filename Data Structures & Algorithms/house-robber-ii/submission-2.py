class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)

        def dp(startIdx: int, endIdx: int) -> int:
            rob1, rob2 = 0, 0
            for i in range(startIdx, endIdx):
                tmp = max(rob1 + nums[i], rob2)
                rob1 = rob2
                rob2 = tmp
            return rob2

        return max(dp(0, n-1), dp(1, n))
