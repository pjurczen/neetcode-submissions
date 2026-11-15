class UnionFind:

    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, v: int) -> int:
        while v != self.parent[v]:
            self.parent[v] = self.parent[self.parent[v]]
            v = self.parent[v]
        return v
    
    def union(self, v1: int, v2: int) -> bool:
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return False
        if self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges): # (v1, v2, weight, idx)
            e.append(i)
        edges.sort(key=lambda x: x[2])

        mstWeight = 0
        uf = UnionFind(n)
        for v1, v2, w, i in edges:
            if uf.union(v1, v2):
                mstWeight += w
        
        critical, pseudo = [], []
        for v1, v2, w, i in edges:
            # Try without the edge
            uf = UnionFind(n)
            curWeight = 0
            for u1, u2, weight, j in edges:
                if (u1, u2) != (v1, v2) and uf.union(u1, u2):
                    curWeight += weight
            if max(uf.rank) < n or curWeight > mstWeight:
                critical.append(i)
                continue
            
            # Try with the edge
            uf = UnionFind(n)
            curWeight = w
            uf.union(v1, v2)
            for u1, u2, weight, j in edges:
                if (u1, u2) != (v1, v2) and uf.union(u1, u2):
                    curWeight += weight
            if curWeight == mstWeight:
                pseudo.append(i)
            
        return [critical, pseudo]












