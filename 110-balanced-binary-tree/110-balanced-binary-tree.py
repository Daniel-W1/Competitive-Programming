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
            left = checkbalance(root.left)+1 if checkbalance(root.left) != None else -float('inf')
            right = checkbalance(root.right)+1 if checkbalance(root.right) != None else float('inf')
            
            if abs(left-right) < 2:
                return max(left,right)
            else:
                return None
        return checkbalance(root)