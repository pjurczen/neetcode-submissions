# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        cur = root
        while cur or stack:
            if not cur:
                cur = stack.pop()
            result.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            cur = cur.left

        return result