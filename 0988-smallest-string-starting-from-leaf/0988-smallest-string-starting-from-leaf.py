# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        """
            256
            2421
        """
        
        def dfs(node, prev_path):
            if not node:
                return "{"
            
            if node and not node.left and not node.right:
                return chr(97 + node.val)
            
            prev_path += chr(97 + node.val) 
            
            left = dfs(node.left, prev_path)
            right = dfs(node.right, prev_path)
            
            prev_l, prev_r = left[:], right[:]
            
            idx = 0
            while len(left) < len(right) and idx < len(prev_path):
                left += prev_path[-idx-1]
                idx += 1
            
            while len(left) > len(right) and idx < len(prev_path):
                right += prev_path[-idx-1]
                idx += 1
            
            # print(left, right, chr(97 + node.val) )
            if left == right:
                return min(prev_l, prev_r) + chr(97 + node.val)
            
            return (prev_l if left < right else prev_r) + chr(97 + node.val) 
        
        return dfs(root, "")