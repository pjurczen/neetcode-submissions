# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def helper(node: Optional[TreeNode], maxValue: int) -> int:
            if node is None:
                return 0

            result = 0
            if node.val >= maxValue:
                result += 1
            
            result += helper(node.left, max(maxValue, node.val))
            result += helper(node.right, max(maxValue, node.val))

            return result

        return helper(root, root.val)