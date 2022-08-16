# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        3
    1       4
3          1    5
        preorder traversal is good 
        i have to visit the root node before i get to that node, 
        
        '''
        seenMax = root.val
        def dfs(root, curMax):
            if root == None:
                return 0
            
            curMax = max(curMax, root.val)
            left = dfs(root.left, curMax)
            right = dfs(root.right, curMax)
            
            if root.val >= curMax:
                return left + right + 1
            else:
                return left + right
        return dfs(root, seenMax)
            