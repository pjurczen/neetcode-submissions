from collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList: dict[int, list[int]] = defaultdict(list)
        for preq, course in prerequisites:
            adjList[course].append(preq)

        preqMap: dict[int, set[int]] = {}

        visited: set[int] = set()

        def dfs(n: int):
            if n not in preqMap:
                preqMap[n] = set(adjList[n])
                for i in adjList[n]:
                    preqMap[n] |= dfs(i)
            return preqMap[n]

        for n in range(numCourses):
            dfs(n)

        result: list[bool] = []

        for preq, course in queries:
            result.append(preq in preqMap[course])

        return result
