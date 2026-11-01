# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def helper(node: Optional[TreeNode]):
            if not node:
                return
            
            tmp = node.right
            node.right = node.left
            node.left = tmp
            helper(node.left)
            helper(node.right)
        
        helper(root)

        return root