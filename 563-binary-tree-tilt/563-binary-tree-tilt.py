# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)+root.val
            right = dfs(root.right)+root.val
            self.total += (abs(left-right))
            return left+right-root.val
        dfs(root)
        return self.total
           
                