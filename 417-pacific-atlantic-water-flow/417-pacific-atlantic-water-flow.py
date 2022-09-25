class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        so this is a normal dfs implementation problem but i which can be done in N^3 time but here we will do it in n^2 time too
        
        we need a visited set because we are also considering cells with the same heights
        '''
#         directions = [(1, 0), (0, 1), (-1, 0),(0, -1)]
#         m, n = len(heights), len(heights[0])

        

#         def dfs(i, j, visited):
#             nonlocal check1, check2
            
#             visited.add((i,j))
            
#             for dx, dy in directions:
#                 newr, newc = i + dx, j + dy
#                 if 0 <= newr < m and 0 <= newc < n:
#                     if (newr, newc) not in visited:
#                         if heights[newr][newc] <= heights[i][j]:
#                             dfs(newr, newc, visited)
#                 else:
#                     if newr == m  or newc == n:
#                         check1 = True
#                     if newc == -1 or newr == -1:
#                         check2 = True
#         ans = []
        
#         for row in range(m):
#             for col in range(n):
                
#                 check1, check2 = False, False
#                 dfs(row, col, set())
                
#                 if check1 and check2:
#                     ans.append([row, col])
#         return ans
    
#         # time comp is N^3 and space comp N^2 recursion stack
        '''
        this sol is very slow so how can we make it efficient
        
        I think we need to work on the efficiency of the sol
        
        we can dfs from the left and the right and record the pos that we see
        '''
        m, n = len(heights), len(heights[0])
        directions = [(1, 0), (0, 1), (-1, 0),(0, -1)]

        def dfs(i, j, seen):
            seen.add((i,j))
            for dx, dy in directions:
                newr, newc = i + dx, j + dy
                if 0 <= newr < m and 0 <= newc < n:
                    if (newr, newc) not in seen:
                        if heights[newr][newc] >= heights[i][j]:
                            dfs(newr, newc, seen)
        
        # first let's go through the rows
        pacific, atlantic = set(), set()
        for idx in range(m):
            dfs(idx, 0, pacific)
            dfs(idx, n-1, atlantic)
        
        # first let's go through the cols
        for idx in range(n):
            dfs(0, idx, pacific)
            dfs(m-1, idx, atlantic)
        
        both = pacific & atlantic
        return [[row, col] for row, col in both]
            
        
        
                        
                            
                