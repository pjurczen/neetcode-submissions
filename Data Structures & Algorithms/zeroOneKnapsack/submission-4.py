class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity + 1
        lastRow: list[int] = [0] * M
        
        for c in range(M):
            if weight[0] <= c:
                lastRow[c] = profit[0]
        
        for i in range(1, N):
            newRow = [0] * M
            for c in range(1, M):
                skip = lastRow[c]
                take = 0
                newCap = c - weight[i]
                if newCap >= 0:
                    take = profit[i] + lastRow[newCap]
                newRow[c] = max(skip, take)
            lastRow = newRow

        return lastRow[M - 1]
