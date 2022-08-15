class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # so what is the plan?
        # when u find E backtrack and find all the others
        # if some numbers put is and don't do anything
        
        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        
        directions = [(1,0),(0,1),(1,1),(-1,-1),(-1,0),(0,-1),(1,-1),(-1,1)]
        def dfs(r,c,visited):
            if board[r][c] != "E":
                return
            
            mineCount = 0
        
            for dir in directions:
                i,j = dir
                new_r, new_c = r+i, c+j
                
                if  (new_r >= 0 and new_r < len(board)) and (new_c >= 0 and new_c < len(board[0])):
                    mineCount = mineCount + 1 if board[new_r][new_c] == "M" else mineCount
                    
            board[r][c] = str(mineCount) if mineCount > 0 else "B"
            
            if mineCount == 0:
                for dir in directions:
                    i,j = dir
                    new_r, new_c = r+i, c+j

                    if  (new_r >= 0 and new_r < len(board)) and (new_c >= 0 and new_c < len(board[0])) and board[new_r][new_c] != "M":  
                        dfs(new_r, new_c, visited)
       
        dfs(r,c, set())
    
        return board
                    
    #
            