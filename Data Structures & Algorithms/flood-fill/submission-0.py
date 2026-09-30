class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startingColor = image[sr][sc]
        self.dfs(image, sr, sc, startingColor, color, set())
        return image

    def dfs(
        self,
        image: List[List[int]],
        row: int,
        column: int,
        startingColor: int,
        color: int,
        visited: set[tuple[int, int]],
    ) -> None:
        ROWS, COLUMNS = len(image), len(image[0])
        if (
            min(row, column) < 0
            or row >= ROWS
            or column >= COLUMNS
            or image[row][column] != startingColor
            or (row, column) in visited
        ):
            return

        image[row][column] = color

        visited.add((row, column))

        self.dfs(image, row + 1, column, startingColor, color, visited)
        self.dfs(image, row - 1, column, startingColor, color, visited)
        self.dfs(image, row, column + 1, startingColor, color, visited)
        self.dfs(image, row, column - 1, startingColor, color, visited)

