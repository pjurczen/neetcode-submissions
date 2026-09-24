from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = 0
        for p in piles:
            max_val = max(p, max_val)
        
        best_solution = max_val
        low: int = 1
        high: int = max_val
        while low <= high:
            guess = (high + low) // 2
            spent_hours: int = 0
            for p in piles:
                spent_hours += ceil(p/guess)
            if spent_hours <= h:
                best_solution = min(guess, best_solution)
                high = guess - 1
            elif spent_hours > h:
                low = guess + 1
        return best_solution
