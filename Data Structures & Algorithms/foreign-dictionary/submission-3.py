from collections import defaultdict


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1] 
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    adjList[c2].add(c1)
                    break
            else:
                if len(w1) > len(w2):
                    return ""

        visited: dict[str, bool] = {}
        result = []

        def dfs(c: str) -> bool:
            nonlocal result
            if c in visited:
                return visited[c]

            visited[c] = True

            for n in adjList[c]:
                if dfs(n):
                    return True
            
            visited[c] = False

            result.append(c)
            return False

        for c in adjList.keys():
            if dfs(c):
                return ""

        return "".join(result)
