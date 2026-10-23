class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result: list[list[int]] = []
        subset: list[int] = []
        def _helper(i: int) -> None:
            if i == len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            _helper(i + 1)
            subset.pop()

            _helper(i + 1)

        _helper(0)
        return result