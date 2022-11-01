class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # this seems like a simulation problem 
        
        # do this for each column
        
        cols = len(grid[0])
        maxdepth = len(grid)
        answer = [0]*cols
        
        for colidx in range(cols):
            curdepth = 0
            curcol = colidx
            
            while curdepth < maxdepth:
                curvalue = grid[curdepth][curcol]
                if curvalue == 1:
                    # check right neighbor
                    if curcol + 1 == cols or grid[curdepth][curcol+1] == -1:
                        answer[colidx] = -1
                        break
                    curcol += 1
                else:
                    if curcol - 1 == -1 or grid[curdepth][curcol-1] == 1:
                        answer[colidx] = -1
                        break
                    curcol -= 1
                    
                curdepth += 1
            
            if answer[colidx] != -1:
                answer[colidx] = curcol
        
        return answer
                