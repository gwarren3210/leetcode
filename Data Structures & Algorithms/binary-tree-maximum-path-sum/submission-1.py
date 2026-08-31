# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        out = [root.val]
        def dfs(node):
            if node == None: return 0
            left = dfs(node.left)
            right = dfs(node.right)

            out[0] = max(out[0], node.val + left + right)
            out[0] = max(out[0], node.val + right)
            out[0] = max(out[0], node.val + left)
            out[0] = max(out[0], node.val)
            return node.val + max(left, right, 0)
        dfs(root)
        return out[0]