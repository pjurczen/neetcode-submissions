class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

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
