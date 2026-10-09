class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLUMNS = len(matrix), len(matrix[0])
        paths: list[list[int]] = [[0] * COLUMNS for _ in range(ROWS)]
        longestPath = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(row: int, col: int, prevVal: int) -> int:
            if min(row, col) < 0 or row == ROWS or col == COLUMNS or matrix[row][col] <= prevVal:
                return 0
            if paths[row][col] > 0:
                return paths[row][col]
            paths[row][col] = max([dfs(row+dr, col+dc, matrix[row][col]) for dr, dc in directions]) + 1
            return paths[row][col]


        for row in range(ROWS):
            for col in range(COLUMNS):
                longestPath = max(longestPath, dfs(row, col, -1))

        return longestPath