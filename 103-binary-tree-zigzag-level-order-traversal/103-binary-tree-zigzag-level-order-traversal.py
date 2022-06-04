# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return root
        q = []
        q.append(root)
        ans = []
        change = False
        while q:
            level = []
            s = len(q)
            for _ in range(s):
                node = q.pop(0)
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if change:
                ans.append(level[::-1])
            else:
                ans.append(level)
            change = not change
        return ans