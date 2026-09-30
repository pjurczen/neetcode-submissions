from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])

        length = 1
        queue = deque()
        visited: set[tuple] = set()
        if grid[0][0] == 0:
            queue.append((0, 0))
            visited.add((0, 0))

        deltas = [(1, 1), (1, 0), (1, -1), (-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1)]

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if row == ROWS - 1 and col == COLUMNS - 1:
                    return length
                for dr, dc in deltas:
                    new_row, new_col = row + dr, col + dc
                    if (
                        min(new_row, new_col) < 0
                        or new_row == ROWS
                        or new_col == COLUMNS
                        or grid[new_row][new_col] != 0
                        or (new_row, new_col) in visited
                    ):
                        continue
                    queue.append((new_row, new_col))
                    visited.add((new_row, new_col))
            length += 1

        return -1
