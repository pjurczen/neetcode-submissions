class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp: list[int] = [-1] * len(s)

        def dfs(i: int) -> int:
            if i == len(s):
                return 1
            if i > len(s) or s[i] == '0':
                return 0
            if dp[i] != -1:
                return dp[i]
            
            res = dfs(i + 1)
            if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                res += dfs(i + 2)
            dp[i] = res
            return dp[i]

        return dfs(0)