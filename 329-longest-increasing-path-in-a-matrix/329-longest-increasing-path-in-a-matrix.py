class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # it says longest increasing path
        '''
        so i think the right way to do this is just to write dfs
        and memoise on the way
        
        and also memoise globally and use that memo for each row and col 
        
        '''
        m, n = len(matrix), len(matrix[0])
        memo = {}
        directions = [(1, 0), (-1, 0), (0, -1), (0,1)]
        
        def dfs(row, col):
            if (row, col) in memo: return memo[row, col]
            res = 1
            for dx, dy in directions:
                newr, newc = row + dx, col + dy
                if 0 <= newr < m and 0 <= newc < n:
                    if matrix[newr][newc] > matrix[row][col]:
                        res = max(res, dfs(newr, newc)+1)
            memo[row, col] = res
            return res
        
        return max(dfs(i, j) for i, j in product(range(m), range(n)))