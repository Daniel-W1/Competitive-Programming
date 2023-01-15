class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [node for node in range(26)]
        
        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                # the cool comprehension
                node = parent[node]
            return node
        
        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            
            if parent1 == parent2:
                return [node1, node2]
            
            node1, node2 = parent1, parent2
            if node1 < node2:
                parent[node2] = node1
                
            elif node1 > node2:
                parent[node1] = node2
                
            return []
        
        for idx in range(len(s1)):
            if s1[idx] != s2[idx]:
                union(ord(s1[idx]) - 97, ord(s2[idx]) - 97)
        
        ans = []
        for char in baseStr:
            ans.append(chr(find(ord(char) - 97) + 97))
        
        return "".join(ans)
        
        