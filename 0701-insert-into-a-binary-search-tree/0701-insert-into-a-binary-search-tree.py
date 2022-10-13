# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        self.done = False

        def insert(node, parent):
            if not node:
                return
            
            if val > node.val:
                insert(node.right, node)
            else:
                insert(node.left, node)

            if node.val > val and not self.done:
                new = TreeNode(val)
                if not parent:
                    node.left = new
                elif val > parent.val:
                    parent.right = new
                    new.right = node
                else:
                    parent.left = new
                    new.right = node
            elif not self.done:
                new = TreeNode(val)
                node.right = new
            self.done = True

            
        insert(root, None)
        return root
                
                    
    
        