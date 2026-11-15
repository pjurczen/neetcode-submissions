from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj: dict[int, list[int]] = defaultdict(list)

        for course, prereq in prerequisites:
            adj[course].append(prereq)
        
        visited = set()
        path = set()

        for n in range(numCourses):
            if not self.dfs(n, visited, path, adj):
                return False
        
        return True


    def dfs(self, n: int, visited: set[int], path: set[int], adj: dict[int, list[int]]) -> bool:
        if n in path:
            return False
        if n in visited:
            return True
        
        visited.add(n)
        path.add(n)
        for c in adj[n]:
            if not self.dfs(c, visited, path, adj):
                return False

        path.remove(n)
        return True
