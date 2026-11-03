# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node: Optional[TreeNode], minValue: Optional[int], maxValue: Optional[int]) -> bool:
            if node is None:
                return True
            if (minValue is not None and node.val <= minValue) or (maxValue is not None and node.val >= maxValue):
                return False
            
            if not dfs(node.left, minValue, node.val):
                return False
            
            return dfs(node.right, node.val, maxValue)

        return dfs(root, None, None)