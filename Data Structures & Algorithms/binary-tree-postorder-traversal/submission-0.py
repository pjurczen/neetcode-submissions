# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visit = []
        stack = []
        result = []
        if root:
            visit.append(False)
            stack.append(root)

        while stack:
            cur, visited = stack.pop(), visit.pop()
            if visited:
                result.append(cur.val)
            else:
                stack.append(cur)
                visit.append(True)
                if cur.right:
                    stack.append(cur.right)
                    visit.append(False)
                if cur.left:
                    stack.append(cur.left)
                    visit.append(False)
        return result
