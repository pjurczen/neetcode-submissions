class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count: int = 0

        def dfs(grid: list[list[str]], row: int, col: int) -> None:
            if min(row, col) < 0 or row >= ROWS or col >= COLUMNS or grid[row][col] != '1':
                return
            
            grid[row][col] = '2'

            dfs(grid, row + 1, col)
            dfs(grid, row - 1, col)
            dfs(grid, row, col + 1)
            dfs(grid, row, col - 1)


        ROWS, COLUMNS = len(grid), len(grid[0])
        for row in range(ROWS):
            for col in range(COLUMNS):
                value = grid[row][col]
                if value == '1':
                    dfs(grid, row, col)
                    count += 1

        return count
