class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLUMNS = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)

        result: list[str] = []

        def dfsSearch(
            cur: TrieNode, row: int, col: int, visited: set[tuple[int, int]], level: int, word: str
        ) -> None:
            if (
                min(row, col) < 0
                or row == ROWS
                or col == COLUMNS
                or (row, col) in visited
                or level > 10
            ):
                return

            c = board[row][col]
            if c not in cur.children:
                return
            new_word = word + c
            node = cur.children[c]
            visited.add((row, col))
            if node.word:
                node.word = False
                result.append(new_word)
            dfsSearch(node, row + 1, col, visited, level + 1, new_word)
            dfsSearch(node, row - 1, col, visited, level + 1, new_word)
            dfsSearch(node, row, col + 1, visited, level + 1, new_word)
            dfsSearch(node, row, col - 1, visited, level + 1, new_word)
            visited.remove((row, col))

        for row in range(ROWS):
            for col in range(COLUMNS):
                dfsSearch(trie.root, row, col, set(), 1, "")

        return result
