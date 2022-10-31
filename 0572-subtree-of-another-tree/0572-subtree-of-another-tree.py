# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sametree(root1, root2):
            if not root1 and not root2:
                return True
            
            if root1 and root2 and root1.val == root2.val:
                left = sametree(root1.left, root2.left)
                right = sametree(root1.right, root2.right)
                
                return left and right
            else:
                return False
        
        self.ans = False
        def dfs(root):
            if not root:
                return
            
            if root.val == subRoot.val:
                check = sametree(subRoot, root)
                if check:
                    self.ans = True
            
            if not self.ans:
                dfs(root.left)
                dfs(root.right)
            
        dfs(root)
        return self.ans