"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depths = []
        if not root:
            return 0
        def findmax(root,cnt):
            childs = root.children
            if not childs:
                if not depths:
                    depths.append(cnt+1)
                elif cnt+1 > depths[-1]:
                    depths.append(cnt+1)
            for child in childs:
                findmax(child,cnt+1)
        findmax(root,0)
        return depths[-1]
        
        
            
        