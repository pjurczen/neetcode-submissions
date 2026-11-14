import heapq

class UnionFind:

    def __init__(self, n: int):
        self.rank = {}
        self.parent = {}
        for i in range(n):
            self.rank[i] = 0
            self.parent[i] = i
    
    def find(self, node: int) -> int:
        parent = self.parent[node]
        while parent != self.parent[parent]:
            self.parent[parent] = self.parent[self.parent[parent]]
            parent = self.parent[parent]
        return parent
    
    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        else:
            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
            elif self.rank[p1] < self.rank[p2]:
                self.parent[p1] = p2
            else:
                self.parent[p2] = p1
                self.rank[p1] += 1
            return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minHeap = []

        def distance(p1: list[int], p2: list[int]) -> int:
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = distance(points[i], points[j])
                heapq.heappush(minHeap, (dist, i, j))
        
        cost = 0

        uf = UnionFind(len(points))
        while minHeap:
            dist, n1, n2 = heapq.heappop(minHeap)
            if uf.union(n1, n2):
                cost += dist

        return cost
