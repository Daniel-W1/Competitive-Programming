class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
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