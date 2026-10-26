class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countS: dict[str, int] = {}
        countT: dict[str, int] = {}
        
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        matches: int = 0
        bestL, bestR = None, None

        l, r = 0, 0

        while r < len(s):
            countS[s[r]] = 1 + countS.get(s[r], 0)

            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                matches += 1

            while matches == len(countT):
                if bestL is None or r - l < bestR - bestL:
                    bestL = l
                    bestR = r

                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    matches -= 1

                l += 1

            r += 1

        return s[bestL : bestR + 1] if bestL != None else ""