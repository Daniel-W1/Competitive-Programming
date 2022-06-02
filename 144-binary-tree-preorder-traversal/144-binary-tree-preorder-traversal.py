# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # arr = []
        # def pre(root, arr):
        #     if root:
        #         arr.append(root.val)
        #         pre(root.left, arr)
        #         pre(root.right, arr)
        #     return arr
        # return pre(root, arr)
        stack = []
        ans = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ans
            