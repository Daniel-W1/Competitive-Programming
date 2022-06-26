# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(root,parent,grandparent):
            if not root:
                return
            if grandparent:
                self.ans += root.val
            if parent:
                if root.val%2 == 0:
                    dfs(root.left,True,True)
                    dfs(root.right,True,True)
                else:
                    dfs(root.left,False,True)
                    dfs(root.right,False,True)
            elif root.val%2 == 0:
                dfs(root.left,True,False)
                dfs(root.right,True,False)
            else:
                dfs(root.left,False,False)
                dfs(root.right,False,False)
        dfs(root,False,False)
        return self.ans
                
            