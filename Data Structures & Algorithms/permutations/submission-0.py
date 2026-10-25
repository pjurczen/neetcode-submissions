class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def helper(i: int) -> list[list[int]]:
            if i == len(nums):
                return [[]]
            
            perm = helper(i + 1)
            result = []
            for p in perm:
                for j in range(len(p) + 1):
                    c: list[int] = p.copy()
                    c.insert(j, nums[i])
                    result.append(c)
            return result

        return helper(0)