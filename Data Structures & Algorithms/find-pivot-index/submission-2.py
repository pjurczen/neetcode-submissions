class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        postfixSums = [0 for _ in range(len(nums))]
        postfixTotal = 0
        prefixSum = 0

        for R in range(len(nums) - 1, -1, -1):
            postfixTotal += nums[R]
            postfixSums[R] = postfixTotal
        for L in range(len(nums)):
            prefixSum += nums[L]
            if prefixSum == postfixSums[L]:
                return L
        return -1
