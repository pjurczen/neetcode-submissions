from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        preqMap: dict[int, set[int]] = defaultdict(set)
        for preq, course in prerequisites:
            preqMap[course].add(preq)

        visited: set[int] = set()

        def dfs(n: int):
            if n in visited:
                return
            
            visited.add(n)
            toAdd = set()
            for i in preqMap[n]:
                dfs(i)
                toAdd.update(preqMap[i])
            
            preqMap[n].update(toAdd)

        for n in range(numCourses):
            dfs(n)

        result: list[bool] = []

        for preq, course in queries:
            result.append(preq in preqMap[course])

        return result
