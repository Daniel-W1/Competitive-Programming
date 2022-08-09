# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, cursum):
            if not root:
                return False
            if root and not root.left and not root.right:
                return cursum + root.val == targetSum
            return dfs(root.left, cursum + root.val) or dfs(root.right, cursum+root.val)
        return dfs(root, 0)
    # time comp