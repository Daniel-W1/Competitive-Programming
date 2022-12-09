"""

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # print(node, not node)
        if not node: return None
        
        if not node.neighbors:
            return Node(node.val)
        
        old_new = {}
        # print(node.val)
        visited = set()
        def dfs(node):
            if node in visited: return
            if node.val not in old_new:
                old_new[node.val] = Node(node.val)
        
            visited.add(node)
            
            for other in node.neighbors:
                if other in visited: continue
                if other.val not in old_new:
                    old_new[other.val] = Node(other.val)
                
                old_new[other.val].neighbors.append(old_new[node.val])
                old_new[node.val].neighbors.append(old_new[other.val])
            for other in node.neighbors:

                dfs(other)
        
        dfs(node)
        
        return old_new[node.val]            