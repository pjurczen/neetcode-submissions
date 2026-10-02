class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if i == offset * 2:
                offset *= 2
            dp[i] = 1 + dp[i - offset]
        return dp
# 0000 0
# 0001 1
# 0010 2
# 0011 3
# 0100 4
# 0101 5
# 0110 6
# 0111 7
# 1000 8
# 1001 9
# 1110 10
# 1111 11
# 10000 12
# 10001 13
# 10010 14
# 10011 15
# 10100 16
# 10101 17
# 10110 18
# 10111 19
# 11000 20

