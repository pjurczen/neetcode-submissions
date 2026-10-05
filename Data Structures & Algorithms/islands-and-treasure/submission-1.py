from collections import deque


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLUMNS = len(grid), len(grid[0])
        INF = 2147483647

        queue = deque()
        queued = set()
        for row in range(ROWS):
            for col in range(COLUMNS):
                if grid[row][col] == 0:
                    queue.append((row, col))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        path = 0

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                grid[row][col] = path
                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if (
                        new_row >= 0
                        and new_col >= 0
                        and new_row < ROWS
                        and new_col < COLUMNS
                        and grid[new_row][new_col] == INF
                        and (new_row, new_col) not in queued
                    ):
                        queued.add((new_row, new_col))
                        queue.append((new_row, new_col))
            path += 1
