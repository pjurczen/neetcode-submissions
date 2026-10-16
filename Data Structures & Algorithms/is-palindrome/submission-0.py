class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1
        while L < R:
            if not (s[L].isascii() and s[L].isalnum()):
                L += 1
            elif not (s[R].isascii() and s[R].isalnum()):
                R -= 1
            else:
                if s[L].lower() != s[R].lower():
                    return False
                L += 1
                R -= 1
        return True