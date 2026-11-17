class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total: int = sum(nums)
        if total % 2 != 0:
            return False
        
        half: int = total // 2
        N, M = len(nums), half + 1
        cache: list[list[bool | None]] = [[None] * M for _ in range(N)]

        def dfs(i: int, cur: int):
            if cur == half:
                return True
            if i == len(nums) or cur > half:
                return False
            if cache[i][cur] is not None:
                return cache[i][cur]

            cache[i][cur] = dfs(i + 1, cur) or dfs(i + 1, cur + nums[i])
            
            return cache[i][cur]

        return dfs(0, 0)