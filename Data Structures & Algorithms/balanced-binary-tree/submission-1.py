# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None), TypeVarTuple:
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
 
        def inorder(root: Optional[TreeNode]) -> tuple[int, bool]:
            result = True
            if not root:
                return 0, result

            left, result_l = inorder(root.left)
            right, result_r = inorder(root.right)
            if not result_l or not result_r or abs(left - right) > 1:
                result = False
            
            r = max(left, right) + 1

            return r, result
        _, result = inorder(root)

        return result