class UnionFind:

    def __init__(self, nums: list[int]) -> None:
        self.parent = {}
        self.rank = {}
        self.count = {}
        for n in nums:
            self.parent[n] = n
            self.rank[n] = 1
            self.count[n] = 1
        self.topCount = 1

    def find(self, n: int) -> Optional[int]:
        parent = self.parent.get(n, None)
        if parent is None:
            return None
        while parent != self.parent[parent]:
            self.parent[n] = self.parent[self.parent[n]]
            parent = self.parent[n]
        return parent

    def union(self, n1: int, n2: int) -> bool:
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == None or p2 == None or p1 == p2:
            return False
        else:
            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
                self.count[p1] += self.count[p2]
                self.topCount = max(self.topCount, self.count[p1])
            elif self.rank[p2] > self.rank[p1]:
                self.parent[p1] = p2
                self.count[p2] += self.count[p1]
                self.topCount = max(self.topCount, self.count[p2])
            else:
                self.parent[p2] = p1
                self.rank[p1] += 1
                self.count[p1] += self.count[p2]
                self.topCount = max(self.topCount, self.count[p1])
            return True

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind(nums)
        for n in nums:
            uf.union(n, n+1)
            uf.union(n, n-1)
        return uf.topCount if nums else 0


