class Solution:
    def numDecodings(self, s: str) -> int:
        
        prev = 1
        prevPrev = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                cur = 0
            else:
                cur = prev
            
                if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and int(s[i + 1]) <= 6)):
                    cur += prevPrev
            
            prevPrev = prev
            prev = cur
        
        return prev