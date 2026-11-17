class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        total = sum(nums)
        if abs(target) > total:
            return 0
 
        dp: dict[int, int] = {0: 1}

        for n in nums:
            tmp = {}
            for cur, count in dp.items():
                tmp[cur + n] = tmp.get(cur + n, 0) + count
                tmp[cur - n] = tmp.get(cur - n, 0) + count
            dp = tmp
        
        return dp.get(target, 0)
