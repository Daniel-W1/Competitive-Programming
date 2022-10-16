class Solution:
    def numTrees(self, n: int) -> int:
        '''
        we can choose any of the numbers from 1 - n
        update left, right
        
        n= [1, 2, 3]
                    1                   
                minelmnt smaller than 1
                0
                
        '''
        
        @cache
        def dfs(n):
            if n == 1 or n == 0:
                return 1
            
            res = 0
            for node in range(1, n+1):
                res += (dfs(node - 1) * dfs(n - node))
            
            return res
        
        return dfs(n)