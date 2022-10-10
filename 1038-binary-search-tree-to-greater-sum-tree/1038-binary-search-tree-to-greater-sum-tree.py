# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.ans = 0
        def inorder(root):
            if root:
                inorder(root.right)
                self.ans += root.val
                root.val = self.ans
                inorder(root.left)
        
        inorder(root)
        return root