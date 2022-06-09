# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def checkbalance(root):
            if not root:
                return 0
            left = checkbalance(root.left)
            right = checkbalance(root.right)
            if left < 0 or right < 0:
                return -1
            if abs(left-right) < 2:
                return max(left,right)+1
            else:
                return -1
        return checkbalance(root) != -1