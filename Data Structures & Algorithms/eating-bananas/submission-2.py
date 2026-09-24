from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = 0
        for p in piles:
            max_val = max(p, max_val)
        
        low: int = 1
        high: int = max_val
        while low <= high:
            guess = (high + low) // 2
            if self.isOptimal(piles, guess, h) < 0:
                high = guess - 1
            elif self.isOptimal(piles, guess, h) > 0:
                low = guess + 1
            else:
                return guess
    
    def isOptimal(self, piles: List[int], guess: int, hours: int) -> int:
        spent_hours: int = 0
        spent_hours_lower: int = 0
        guess_lower = guess - 1
        for p in piles:
            spent_hours += ceil(p/guess)
            if guess_lower > 0:
                spent_hours_lower += ceil(p/guess_lower)
        if spent_hours > hours:
            return 1
        if spent_hours <= hours and (guess_lower != 0 and spent_hours_lower <= hours):
            return -1
        return 0