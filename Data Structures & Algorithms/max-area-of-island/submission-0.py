class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxCount: int = 0
        ROWS, COLUMNS = len(grid), len(grid[0])

        def dfs(grid: list[list[int]], row: int, col: int) -> int:
            if min(row, col) < 0 or row == ROWS or col == COLUMNS or grid[row][col] != 1:
                return 0
            
            count = 1
            grid[row][col] = -1

            count += dfs(grid, row + 1, col)
            count += dfs(grid, row - 1, col)
            count += dfs(grid, row, col + 1)
            count += dfs(grid, row, col - 1)

            return count

        for row in range(ROWS):
            for col in range(COLUMNS):
                val: int = grid[row][col]
                if val == 1:
                    count = dfs(grid, row, col)
                    maxCount = max(count, maxCount)
        
        return maxCount
