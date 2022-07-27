# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(root):
            if not root:
                return None
            if not root.left and not root.right:
                return root
            
            left = dfs(root.left)
            right = dfs(root.right)
            if left:
                root.right, root.left = left, None
            # we need to find the last node of the left part
            while left and left.right:
                left = left.right
            
            if left:
                left.right = right 
            return root
        dfs(root)
        