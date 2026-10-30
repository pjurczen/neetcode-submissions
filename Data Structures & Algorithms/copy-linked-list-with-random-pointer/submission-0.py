"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies: dict[Node, Node] = {}

        def getOrCopy(node: Optional[Node]) -> Optional[Node]:
            if node is None:
                return None
            if node in copies:
                return copies[node]
            else:
                copy = Node(x=node.val)
                copies[node] = copy
                return copy

        cur = head
        curCopy = None
        while cur:
            curCopy = getOrCopy(cur)
            curCopy.next = getOrCopy(cur.next)
            curCopy.random = getOrCopy(cur.random)
            cur = cur.next
        
        return getOrCopy(head)
