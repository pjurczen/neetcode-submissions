class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache: list[list[int]] = [[0] * n for _ in range(m)]
        
        def dfs(row: int, col: int) -> int:
            if row == m or col == n:
                return 0
            if cache[row][col] != 0:
                return cache[row][col]
            if row == m - 1 and col == n - 1:
                return 1
            result = 0
            result += dfs(row + 1, col)
            result += dfs(row, col + 1)
            cache[row][col] = result
            return result

        return dfs(0, 0)