class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = [node for node in range(n)]
        self.removed = n
        
        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                # the cool comprehension
                node = parent[node]
            return node
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            
            if parent1 != parent2:
                self.removed -= 1
                parent[parent2] = parent1
        
        for idx, (r, c) in enumerate(stones):
            for j , (sr, sc) in enumerate(stones):
                if r == sr or c == sc:
                    union(idx, j)
        
        return n - self.removed