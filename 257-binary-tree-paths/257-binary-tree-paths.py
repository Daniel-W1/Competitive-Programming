# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.output = []
        def preorder(root,res):
            if root and not root.left and not root.right:
                res += str(root.val) 
                self.output.append(res)
            elif root:
                res += str(root.val) + "->"
                preorder(root.left, res)
                preorder(root.right, res)
        preorder(root,"")
        return self.output
        