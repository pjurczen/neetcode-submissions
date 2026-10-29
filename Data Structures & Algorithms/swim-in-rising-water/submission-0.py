import heapq
from collections import defaultdict

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLUMNS = len(grid), len(grid[0])
        minHeap = [(grid[0][0], (0, 0))]
        visited = set()
        elevation = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while minHeap:
            e1, (r1, c1) = heapq.heappop(minHeap)
            
            visited.add((r1, c1))
            elevation = max(elevation, e1)

            if r1 == ROWS - 1 and c1 == COLUMNS - 1:
                return elevation

            for dr, dc in directions:
                r2, c2 = r1 + dr, c1 + dc
                if min(r2, c2) >= 0 and r2 < ROWS and c2 < COLUMNS and (r2, c2) not in visited:
                    heapq.heappush(minHeap, (grid[r2][c2], (r2, c2)))
        
