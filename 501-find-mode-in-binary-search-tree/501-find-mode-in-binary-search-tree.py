# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = {}
        def dfs(root):
            if not root:
                return
            counter[root.val] = counter.get(root.val,0)+1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        counted = sorted([(k,v) for k,v in counter.items()],key = lambda val:val[1],reverse = True)
        top = counted[0][1]
        i = 0
        ans = []
        while i < len(counted) and counted[i][1] == top:
            ans.append(counted[i][0])
            i += 1
        return ans