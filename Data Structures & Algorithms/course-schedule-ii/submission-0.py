from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList: dict[int, list[int]] = defaultdict(list)

        for preq in prerequisites:
            first = preq[1]
            after = preq[0]
            adjList[after].append(first)
        
        order = []
        finishable = set()
        visited = set()

        def dfs(course: int) -> bool:
            if course in visited:
                return False

            if course in finishable:
                return True
            
            visited.add(course)

            for preq in adjList[course]:
                if not dfs(preq):
                    return False
            
            visited.remove(course)
            if course not in finishable:
                finishable.add(course)
                order.append(course)
            
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        
        return order