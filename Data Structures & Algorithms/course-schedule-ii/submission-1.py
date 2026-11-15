from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj: dict[int, list[int]] = defaultdict(list)

        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        topSort = []
        visited = set()
        path = set()

        for n in range(numCourses):
            if not self.dfs(n, visited, path, adj, topSort):
                return []
        
        return topSort


    def dfs(self, n: int, visited: set[int], path: set[int], adj: dict[int, list[int]], topSort: list[int]) -> bool:
        if n in path:
            return False
        if n in visited:
            return True
        
        visited.add(n)
        path.add(n)
        
        for c in adj[n]:
            if not self.dfs(c, visited, path, adj, topSort):
                return False
        
        topSort.append(n)
        path.remove(n)
        return True
