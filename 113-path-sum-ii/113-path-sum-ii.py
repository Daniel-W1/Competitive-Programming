# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def traverse(root, res):
            ans = []
            if root and not root.left and not root.right:
                res += root.val
                if res == targetSum:
                    return [[root.val]]
                else:
                    return False
            elif root:
                path1 = traverse(root.left, res+root.val)
                path2 = traverse(root.right, res + root.val)
                if path1:
                    for arr in path1:
                        arr.append(root.val)
                        ans.append(arr)
                if path2:
                    for arr in path2:
                        arr.append(root.val)
                        ans.append(arr)
            return ans
        result = traverse(root,0) 
        return [arr[::-1] for arr in result] if result else []
                
                