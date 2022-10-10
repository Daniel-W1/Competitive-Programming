# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = {0:1}
        self.ans = 0
        cur = 0
        
        def dfs(root):
            nonlocal cur 
            
            if not root:
                return 
            
            cur += root.val
            
            self.ans += prefix.get(cur - targetSum, 0)
            
            prefix[cur] = prefix.get(cur, 0) + 1
            
            dfs(root.left)    
            dfs(root.right)
                
            prefix[cur] -= 1
            cur -= root.val 

        dfs(root)

        return self.ans
            