# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque([root])
        while q:
            cur_size = len(q)
            level = []
            for _ in range(cur_size):
                node = q.popleft()
                if node:
                    level.append(node.val)
                else:
                    level.append(None)
                if node:
                    q.append(node.left)
                if node:
                    q.append(node.right)

            if level != level[::-1]:
                return False
        return True