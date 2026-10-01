class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        cache: dict[tuple[int, int], int] = {}

        def dfs(i: int, j: int) -> int:
            if j == len(text2) or i == len(text1):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            if text1[i] == text2[j]:
                cache[(i, j)] = 1 + dfs(i+1, j+1)
            else:
                cache[(i, j)] = max(dfs(i+1, j), dfs(i, j+1))
            return cache[(i, j)]

        return dfs(0, 0)