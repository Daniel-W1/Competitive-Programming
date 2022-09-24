class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        so this is a normal dfs implementation problem but i which can be done in N^3 time but here we will do it in n^2 time too
        
        we need a visited set because we are also considering cells with the same heights
        '''
        directions = [(1, 0), (0, 1), (-1, 0),(0, -1)]
        m, n = len(heights), len(heights[0])

        
        
        def dfs(i, j, visited):
            nonlocal check1, check2
            
            visited.add((i,j))
            
            for dx, dy in directions:
                newr, newc = i + dx, j + dy
                if 0 <= newr < m and 0 <= newc < n:
                    if (newr, newc) not in visited:
                        if heights[newr][newc] <= heights[i][j]:
                            dfs(newr, newc, visited)
                else:
                    if newr == m  or newc == n:
                        check1 = True
                    if newc == -1 or newr == -1:
                        check2 = True
        ans = []
        
        for row in range(m):
            for col in range(n):
                
                check1, check2 = False, False
                dfs(row, col, set())
                
                if check1 and check2:
                    ans.append([row, col])
        return ans
                    
                        
                            
                