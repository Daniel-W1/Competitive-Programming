# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(node, path_sum):
            if not node:
                return
            
            path_sum *= 10
            path_sum += node.val
            
            if node and not node.left and not node.right:
                self.ans += path_sum
                return
            
            dfs(node.left, path_sum)
            dfs(node.right, path_sum)
        
        dfs(root, 0)
        
        return self.ans