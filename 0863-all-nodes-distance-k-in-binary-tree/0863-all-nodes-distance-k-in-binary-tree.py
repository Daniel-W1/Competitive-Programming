# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}
        def dfs(node, parent):
            if not node:
                return

            parents[node] = parent
            dfs(node.left, node)
            dfs(node.right, node)

        def findallnodes_k_distance(root, target, k):
            dfs(root, None)
            queue = deque([target])
            steps = 0
            answer = []
            visited = set()
            visited.add(target)

            while queue:
                size = len(queue)
                for _ in range(size):
                    cur = queue.popleft()

                    if steps == k:
                        answer.append(cur.val)
                        continue

                    if cur.left and cur.left not in visited:
                        queue.append(cur.left)
                        visited.add(cur.left)
                        
                    if cur.right and cur.right not in visited:
                        queue.append(cur.right)
                        visited.add(cur.right)
                        
                    if parents[cur] and parents[cur] not in visited:
                        queue.append(parents[cur])
                        visited.add(parents[cur])
                steps += 1

            return answer
        return findallnodes_k_distance(root, target, k)