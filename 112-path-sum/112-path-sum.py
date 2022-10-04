# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, cur):
            if not root:
                return False
            
            if root and not root.left and not root.right:
                return cur + root.val == targetSum
            
            left = dfs(root.left, cur + root.val)
            right = dfs(root.right, cur + root.val)
            
            return left or right
    
        return dfs(root, 0)
            
            