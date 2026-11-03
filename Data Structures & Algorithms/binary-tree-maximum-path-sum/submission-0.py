# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maxSum = float("-inf")

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal maxSum
            if not node:
                return 0

            left = dfs(node.left)
            left = max(0, left)
            right = dfs(node.right)
            right = max(0, right)

            maxSum = max(maxSum, node.val + left + right)

            return node.val + max(left, right)

        dfs(root)

        return int(maxSum)
