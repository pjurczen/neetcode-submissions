class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i: int = 0
        j: int = 0
        k = len(nums) - 1
        mid = 1
        
        while j <= k:
            if nums[j] < mid:
                tmp = nums[j]
                nums[j] = nums[i]
                nums[i] = tmp
                i += 1
                j += 1
            elif nums[j] > mid:
                tmp = nums[k]
                nums[k] = nums[j]
                nums[j] = tmp
                k -= 1
            else:
                j += 1
