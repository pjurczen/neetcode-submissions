class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity + 1
        cache: list[list[int]] = [[-1] * M for _ in range(N)]

        def dfs(i: int, c: int) -> int:
            if i == len(profit):
                return 0
            if cache[i][c] != -1:
                return cache[i][c]
            
            skip = dfs(i + 1, c)
            res = skip

            newCap = c - weight[i]
            if newCap >= 0:
                take = dfs(i + 1, newCap) + profit[i]
                res = max(skip, take)
            
            cache[i][c] = res

            return res
        
        return dfs(0, capacity)