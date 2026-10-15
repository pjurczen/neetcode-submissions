class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax = nums[0]
        curMax = 0
        globalMin = nums[0]
        curMin = 0
        total = 0

        for n in nums:
            curMax = max(curMax + n, n)
            globalMax = max(globalMax, curMax)
            curMin = min(curMin + n, n)
            globalMin = min(globalMin, curMin)
            total += n
        
        return globalMax if globalMax < 0 else max(globalMax, total - globalMin)