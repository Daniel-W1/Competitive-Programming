# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1: 
            new_root = TreeNode(val)
            new_root.left = root
            
            return new_root
        
        q = deque([root])
        cur_depth = 2
        
        while q and cur_depth < depth:
            level = []
            for _ in range(len(q)):
                cur = q.popleft()
                
                if cur.left:
                    level.append(cur.left)
                
                if cur.right:
                    level.append(cur.right)
            
            q += level
            cur_depth += 1
        
        for node in q:
            left = node.left
            right = node.right
            
            node.left = TreeNode(val)
            node.right = TreeNode(val)
            
            node.left.left = left
            node.right.right = right
        
        return root
                
            