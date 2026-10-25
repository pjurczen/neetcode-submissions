import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts: dict[int, int] = {}
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)
        
        topFreq = 0

        freq = [[] for _ in range(len(nums) + 1)]
        for n, c in counts.items():
            freq[c].append(n)
            topFreq = max(topFreq, c)
        
        result = []
        for c in range(topFreq, -1, -1):
            elems = freq[c]
            for e in elems:
                result.append(e)
                if len(result) == k:
                    return result

        return result