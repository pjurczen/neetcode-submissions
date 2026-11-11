from collections import defaultdict
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # dict[point, list[tuple[distance, point]]]
        adj: dict[tuple[int, int], list[tuple[int, tuple[int]]]] = defaultdict(list)

        def distance(p1: tuple[int, int], p2: tuple[int, int]) -> int:
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1 = tuple(points[i])
                p2 = tuple(points[j])
                dist = distance(p1, p2)
                adj[p1].append((dist, p2))
                adj[p2].append((dist, p1))
        
        visited: set[tuple[int, int]] = set()
        minHeap = []
        total = 0
        p1 = tuple(points[0])
        for dist, p2 in adj[p1]:
            heapq.heappush(minHeap, (dist, p2))
        visited.add(p1)

        while len(visited) < len(points):
            dist, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            
            visited.add(node)
            total += dist

            for dist2, node2 in adj[node]:
                if node2 not in visited:
                    heapq.heappush(minHeap, (dist2, node2))

        return total