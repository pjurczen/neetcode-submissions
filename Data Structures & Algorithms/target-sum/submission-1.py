class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = defaultdict(int)

        dp[0] = 1

        for n in nums:
            next_dp = defaultdict(int)
            for sum, count in dp.items():
                next_dp[sum + n] += count
                next_dp[sum - n] += count
            dp = next_dp
        
        return dp[target]

        cache: dict[tuple[int, int], int] = {}
        
        def dfs(i: int, sum: int) -> int:
            if (i, sum) in cache:
                return cache[(i, sum)]
            if i == len(nums):
                if sum == target:
                    return 1
                else:
                    return 0
            result = 0
            result += dfs(i+1, sum - nums[i])
            result += dfs(i+1, sum + nums[i])
            cache[(i, sum)] = result

            return result
        
        return dfs(0, 0)
