class TrieNode:

    def __init__(self) -> None:
        self.children = {}

class Trie:

    def __init__(self) -> None:
        self.root = TrieNode()

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLUMNS = len(board), len(board[0])
        trie = Trie()

        def dfsInsert(cur: TrieNode, row: int, col: int, level: int, visited: set[tuple[int, int]]) -> None:
            if min(row, col) < 0 or row == ROWS or col == COLUMNS or (row, col) in visited or level > 10:
                return
            c = board[row][col]
            if c not in cur.children:
                cur.children[c] = TrieNode()
            visited.add((row, col))
            dfsInsert(cur.children[c], row + 1, col, level + 1, visited)
            dfsInsert(cur.children[c], row - 1, col, level + 1, visited)
            dfsInsert(cur.children[c], row, col + 1, level + 1, visited)
            dfsInsert(cur.children[c], row, col - 1, level + 1, visited)
            visited.remove((row, col))

        for row in range(ROWS):
            for col in range(COLUMNS):
                dfsInsert(trie.root, row,  col, 1, set())
        
        return [w for w in words if trie.search(w)]

        