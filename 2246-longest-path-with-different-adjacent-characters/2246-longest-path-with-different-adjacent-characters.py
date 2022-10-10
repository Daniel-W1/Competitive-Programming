class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        tree = defaultdict(list)
        for idx in range(1, len(parent)):
            p = parent[idx]
            tree[p].append(idx)
        
        self.ans = 0
        def dfs(root, parent):
            if root not in tree:
                return 1 if s[root] != s[parent] else 0
            
            res1, res2 = 0, 0
            for child in tree[root]:
                res = dfs(child, root) 
                if res > res1: 
                    res2, res1 = res1, res
                elif res > res2: res2 = res
            
            self.ans = max(self.ans, res1 + res2 + 1)
            return max(res1, res2)+1 if s[root] != s[parent] else 0
        
        dfs(0, -1)
        return max(self.ans, 1)