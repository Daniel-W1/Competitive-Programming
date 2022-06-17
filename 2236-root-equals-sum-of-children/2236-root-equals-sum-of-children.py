# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root and not root.left and not root.right:
                return root.val
            left = dfs(root.left) if root.left else 0
            right = dfs(root.right) if root.right else 0
            
            if left is None or right is None:
                return None
            if root.val == left+right:
                return root.val+left+right
            return None
        return True if dfs(root) is not None else False