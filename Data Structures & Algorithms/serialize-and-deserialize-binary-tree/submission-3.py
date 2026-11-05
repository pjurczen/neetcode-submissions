# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        values: list[str] = []

        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                values.append("N")
                return
            values.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        return ",".join(values)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values: list[str] = data.split(",")

        i: int = 0
        def dfs() -> Optional[TreeNode]:
            nonlocal i
            if values[i] == "N":
                i += 1
                return None
            node = TreeNode(val=int(values[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()
