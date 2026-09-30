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
        hashmap = {}
        if not node:
            return None
        
        def dfs(node: Node) -> Node:
            if node in hashmap:
                return hashmap[node]

            clone = Node(val=node.val)
            hashmap[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))

            return clone
        
        return dfs(node)