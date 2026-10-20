class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    root: TrieNode

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        
        def dfs(cur: TrieNode, i: int) -> bool:
            if i == len(word):
                return cur.word
            if word[i] not in cur.children and word[i] != '.':
                return False
            result = False
            if word[i] in cur.children:
                result |= dfs(cur.children[word[i]], i+1)
            elif word[i] == '.':
                for child in cur.children.values():
                    result |= dfs(child, i+1)
                    if result:
                        return True

            return result
        
        return dfs(self.root, 0)