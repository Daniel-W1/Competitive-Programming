# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []
        def pre(root, arr):
            if root:
                arr.append(root.val)
                pre(root.left, arr)
                pre(root.right, arr)
            return arr
        ans = pre(root,arr)
        for val in ans[1:]:
            root.right = TreeNode(val)
            root.left = None
            root = root.right
        return root
        