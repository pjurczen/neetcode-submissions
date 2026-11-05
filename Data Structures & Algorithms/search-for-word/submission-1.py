class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLUMNS = len(board), len(board[0])

        def dfs(i: int, row: int, col: int, visited: set[tuple[int, int]]) -> bool:
            if i == len(word):
                return True
            if (
                min(row, col) < 0
                or row == ROWS
                or col == COLUMNS
                or (row, col) in visited
                or board[row][col] != word[i]
            ):
                return False
            visited.add((row, col))
            if dfs(i+1, row+1, col, visited):
                return True
            elif dfs(i+1, row-1, col, visited):
                return True
            elif dfs(i+1, row, col+1, visited):
                return True
            elif dfs(i+1, row, col-1, visited):
                return True
            visited.remove((row, col))
            return False

        for r in range(ROWS):
            for c in range(COLUMNS):
                if dfs(0, r, c, set()):
                    return True
        
        return False