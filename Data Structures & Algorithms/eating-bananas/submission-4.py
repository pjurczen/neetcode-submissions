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
            if self.isOptimal(piles, guess, h) < 0:
                best_solution = min(guess, best_solution)
                high = guess - 1
            elif self.isOptimal(piles, guess, h) > 0:
                low = guess + 1
            else:
                return guess
        return best_solution
    
    def isOptimal(self, piles: List[int], guess: int, hours: int) -> int:
        spent_hours: int = 0
        for p in piles:
            spent_hours += ceil(p/guess)
        if spent_hours > hours:
            return 1
        if spent_hours <= hours:
            return -1