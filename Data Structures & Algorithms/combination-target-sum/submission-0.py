class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i: int, path: list[int], sum: int) -> None:
            if sum == target:
                result.append(path)
                return
            if i >= len(nums) or sum > target:
                return

            val = nums[i]
            dfs(i, path + [val], sum + val)
            dfs(i+1, path, sum)

        dfs(0, [], 0)

        return result