class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total: int = sum(nums)
        if total % 2 != 0:
            return False
        
        half: int = total // 2
        N, M = len(nums), half + 1
        cache: dict[tuple[int, int], bool] = {}

        def dfs(i: int, cur: int):
            if cur == half:
                return True
            if i == len(nums) or cur > half:
                return False
            key = (i, cur)
            if key in cache:
                return cache[key]

            cache[key] = dfs(i + 1, cur) or dfs(i + 1, cur + nums[i])
            
            return cache[key]

        return dfs(0, 0)