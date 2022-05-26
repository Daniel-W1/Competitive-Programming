class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ans = {}
        for i,row in enumerate(board):
            for j,val in enumerate(row):
                live_count = 0
                dead_count = 0
                neighbours = [(a,b) for a in range(i-1,i+2) for b in range(j-1,j+2) if a >= 0 and a < len(board) and b >= 0 and b < len(board[0])]
                for inds in neighbours:
                    if inds == (i,j): continue
                    a,b = inds
                    if board[a][b] == 1:
                        live_count += 1
                    else:
                        dead_count += 1
                if val == 1:
                    if live_count < 2:
                        ans[i,j] = 0
                    elif live_count == 2 or live_count == 3:
                        ans[i,j] = 1
                    elif live_count > 3:
                        ans[i,j] = 0
                else:
                    if live_count == 3:
                        ans[i,j] = 1
        for keys in ans:
            i,j = keys
            board[i][j] = ans[keys]
        
                
                    
                    
                    
                    
                    
        