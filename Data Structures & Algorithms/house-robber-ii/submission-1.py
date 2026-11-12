class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        def dfs(idx: int, endIdx: int, cache: dict[int, int]) -> int:
            if idx in cache:
                return cache[idx]
            if idx > endIdx:
                return 0

            skip = dfs(idx + 1, endIdx, cache)
            take = nums[idx] + dfs(idx + 2, endIdx, cache)
            cache[idx] = max(skip, take)
            return cache[idx]

        return max(dfs(0, len(nums) - 2, {}), dfs(1, len(nums) - 1, {}))
