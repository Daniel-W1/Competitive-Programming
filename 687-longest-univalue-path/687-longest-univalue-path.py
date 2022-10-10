# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        self.ans = 0
        def dfs(root, prev):
            if not root:
                return 0
            
            if root and not root.left and not root.right:
                return int(root.val == prev)
            
            
            left = dfs(root.left, root.val)
            right = dfs(root.right, root.val)
        
            # print(left, right, root.val)
            self.ans = max(self.ans, left + right)
            
            return max(left, right)+1 if root.val == prev else 0
        dfs(root, -1)
        return self.ans
        
            
            
                
                