class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        globalMax: int = 0
        currentMax: int = 0
        for n in nums:
            if n != 1:
                globalMax = max(currentMax, globalMax)
                currentMax = 0
            else:
                currentMax += 1
        globalMax = max(currentMax, globalMax)
        return globalMax
