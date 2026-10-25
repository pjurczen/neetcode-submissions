class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count: dict[str, int] = defaultdict(int)
        s2Count: dict[str, int] = defaultdict(int)
        for i in range(len(s1)):
            s1Count[s1[i]] = 1 + s1Count[s1[i]]
            s2Count[s2[i]] = 1 + s2Count[s2[i]]
        
        matches = 0
        for i in range(26):
            if s1Count[chr(ord('a') + i)] == s2Count[chr(ord('a') + i)]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            s2Count[s2[r]] += 1
            if s2Count[s2[r]] == s1Count[s2[r]]:
                matches += 1
            elif s1Count[s2[r]] + 1 == s2Count[s2[r]]:
                matches -= 1
            
            s2Count[s2[l]] -= 1
            if s2Count[s2[l]] == s1Count[s2[l]]:
                matches += 1
            elif s1Count[s2[l]] - 1 == s2Count[s2[l]]:
                matches -= 1
            l += 1

        return matches == 26