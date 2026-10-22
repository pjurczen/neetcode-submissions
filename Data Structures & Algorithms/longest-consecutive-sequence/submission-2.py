class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        maxLength = 0
        for n in nums:
            if n-1 not in hashset:
                length = 1
                while n + length in hashset:
                    length += 1
                maxLength = max(length, maxLength)
        return maxLength