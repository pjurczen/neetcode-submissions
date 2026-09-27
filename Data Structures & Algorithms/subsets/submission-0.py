class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        def _subsets(nums: List[int], path: List[int]) -> List[List[int]]:
            if not nums:
                return []
            
            cur = nums[0]
            curPath = path + [cur]
            subResults = [curPath]
            for i in range(1, len(nums[1:]) + 1):
                subResults += _subsets(nums[i:], curPath)
            return subResults

        for i in range(len(nums)):
            result += _subsets(nums[i:], [])

        return result
