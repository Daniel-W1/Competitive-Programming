# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depths = []
        def findmaxdep(root,cnt):
            if not root:
                if not depths:
                    depths.append(cnt)
                else:
                    if cnt > depths[-1]:
                        depths.append(cnt)
                return
            findmaxdep(root.left,cnt+1)
            findmaxdep(root.right,cnt+1)
        findmaxdep(root,0)
        return depths[-1]
            