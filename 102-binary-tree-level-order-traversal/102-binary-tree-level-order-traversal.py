# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return []
        
        sol = []
        ans = []

        sol.append(root)        
        while len(sol) > 0:
            
            ans.append([])
            s = len(sol)            
            for i in range(s):
                curr = sol.pop(0)
                ans[len(ans)-1].append(curr.val)

                if curr.left:
                    sol.append(curr.left)

                if curr.right:
                    sol.append(curr.right)
                                        
        return ans