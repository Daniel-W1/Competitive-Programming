# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        path = []
        def dfs(root):
            if not root:
                return
            
            if root and not root.left and not root.right:
                path.append(root.val)
                ans.append("->".join(str(val) for val in path))
                path.pop()
                return
            
            path.append(root.val)
            dfs(root.left)
            dfs(root.right)
            path.pop()
        
        dfs(root)
        
        return ans