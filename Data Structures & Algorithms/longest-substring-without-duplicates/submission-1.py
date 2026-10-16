class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # zzxyzz
        # dvdf
        # pwwkew
        L, length = 0, 0
        hashset: set[str] = set()
        for R in range(len(s)):
            while s[R] in hashset:
                hashset.remove(s[L])
                L += 1

            hashset.add(s[R])
            length = max(length, R-L+1)

        return length