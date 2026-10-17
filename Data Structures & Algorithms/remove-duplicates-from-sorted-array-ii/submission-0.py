class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L, R = 0, 0

        while R < len(nums):
            count = 1
            while R < len(nums) - 1 and nums[R] == nums[R + 1]:
                R += 1
                count += 1

            for i in range(min(2, count)):
                nums[L] = nums[R]
                L += 1
            R += 1

        return L
