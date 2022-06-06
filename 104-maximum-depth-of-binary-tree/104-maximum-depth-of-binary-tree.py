# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        def findmaxdep(root,cnt):
            if not root:
                self.depth = max(self.depth, cnt)
                return
            findmaxdep(root.left,cnt+1)
            findmaxdep(root.right,cnt+1)
        findmaxdep(root,0)
        return self.depth
            