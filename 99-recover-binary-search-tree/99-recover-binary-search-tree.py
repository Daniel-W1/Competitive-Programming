# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # so the approach here is to find the faulty node and stop the
        # dfs and store that node
        # when we are done with the whole thing and we still have one node
        # that means the root node should be changed.
        # stop and think is it possible to find two faulty nodes on one
        # path because that case this approach won't work
        srt = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            srt.append(root)
            inorder(root.right)
            
        inorder(root)
        correct = sorted(node.val for node in srt)
        for i in range(len(correct)):
            srt[i].val = correct[i]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            