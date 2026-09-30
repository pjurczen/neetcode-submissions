class Solution:

    def rob(self, nums: List[int]) -> int:
        cache: dict[int, int] = {}
       
        def dfs(nums: list[int], idx: int) -> int:
            if idx in cache:
                return cache[idx]
            if idx >= len(nums):
                return 0
            if idx == len(nums) - 1:
                return nums[idx]
            if idx == len(nums) - 2:
                return max(nums[idx], nums[idx + 1])

            count = nums[idx]
            first = dfs(nums, idx+2)
            second = dfs(nums, idx+3)
            count += max(first, second)

            cache[idx] = count
            return count
        
        return max(dfs(nums, 0), dfs(nums, 1)) if len(nums) > 1 else nums[0]

