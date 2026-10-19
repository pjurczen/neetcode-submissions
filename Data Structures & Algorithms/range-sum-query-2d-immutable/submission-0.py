class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLUMNS = len(matrix), len(matrix[0])
        self.prefix = [[0] * COLUMNS for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLUMNS):
                self.prefix[r][c] = (
                    self._getVal(self.prefix, r - 1, c)
                    + self._getVal(self.prefix, r, c - 1)
                    - self._getVal(self.prefix, r - 1, c - 1)
                    + matrix[r][c]
                )

    def _getVal(self, matrix: list[list[int]], row: int, col: int) -> int:
        if min(row, col) < 0:
            return 0
        return matrix[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefix[row2][col2]
            - self._getVal(self.prefix, row2, col1 - 1)
            - self._getVal(self.prefix, row1 - 1, col2)
            + self._getVal(self.prefix, row1 - 1, col1 - 1)
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
