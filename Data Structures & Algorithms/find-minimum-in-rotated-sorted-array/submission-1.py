class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]

        l, r = 0, len(nums) - 1

        while r - l > 1:
            m = (r + l) // 2
            if nums[m] < nums[l]:
                r = m
            else:
                l = m
        
        return min(nums[l], nums[r])