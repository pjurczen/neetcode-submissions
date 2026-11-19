import math

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stonesSum = sum(stones) # 23
        target = math.ceil(stonesSum / 2) # 12
        
        dp: dict[tuple[int, int], int] = {}

        def dfs(i: int, total: int) -> int:
            if total >= target or i == len(stones):
                return abs(total - (stonesSum - total))
            key = (i, total)
            if key in dp:
                return dp[key]
            
            dp[key] = min(
                dfs(i + 1, total), dfs(i + 1, total + stones[i])
            )
            
            return dp[key]
        
        return dfs(0, 0)
        

