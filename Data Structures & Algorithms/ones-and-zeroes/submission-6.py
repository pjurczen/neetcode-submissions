class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        N = len(strs)
        counts: list[tuple[int, int]] = [(s.count('0'), s.count('1')) for s in strs]

        dp: list[list[int]] = [[0] * (n + 1) for _ in range(m + 1)]

        for zeros, ones in counts:
            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                    skip = dp[i][j]
                    take = 0
                    newZeros, newOnes = i - zeros, j - ones
                    if newZeros >= 0 and newOnes >= 0:
                        take = dp[newZeros][newOnes] + 1
                    dp[i][j] = max(skip, take)

        return dp[m][n]