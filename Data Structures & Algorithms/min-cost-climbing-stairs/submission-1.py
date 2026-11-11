class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        plusOne = cost[-1]
        plusTwo = 0

        for i in range(len(cost) - 2, -1, -1):
            cur = cost[i] + min(plusOne, plusTwo)
            plusTwo = plusOne
            plusOne = cur
        
        return min(plusOne, plusTwo)
