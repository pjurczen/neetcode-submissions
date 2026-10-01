class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS, COLUMNS = m, n
        prevRow = [0] * COLUMNS

        for _ in range(ROWS - 1, -1, -1):
            curRow = [0] * COLUMNS
            curRow[COLUMNS - 1] = 1
            for col in range(COLUMNS - 2, -1, -1):
                curRow[col] = curRow[col + 1] + prevRow[col]
            prevRow = curRow

        return prevRow[0]
