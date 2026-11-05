class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []

        def dfs(open: int, close: int) -> None:
            if len(path) == 2*n:
                result.append("".join(path))
                return
            
            if open < n:
                path.append("(")
                dfs(open + 1, close)
                path.pop()
            if close < n and close < open:
                path.append(")")
                dfs(open, close + 1)
                path.pop()
            
        dfs(0, 0)
        
        return result