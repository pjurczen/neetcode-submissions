class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        
        cache: dict[tuple[int, int], int] = {}

        def dfs(i: int, capacity: int) -> int:
            if i == len(profit):
                return 0
            key = (i, capacity)
            if key in cache:
                return cache[key]
            
            skip = dfs(i + 1, capacity)
            take = 0
            newCap = capacity - weight[i]
            if newCap >= 0:
                take = profit[i] + dfs(i, newCap)
            
            cache[key] = max(skip, take)
            return cache[key]
        
        return dfs(0, capacity)