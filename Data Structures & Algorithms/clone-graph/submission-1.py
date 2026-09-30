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
        hashmap = {}
        if not node:
            return None
        queue.append(node)
        while queue:
            cur = queue.popleft()
            if cur in visited:
                continue
            for n in cur.neighbors:
                queue.append(n)
            hashmap[cur] = Node(val=cur.val)
            visited.add(cur)
        
        for k, v in hashmap.items():
            for n in k.neighbors:
                new_n = hashmap[n]
                v.neighbors.append(new_n)
        
        return hashmap[node]