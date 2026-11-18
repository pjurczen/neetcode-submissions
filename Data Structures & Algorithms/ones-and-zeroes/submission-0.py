from collections import Counter
from functools import cache

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        counts: dict[int, Counter] = {}
        for i, s in enumerate(strs):
            counts[i] = Counter(s)
        
        @cache
        def dfs(i: int, m: int, n: int) -> int:
            if i == len(strs) or (m == 0 and n == 0):
                return 0
            
            skip = dfs(i + 1, m, n)
            take = 0
            newM, newN = m - counts[i]['0'], n - counts[i]['1']
            if newM >= 0 and newN >= 0:
                take = dfs(i + 1, newM, newN) + 1

            return max(skip, take)
        
        return dfs(0, m, n)

            