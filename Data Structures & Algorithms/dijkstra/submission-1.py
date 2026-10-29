from collections import defaultdict
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list) # (src, [(weight, dst)])
        
        # s=src, d=dest, w=weight
        for s, d, w in edges:
            adj[s].append((w, d))
        
        shortestPath = {}
        minHeap = [(0, src)]

        while minHeap:
            w, d = heapq.heappop(minHeap)
            if d in shortestPath:
                continue
            
            shortestPath[d] = w

            for w_n, d_n in adj[d]:
                heapq.heappush(minHeap, (w + w_n, d_n))

        for i in range(n):
            if i not in shortestPath:
                shortestPath[i] = -1
                
        return shortestPath
