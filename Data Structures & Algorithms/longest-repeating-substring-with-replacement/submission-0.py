class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # BAAABACBAAAA
        result: int = 0
        L: int = 0
        counts: dict[str, int] = {}

        for R in range(len(s)):
            counts[s[R]] = 1 + counts.get(s[R], 0)

            while (R - L + 1) - max(counts.values()) > k:
                counts[s[L]] -= 1
                L += 1
            
            result = max(result, R - L + 1)

        return result
