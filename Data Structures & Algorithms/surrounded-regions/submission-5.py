class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLUMNS = len(board), len(board[0])

        stack = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(ROWS):
            stack.append((r, 0))
            stack.append((r, COLUMNS - 1))

        for c in range(COLUMNS):
            stack.append((0, c))
            stack.append((ROWS - 1, c))
        
        while stack:
            row, col = stack.pop()

            if board[row][col] != 'O':
                continue

            board[row][col] = 'T'

            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if min(nr, nc) >= 0 and nr < ROWS and nc < COLUMNS:
                    stack.append((nr, nc))

        for r in range(ROWS):
            for c in range(COLUMNS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
