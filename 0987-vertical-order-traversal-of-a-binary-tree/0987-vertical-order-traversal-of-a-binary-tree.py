# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        node_map = []
        
        def dfs(node, row, col):
            if not node:
                return
            
            node_map.append((col, row, node.val))

            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        
        dfs(root, 0, 0)
        node_map.sort()
        
        # print(node_map)
        cur_col = node_map[0][0]
        ans = [[]]
        
        for col, row, val in node_map:
            if col == cur_col:
                ans[-1].append(val)
            else:
                ans.append([val])
                cur_col = col
        
        return ans
        
        
        
            