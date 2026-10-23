class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result: list[list[int]] = []
        subset: list[int] = []

        def _helper(i: int) -> None:
            if i == len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            _helper(i + 1)
            subset.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            _helper(i + 1)

        _helper(0)
        return result