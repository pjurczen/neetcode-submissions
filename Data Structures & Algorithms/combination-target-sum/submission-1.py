class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result: list[list[int]] = []
        
        subset: list[int] = []
        def _helper(i: int, total: int) -> None:
            if total == target:
                result.append(subset.copy())
                return
            if total > target:
                return
            
            for j in range(i, len(nums)):
                total += nums[j]
                subset.append(nums[j])
                _helper(j, total)
                total -= nums[j]
                subset.pop()

        _helper(0, 0)

        return result