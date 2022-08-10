# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        answer = 0
        def dfs(root, parent, gparent):
            nonlocal answer
            
            if not root:
                return 
            if gparent and gparent.val % 2 == 0:
                answer += root.val
            
            dfs(root.left, root, parent)
            dfs(root.right, root, parent)
        
        dfs(root, None, None)
        return answer
                