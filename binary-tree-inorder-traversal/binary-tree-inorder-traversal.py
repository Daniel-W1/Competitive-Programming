# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        def inorder(root, arr):
            if root:
                inorder(root.left, arr)
                output.append(root.val)
                inorder(root.right, arr)
            return output
        return inorder(root, output)
        
        
        
            