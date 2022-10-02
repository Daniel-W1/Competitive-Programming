class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        '''
        so we are rolling the dice n times and it has k numbers in it
        
        1,2,3,4,5,6
        target = 3
        n = 1
        
        i think i need to keep track of my target and also the number of times i am going
        
        
        i have two states n, and k 
        each time n > 0
        
        am gonna loop through all possible ks and choose one and do dfs
        and when n == 0 and my target becomes 0 then that means i can return 
        1 else 0
    
        
        k * n
        space comp is also k*n
        
        '''
        @cache
        def dfs(n, target):
            if n == 0:
                return int(target == 0)
            
            res = 0
            for num in range(1, k+1):
                res += dfs(n-1, target - num)
            
            return res
        return (dfs(n, target)) % (10**9 + 7)