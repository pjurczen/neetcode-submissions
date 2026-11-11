class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList: dict[int, list[int]] = defaultdict(list)

        for preq in prerequisites:
            first = preq[1]
            after = preq[0]
            adjList[after].append(first)
        
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
            finishable.add(course)

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
