# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        
        def dfs(root):
            if not root: return None
            if not root.left and not root.right:
                # print(root.val)
                return root if root == p or root == q else None
            
            left = dfs(root.left)
            right = dfs(root.right)
            # print(left, right)
            if left and right:
                self.ans = root
                return None
            if not left and not right and (root == p or root == q):
                return root 
            
            if not left and not right:
                return None
            if left:
                if root == p or root == q:
                    self.ans = root
                    return None
                else: return left
            if right:
                if root == p or root == q:
                    self.ans = root
                    return None
                else: return right
            
        dfs(root)
        return self.ans