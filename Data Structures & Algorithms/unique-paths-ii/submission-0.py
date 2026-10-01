class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(obstacleGrid), len(obstacleGrid[0])
        cache: list[list[int]] = [[0] * COLUMNS for _ in range(ROWS)]

        def dfs(row: int, col: int) -> int:
            if row == ROWS or col == COLUMNS:
                return 0
            if obstacleGrid[row][col] == 1:
                return 0
            if row == ROWS - 1 and col == COLUMNS - 1:
                return 1
            if cache[row][col] != 0:
                return cache[row][col]

            paths: int = 0
            paths += dfs(row + 1, col)
            paths += dfs(row, col + 1)
            
            cache[row][col] = paths

            return paths
        
        return dfs(0, 0)