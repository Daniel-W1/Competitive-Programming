# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        turn_map = defaultdict(list)
        def dfs(node):
            if not node:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            real_turn = max(left, right) + 1
            turn_map[real_turn].append(node.val)
            
            return real_turn
        
        dfs(root)
        
        return list(turn_map.values())
            
            
            