class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        height = len(triangle)-1
        memo = {}
        def minpath(i,j):
            if (i,j) not in memo:
                if i == height:
                    return triangle[i][j]
                memo[i,j] = min(minpath(i+1,j)+triangle[i][j],minpath(i+1,j+1)+triangle[i][j])
            return memo[i,j]
        return minpath(0,0)
        
        