# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # what are the deepest leaves
        # what is the parent of them
        # so the approach am trying to implement is 
        # for each leaf node i return depth + 1
        # for each None node i return depth
        
        # for 2 left = 3, right = 3, store (3, 3, node)
        # for 5 left = 2, right = 3
        # for 1 left = 2, right = 2
        # for 3 left = 3, right = 2
        
        # first time i get a node i make my answer that, (3,3,2)
        # second time i compare if it's equal i make it the answer 
        self.ans = None
        def dfs(root, depth):
            if not root:
                return depth
            if root and not root.left and not root.right:
                if not self.ans:
                    self.ans = (depth+1, depth+1, root)
                else:
                    prev_left, prev_right, prev_node = self.ans
                    if depth+1 >= prev_left and depth+1 >= prev_right:
                        self.ans = (depth+1, depth+1, root)
                return depth + 1
            
            left = dfs(root.left, depth+1) 
            right = dfs(root.right, depth+1) 
             
            if not self.ans:
                self.ans = (left, right, root)
            else:
                prev_left, prev_right, prev_node = self.ans
                if left >= prev_left and right >= prev_right:
                    self.ans = (left, right, root)
            
            return max(left, right)
        dfs(root,0)
        return self.ans[2]
                
            