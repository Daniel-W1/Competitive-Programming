# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,left,right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            
            l = dfs(node.left,left,min(node.val,right))
            r = dfs(node.right,max(left,node.val),right)
            
            return l and r
        return dfs(root,-float('inf'),float('inf'))