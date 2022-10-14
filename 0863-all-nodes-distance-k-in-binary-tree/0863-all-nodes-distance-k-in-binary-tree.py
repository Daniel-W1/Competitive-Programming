# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # first let's make the graph
        parents = {}
        def dfs(node, parent):
            if not node:
                return
            
            parents[node.val] = parent
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)
        
        # now do bfs
        q = deque([(target)])
        steps = 0
        ans = []
        seen = set()
        
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if steps == k:
                    ans.append(node.val)
                
                seen.add(node)
                
                if parents[node.val] and parents[node.val] not in seen:
                    q.append(parents[node.val])
                
                if node.left and node.left not in seen:
                    q.append(node.left)
                
                if node.right and node.right not in seen:
                    q.append(node.right)
            steps += 1
            if steps > k:
                break
            
        return ans
        
            