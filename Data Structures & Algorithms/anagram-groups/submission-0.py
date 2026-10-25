from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            counts = [0] * 26 # a-z
            for c in s:
                counts[ord(c) - ord("a")] += 1
            
            result[tuple(counts)].append(s)
        
        return [value for _, value in result.items()]