class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(obstacleGrid), len(obstacleGrid[0])
        
        prevRow = [0] * (COLUMNS + 1)

        prevRow[COLUMNS - 1] = 1 if obstacleGrid[ROWS - 1][COLUMNS - 1] == 0 else 0

        for row in range(ROWS - 1, -1, -1):
            curRow = [0] * (COLUMNS + 1)
            for col in range(COLUMNS - 1, -1, -1):
                if obstacleGrid[row][col] == 1:
                    curRow[col] = 0
                else:
                    curRow[col] = curRow[col + 1] + prevRow[col]
            prevRow = curRow
        
        return prevRow[0]