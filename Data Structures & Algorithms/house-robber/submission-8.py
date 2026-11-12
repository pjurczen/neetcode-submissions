class Solution:

    def rob(self, nums: List[int]) -> int:
        cache: dict[int, int] = {}
       
        def dfs(idx: int) -> int:
            if idx in cache:
                return cache[idx]
            if idx >= len(nums):
                return 0

            first = dfs(idx+1)
            second = nums[idx] + dfs(idx+2)
            count = max(first, second)

            cache[idx] = count
            return count
        
        return dfs(0)

