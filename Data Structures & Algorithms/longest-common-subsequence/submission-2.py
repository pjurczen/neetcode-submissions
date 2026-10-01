class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        ROWS, COLUMNS = len(text1), len(text2)
        grid = [[0] * (COLUMNS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLUMNS - 1, -1, -1):
                if text1[r] == text2[c]:
                    grid[r][c] = 1 + grid[r+1][c+1]
                else:
                    grid[r][c] = max(grid[r+1][c], grid[r][c+1])
        
        return grid[0][0]