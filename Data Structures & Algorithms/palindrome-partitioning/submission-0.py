class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result: list[list[str]] = []
        palindromes: list[str] = []
        def dfs(i: int, j: int) -> None:
            if j == len(s):
                if i == j:
                    result.append(palindromes.copy())
                return
            
            dfs(i, j+1)

            val = s[i:j + 1]
            if val == val[::-1]:
                palindromes.append(val)
                dfs(j+1, j+1)
                palindromes.pop()


        dfs(0, 0)

        return result