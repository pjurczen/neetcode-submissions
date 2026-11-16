from collections import defaultdict


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList: dict[str, set[str]] = defaultdict(set)
        chars: set[str] = set()
        for word in words:
            for c in word:
                chars.add(c)
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            j: int = 0
            while j < len(w1) and j < len(w2) and w1[j] == w2[j] :
                j += 1
            if j < len(w1) and j == len(w2):
                return ""
            elif j < len(w1) and j < len(w2):
                adjList[w2[j]].add(w1[j])
            
        visited: set[str] = set()
        path: set[str] = set()
        result = ""

        def dfs(c: str) -> bool:
            nonlocal result
            if c in path:
                return False
            if c in visited:
                return True

            visited.add(c)
            path.add(c)

            for n in adjList[c]:
                if not dfs(n):
                    return False
            
            path.remove(c)

            result += c
            return True

        for c in chars:
            if not dfs(c):
                return ""

        return result
