class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def move(i,j,memo = {}): 
            if (i,j) in memo: return memo[i,j]
            if i > m-1 or j > n-1:
                return 0
            if i == m-1 and j == n-1:
                return 1
            memo[i,j] = move(i+1, j) + move(i,j+1)
            return memo[i,j]
        return move(0,0)
    
    # but this thing need to be memoised 
    # time comp and space comp