# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # we just need to do a level order traversal 
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        q = [root]
        dep = 2
        while q:
            width = len(q)
            for _ in range(width):
                node = q.pop(0)
                if dep == depth:
                    current_left = node.left
                    current_right = node.right
                    node.right,node.left = TreeNode(val), TreeNode(val)
                    node.right.right,node.left.left = current_right,current_left
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if dep == depth:
                return root
            dep += 1
        