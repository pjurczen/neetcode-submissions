# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        pre_iter = iter(preorder)

        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            root_val = next(pre_iter)
            i = inorder_map[root_val]
            
            root = TreeNode(val=root_val)
            root.left = helper(left, i - 1)
            root.right = helper(i + 1, right)
            return root

        return helper(0, len(inorder) - 1)