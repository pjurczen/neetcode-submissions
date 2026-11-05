class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLUMNS = len(board), len(board[0])
        L = len(word)
        boardCounter = Counter([ch for row in board for ch in row])
        for ch, k in Counter(word).items():
            if boardCounter[ch] < k:
                return False

        if word[0] > word[-1]:
            word = word[::-1]

        def dfs(i: int, row: int, col: int) -> bool:
            if i == L:
                return True
            if (
                min(row, col) < 0
                or row == ROWS
                or col == COLUMNS
                or board[row][col] != word[i]
            ):
                return False
            tmp = board[row][col]
            board[row][col] = "#"
            if dfs(i+1, row+1, col):
                return True
            elif dfs(i+1, row-1, col):
                return True
            elif dfs(i+1, row, col+1):
                return True
            elif dfs(i+1, row, col-1):
                return True
            board[row][col] = tmp
            return False

        for r in range(ROWS):
            for c in range(COLUMNS):
                if dfs(0, r, c):
                    return True
        
        return False