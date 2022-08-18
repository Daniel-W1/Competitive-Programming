# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        q = collections.deque([root])
        answer = []
        reverse = False
        while q:
            level = []
            current_size = len(q)
            for _ in range(current_size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if reverse:
                answer.append(level[::-1])
            else:
                answer.append(level)
            reverse = not reverse
        return answer