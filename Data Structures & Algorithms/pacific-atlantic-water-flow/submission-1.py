class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        ROWS, COLUMNS = len(heights), len(heights[0])
        pacificAccess: set[tuple[int, int]] = set()
        atlanticAccess: set[tuple[int, int]] = set()
        directions: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result: list[list[int]] = []

        def dfs(row: int, col: int, visited: set[tuple[int, int]]) -> None:
            visited.add((row, col))
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (
                    min(nr, nc) >= 0
                    and nr < ROWS
                    and nc < COLUMNS
                    and (nr, nc) not in visited
                    and heights[nr][nc] >= heights[row][col]
                ):
                    dfs(nr, nc, visited)

        for r in range(ROWS):
            dfs(r, 0, pacificAccess)
            dfs(r, COLUMNS - 1, atlanticAccess)

        for c in range(COLUMNS):
            dfs(0, c, pacificAccess)
            dfs(ROWS - 1, c, atlanticAccess)

        for r in range(ROWS):
            for c in range(COLUMNS):
                if (r, c) in pacificAccess and (r, c) in atlanticAccess:
                    result.append([r, c])

        return result
