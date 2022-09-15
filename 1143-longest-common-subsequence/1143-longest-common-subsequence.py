class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        @cache
        def find(pointer1, pointer2):
            if pointer1 == -1 or pointer2 == -1: return 0
            
            elif text1[pointer1] == text2[pointer2]:
                return 1 + find(pointer1-1, pointer2-1)
            else:
                return max(find(pointer1-1, pointer2), find(pointer1, pointer2-1))
            
        return find(len(text1)-1, len(text2)-1)
        '''
        # now let's try to solve it using bottom up appraoch or tabulation
        # we will also use the shifting of index idea to set our basecases
        
        # that means -1 becomes 0 and last index becomes n
        '''
        n, m = len(text1), len(text2)
        dp = [[-1]*(n+1) for _ in range(m+1)]
        
        # the base case is when ever we are dealing with an empty string the ans
        # is going to be 0
        
        for col in range(n+1):
            dp[0][col] = 0
        for row in range(m+1):
            dp[row][0] = 0
        
        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                if text2[row-1] == text1[col-1]:
                    dp[row][col] = 1 + dp[row-1][col-1]
                else:
                    dp[row][col] = max(dp[row-1][col], dp[row][col-1])
         # just like the recursive code
        return dp[-1][-1]
        
        '''
        # now how can we optimise the space for the bottom up code that should be
        # pretty easy
        # as we can see from the dp, we only need the previous row
        n, m = len(text1), len(text2)
        prev = [0]*(n+1)
        cur = [0]*(n+1)
        
        for row in range(1, m+1):
            for col in range(1, n+1):
                if text2[row-1] == text1[col-1]:
                    cur[col] = 1 + prev[col-1]
                else:
                    cur[col] = max(prev[col], cur[col-1])
            prev, cur = cur,prev 
            
        return prev[-1]