# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root,res):
            if root and not root.left and not root.right:
                res += str(root.val)
                self.ans += int(res)
                return
            if not root:
                return 
            dfs(root.left,res+str(root.val))
            dfs(root.right,res+str(root.val))
        dfs(root,"")
        return self.ans