# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countleftsubtree(self, node):
        if not node:
            return 0
        return 1 + self.countleftsubtree(node.left)
    
    def countrightsubtree(self, node):
        if not node:
            return 0
        
        return 1 + self.countrightsubtree(node.right)
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        left, right = self.countleftsubtree(root.left), self.countrightsubtree(root.right)
        
        if left > right:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
        else:
            return 2 ** (left + 1) - 1
        
        
        