class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows: list[set[str]] = [set() for _ in range(9)]
        columns: list[set[str]] = [set() for _ in range(9)]
        subboxes: list[list[set[str]]] = [[set() for _ in range(3)] for _ in range(3)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val != ".":
                    if val in rows[row]:
                        return False
                    rows[row].add(val)
                    if val in columns[col]:
                        return False
                    columns[col].add(val)
                    if val in subboxes[row // 3][col // 3]:
                        return False
                    subboxes[row // 3][col // 3].add(val)

        return True