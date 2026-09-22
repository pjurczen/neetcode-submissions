class Solution:
    cache: dict[int, int] = {}

    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n < 0:
            return 0
        if n in self.cache:
            return self.cache[n]
        result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        self.cache[n] = result
        return result
        