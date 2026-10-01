from collections import deque


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(obstacleGrid), len(obstacleGrid[0])
        queue = deque()
        queued = set()
        queue.append((0, 0))
        queued.add((0, 0))
        paths = [[0] * COLUMNS for _ in range(ROWS)]
        if obstacleGrid[0][0] == 0:
            paths[0][0] = 1
        directions = [(1, 0), (0, 1)]

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if new_row < ROWS and new_col < COLUMNS and obstacleGrid[new_row][new_col] != 1:
                    paths[new_row][new_col] += paths[row][col]
                    if (new_row, new_col) not in queued:
                        queue.append((new_row, new_col))
                        queued.add((new_row, new_col))

        return paths[ROWS - 1][COLUMNS - 1]
