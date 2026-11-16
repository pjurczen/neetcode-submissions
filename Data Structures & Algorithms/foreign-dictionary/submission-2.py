from collections import defaultdict


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = {c: set() for word in words for c in word}

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
