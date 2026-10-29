from collections import defaultdict

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i in range(len(edges)):
            a, b = edges[i]
            prob = succProb[i]
            adj[a].append((b, prob))
            adj[b].append((a, prob))
        
        maxHeap = []
        visited = set()
        for dest, prob in adj[start_node]:
            heapq.heappush_max(maxHeap, (prob, dest))
        
        while maxHeap:
            prob1, dest1 = heapq.heappop_max(maxHeap)
            if dest1 == end_node:
                return prob1

            visited.add(dest1)

            for dest2, prob2 in adj[dest1]:
                if dest2 not in visited:
                    heapq.heappush_max(maxHeap, (prob1 * prob2, dest2))
        
        return 0
        