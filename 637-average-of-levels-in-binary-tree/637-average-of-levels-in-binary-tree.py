# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = []
        q.append(root)
        ans = []
        while q:
            level_sum = 0
            width = len(q)
            for _ in range(width):
                node = q.pop(0)
                level_sum += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level_sum/width)
        return ans
            