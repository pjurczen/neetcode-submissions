from functools import cache

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts: list[tuple[int, int]] = [(s.count('0'), s.count('1')) for s in strs]
        
        @cache
        def dfs(i: int, m: int, n: int) -> int:
            if i == len(strs) or (m == 0 and n == 0):
                return 0
            
            skip = dfs(i + 1, m, n)
            take = 0
            zeros, ones = counts[i]
            newM, newN = m - zeros, n - ones
            if newM >= 0 and newN >= 0:
                take = dfs(i + 1, newM, newN) + 1

            return max(skip, take)
        
        return dfs(0, m, n)

            