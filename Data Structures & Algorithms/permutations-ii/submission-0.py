class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counts: dict[int, int] = {}
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        result = []
        perm = []
        
        def dfs():
            if len(perm) == len(nums):
                result.append(perm.copy())
                return
            
            for n in counts.keys():
                if counts[n] > 0:
                    perm.append(n)
                    counts[n] -= 1

                    dfs()

                    perm.pop()
                    counts[n] += 1
        
        dfs()
        return result