class Solution:

    def rob(self, nums: List[int]) -> int:
        cache: dict[int, int] = {}
       
        def dfs(nums: list[int], idx: int) -> int:
            if idx in cache:
                return cache[idx]
            if idx >= len(nums):
                return 0

            first = dfs(nums, idx+1)
            second = nums[idx] + dfs(nums, idx+2)
            count = max(first, second)

            cache[idx] = count
            return count
        
        return dfs(nums, 0)

