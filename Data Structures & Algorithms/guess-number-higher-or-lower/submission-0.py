# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        high = n
        low = 1

        while low <= high:
            middle = (high + low) // 2
            guess_result: int = guess(middle)
            if guess_result < 0:
                high = middle - 1
            elif guess_result > 0:
                low = middle + 1
            else:
                return middle
