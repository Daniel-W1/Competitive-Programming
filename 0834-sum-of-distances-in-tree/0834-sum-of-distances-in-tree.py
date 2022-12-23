class Solution:
    def dfs1(self, node, parent):
        res = 0
        
        for child in self.tree[node]:
            if child != parent:
                res += self.dfs1(child, node)
                self.dp[node] += self.dp[child]

        if res:
            self.dp[node] += (res)
        
        self.childcnt[node] = res + 1
        return res + 1
    
    def dfs2(self, node, parent):
        if parent != -1:
            subnode = self.childcnt[node]
            left = self.n - subnode
            
            self.dp[node] = (self.dp[parent] + self.n - 2 * subnode)
        
        for child in self.tree[node]:
            if child != parent:
                self.dfs2(child, node)
            
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        self.n = n
        self.tree = defaultdict(list)
        self.childcnt = defaultdict(int)
        
        for n1, n2 in edges:
            self.tree[n1].append(n2)
            self.tree[n2].append(n1)
             
        self.dp = [0] * n
        self.dfs1(0, -1)
        self.dfs2(0, -1)
        
        
        return self.dp