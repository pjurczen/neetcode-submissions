class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def _subsets(nums: List[int], path: List[int]) -> None:
            if not nums:
                result.append(path)
                return
            cur = nums[0]
            curPath = path + [cur]

            _subsets(nums[1:], path + [cur])
            _subsets(nums[1:], path)
            
        _subsets(nums, [])

        return result
