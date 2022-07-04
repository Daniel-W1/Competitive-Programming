# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        def max_depth(node):
            if not node:
                return 0
            left = max_depth(node.left) + 1
            right = max_depth(node.right) + 1
            self.max = max(self.max, left+right-2)
            
            return max(left,right)
        max_depth(root)
        return self.max