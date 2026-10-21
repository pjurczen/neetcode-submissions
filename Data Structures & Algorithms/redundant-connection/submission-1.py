class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = {}
        self.rank = {}

        for i in range(1, n + 1):
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, node: int) -> int:
        parent = self.parent[node]
        while parent != self.parent[parent]:
            self.parent[node] = self.parent[self.parent[node]]
            parent = self.parent[node]
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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for e1, e2 in edges:
            if not uf.union(e1, e2):
                return [e1, e2]
        return []
