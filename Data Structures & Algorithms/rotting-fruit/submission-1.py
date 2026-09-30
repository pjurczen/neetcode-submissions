from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        freshFruits: int = 0
        minutes: int = -1
        queue = deque()
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for row in range(ROWS):
            for col in range(COLUMNS):
                val = grid[row][col]
                if val == 1:
                    freshFruits += 1
                elif val == 2:
                    queue.append((row, col))
                    
        if freshFruits == 0:
            return 0
        
        freshFruits += len(queue)

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in deltas:
                    new_row, new_col = row + dr, col + dc
                    if (
                        min(new_row, new_col) < 0
                        or new_row == ROWS
                        or new_col == COLUMNS
                        or grid[new_row][new_col] != 1
                    ):
                        continue
                    queue.append((new_row, new_col))
                    grid[new_row][new_col] = 2
                freshFruits -= 1

            minutes += 1

            if freshFruits == 0:
                return minutes

        return -1
