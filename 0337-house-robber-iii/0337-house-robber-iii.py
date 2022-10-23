# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        
        def dfs(node):
            if not node:
                return (0, 0)
            
            # if not node.left and not node.right:
            #     return (node.val, 0)
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            child_ans = max(node.val + left[1] + right[1], left[0] + right[0])
            return (child_ans, left[0] + right[0])
        
        res = dfs(root)
        return max(res)
        
        
            
            
            
            