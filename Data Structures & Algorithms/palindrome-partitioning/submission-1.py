class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result: list[list[str]] = []
        palindromes: list[str] = []
        def dfs(i: int) -> None:
            if i == len(s):
                result.append(palindromes.copy())
                return
            
            for j in range(i, len(s)):
                val = s[i:j + 1]
                if val == val[::-1]:
                    palindromes.append(val)
                    dfs(j+1)
                    palindromes.pop()

        dfs(0)

        return result