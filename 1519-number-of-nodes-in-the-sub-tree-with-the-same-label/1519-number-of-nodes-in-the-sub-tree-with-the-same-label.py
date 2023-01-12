class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        tree = defaultdict(list)
        
        for n1, n2 in edges:
            tree[n1].append(n2)
            tree[n2].append(n1)
            
        answer = [-1] * n
        
        def dfs(node, parent):
            
            res = [0]*26
            
            for neig in tree[node]:
                if neig != parent:
                    kid_res = dfs(neig, node)
                    
                    res = [res[i] + kid_res[i] for i in range(26)]
            
            res[ord(labels[node]) - 97] += 1
            answer[node] = res[ord(labels[node]) - 97]
            
            return res
        
        dfs(0, -1)
        return answer
        
        