from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = set()
        queue = deque()
        adjList = {}
        if not node:
            return None
        queue.append(node)
        while queue:
            cur = queue.popleft()
            if cur.val not in adjList:
                adjList[cur.val] = []
            if cur in visited:
                continue
            for n in cur.neighbors:
                adjList[cur.val].append(n.val)
                queue.append(n)
            visited.add(cur)
        
        hashmap = {} # val: node
        for k, v in adjList.items():
            if k not in hashmap:
                hashmap[k] = Node(val=k)
            for n in v:
                if n not in hashmap:
                    hashmap[n] = Node(n)
                hashmap[k].neighbors.append(hashmap[n])
        
        return hashmap[node.val]