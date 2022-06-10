# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root):
            if not root:
                return 
            if root and root.left:
                left_leaf = root.left
                if not left_leaf.left and not left_leaf.right:
                    self.ans += left_leaf.val
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.ans
                    
                
                    