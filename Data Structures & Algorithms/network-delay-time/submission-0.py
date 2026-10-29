from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for s, d, t in times:
            adj[s].append((d, t))

        minHeap = [(0, k)]
        shortestPath = {}
        time = 0

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in shortestPath:
                continue
            
            shortestPath[n1] = t1
            time = t1

            for n2, t2 in adj[n1]:
                heapq.heappush(minHeap, (t1 + t2, n2))

        return time if len(shortestPath) == n else -1
