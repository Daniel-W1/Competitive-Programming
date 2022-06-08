# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        changed_nums = [(val, i) for i,val in enumerate(nums)]
        def build(changed_nums, l, h):
            if l < h:
                the_max = max(changed_nums[l:h])
                root = TreeNode(the_max[0])
                root.left = build(changed_nums, l, the_max[1])
                root.right = build(changed_nums,the_max[1]+1,h)
                return root
        return build(changed_nums,0,len(changed_nums))
        
            
        
        