import math

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stonesSum = sum(stones) # 23
        target = math.ceil(stonesSum / 2) # 12
        
        dp: list[list[int]] = [[0] * (target + 1) for _ in range(len(stones) + 1)]

        for t in range(target + 1):
            dp[len(stones)][t] = abs(t - (stonesSum - t))

        for i in range(len(stones) - 1, -1, -1):
            for t in range(target):
                skip = dp[i + 1][t]

                new_t = t + stones[i]
                if new_t >= target:
                    take = abs(new_t - (stonesSum - new_t))
                else:
                    take = dp[i + 1][new_t]

                dp[i][t] = min(skip, take)
                       
        return dp[0][0]
        

