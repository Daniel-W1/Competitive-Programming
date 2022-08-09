"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(root):
            if not root:
                return 0
            answer = 1
            for kid in root.children:
                answer = max(answer, dfs(kid)+1)
            return answer
        
        return dfs(root)