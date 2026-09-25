# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        parent = None
        location: int = 0 # -1=left, +1=right

        while curr:
            parent = curr
            if val < curr.val:
                location = -1
                curr = curr.left
            elif val > curr.val:
                location = 1
                curr = curr.right
        
        if location > 0:
            parent.right = TreeNode(val)
        elif location < 0:
            parent.left = TreeNode(val)
        else:
            root = TreeNode(val)
        
        return root


