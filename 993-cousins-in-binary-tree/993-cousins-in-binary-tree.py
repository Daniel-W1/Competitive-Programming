# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # the final result of the dfs is going to be (depth, parent)
        # x: (2, 2) y:(1, 1)
        
        # time comp O(n)
        # space comp O(n)
        
        xans, yans = None, None
        def preorder(root, parent, depth):
            nonlocal xans, yans
            if not root:
                return
            
            if xans and yans:
                return
            
            if root.val == x:
                xans = (depth, parent)
            if root.val == y:
                yans = (depth, parent)
            
            preorder(root.left, root, depth+1)
            preorder(root.right, root, depth+1)
        
        preorder(root, None, 0)
        return True if xans[0] == yans[0] and xans[1] != yans[1] else False
                
            
            
            