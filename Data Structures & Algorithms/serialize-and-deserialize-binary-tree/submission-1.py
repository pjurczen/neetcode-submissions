# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        values: list[str] = []
        queue = deque()
        if root:
            queue.append((root, 1))
        while queue:
            node, i = queue.popleft()
            values.append(f"{i}:{node.val}")
            if node.left:
                queue.append((node.left, 2 * i))
            if node.right:
                queue.append((node.right, 2 * i + 1))
        print(values)
        return str(",".join(values))

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values: list[str] = data.split(",")
        if not values or values[0] == "":
            return None
        hashmap: dict[int, int] = {}  # dict[index, value]
        for val in values:
            elems: list[str] = val.split(":")
            hashmap[int(elems[0])] = int(elems[1])

        queue = deque()
        root = TreeNode(val=hashmap[1])
        queue.append((root, 1))
        while queue:
            node, i = queue.popleft()
            if 2 * i in hashmap:
                left = TreeNode(val=int(hashmap[2 * i]))
                node.left = left
                queue.append((left, 2 * i))
            if 2 * i + 1 in hashmap:
                right = TreeNode(val=int(hashmap[2 * i + 1]))
                node.right = right
                queue.append((right, 2 * i + 1))
        return root
