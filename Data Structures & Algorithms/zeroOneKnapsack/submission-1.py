class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        
        cache: dict[tuple[int, int], int] = {}

        def dfs(i: int, c: int) -> int:
            if i == len(profit):
                return 0
            if (i, c) in cache:
                return cache[(i, c)]
            
            skip = dfs(i + 1, c)
            res = skip

            newCap = c - weight[i]
            if newCap >= 0:
                take = dfs(i + 1, newCap) + profit[i]
                res = max(skip, take)
            
            cache[(i, c)] = res

            return res
        
        return dfs(0, capacity)