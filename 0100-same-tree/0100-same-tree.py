# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            
            if root1 and root2 and root1.val == root2.val:
                left = dfs(root1.left, root2.left)
                right = dfs(root1.right, root2.right)
                
                return left and right
            else:
                return False
        
        return dfs(p, q)
            