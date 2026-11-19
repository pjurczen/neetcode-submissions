import math

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stonesSum = sum(stones) # 23
        target = math.ceil(stonesSum / 2) # 12
        
        dp: list[list[int]] = [[-1] * (target + 1) for _ in range(len(stones))]

        def dfs(i: int, total: int) -> int:
            if total >= target or i == len(stones):
                return abs(total - (stonesSum - total))
            if dp[i][total] != -1:
                return dp[i][total]
            
            dp[i][total] = min(
                dfs(i + 1, total), dfs(i + 1, total + stones[i])
            )
            
            return dp[i][total]
        
        return dfs(0, 0)
        

