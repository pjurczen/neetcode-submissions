class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result: list[list[int]] = []
        
        subset: list[int] = []
        def _helper(i: int, total: int) -> None:
            if total == target:
                result.append(subset.copy())
                return
            if i == len(nums) or total > target:
                return
            
            total += nums[i]
            subset.append(nums[i])
            _helper(i, total)
            total -= nums[i]
            subset.pop()
            _helper(i+1, total)

        _helper(0, 0)

        return result