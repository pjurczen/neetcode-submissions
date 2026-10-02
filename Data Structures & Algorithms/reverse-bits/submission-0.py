class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        i = 0
        while i < 32:
            if n & (2**i):
                result = result ^ (2**(31-i))
            i += 1
        return result
