class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result: list[list[str]] = []
        board: list[list[str]] = [["."] * n for _ in range(n)]
        
        def dfs(r: int) -> None:
            if r == n:
                cp: list[str] = ["".join(row) for row in board]
                result.append(cp)
                return
            
            for j in range(n):
                if self.canPlaceQueen(r, j, board):
                    board[r][j] = 'Q'
                    dfs(r + 1)
                    board[r][j] = '.'
        
        dfs(0)
        
        return result


    def canPlaceQueen(self, r: int, c: int, board: list[list[str]]) -> bool:
        for k in range(r):              # only rows above
            qc = board[k].index('Q')    # column of queen in row k
            if qc == c:                 # same column
                return False
            if abs(qc - c) == r - k:    # same diagonal
                return False
        return True