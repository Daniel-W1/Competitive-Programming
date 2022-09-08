class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        '''
         rowSize = len(triangle)
        
        @cache
        def dfs(row, idx):
            if not idx < len(triangle[row]):
                return float('inf')
            
            if row == rowSize - 1:
                return triangle[row][idx]
            
            choice1 = dfs(row+1, idx) + triangle[row][idx]
            choice2 = dfs(row+1, idx + 1) + triangle[row][idx]
            
            return min(choice1, choice2)
        return dfs(0,0)
        
        '''
        dp = [[0 for _ in range(len(triangle[idx]))] for idx in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        
        for rowind in range(1, len(dp)):
            row = dp[rowind]
            for idx in range(len(row)):
                if idx == 0: 
                    dp[rowind][idx] = triangle[rowind][idx]+dp[rowind-1][idx]
                elif idx == len(row)-1:
                    dp[rowind][idx] = triangle[rowind][idx] + dp[rowind-1][idx-1]
                else:
                    dp[rowind][idx] = triangle[rowind][idx]+ min(dp[rowind-1][idx], dp[rowind-1][idx-1])
        return min(dp[-1])
    # time comp O(m*n)
    # space comp O(m*n)