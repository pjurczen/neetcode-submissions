from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList: dict[int, list[int]] = {}

        for n in prerequisites:
            node: int = n[0]
            child: int = n[1]
            if node not in adjList:
                adjList[node] = []
            if child not in adjList:
                adjList[child] = []
            adjList[node].append(child)


        def dfs(node: int, visited: set) -> bool:
            if node in finishable:
                return True
            if node in visited:
                return False
            
            visited.add(node)
            for n in adjList[node]:
                if not dfs(n, visited):
                    return False
            visited.remove(node)
            return True

        finishable = set()

        for c in adjList.keys():
            result = dfs(c, set())
            if result:
                finishable.add(c)
            else:
                return False

        return True