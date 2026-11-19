import math

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stonesSum = sum(stones) # 23
        target = math.ceil(stonesSum / 2) # 12
        
        dp: list[int] = [0] * (target + 1)

        for t in range(target + 1):
            dp[t] = abs(t - (stonesSum - t))

        for i in range(len(stones) - 1, -1, -1):
            for t in range(target):
                skip = dp[t]

                new_t = t + stones[i]
                if new_t >= target:
                    take = abs(new_t - (stonesSum - new_t))
                else:
                    take = dp[new_t]

                dp[t] = min(skip, take)
                       
        return dp[0]
