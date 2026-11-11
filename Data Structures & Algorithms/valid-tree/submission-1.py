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
                self.rank[p1] += self.rank[p2]
            return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)
        for edge in edges:
            e1 = edge[0]
            e2 = edge[1]
            if not uf.union(e1, e2):
                return False
        
        parents = set()
        for i in range(n):
            parents.add(uf.find(i))
        
        return len(parents) == 1