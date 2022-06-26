class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        def dfs(i,j,visited):
            if (i,j) in visited:
                return
            if i < 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1:
                return
            if board[i][j] == "X":
                return
            visited.add((i,j))
            dfs(i+1,j,visited)
            dfs(i-1,j,visited)
            dfs(i,j+1,visited)
            dfs(i,j-1,visited)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or j == 0 or i == len(board)-1 or j == len(board[0])-1) and board[i][j] == "O":
                    dfs(i,j,visited)
        def dfs_mark(i,j,visited):
            if (i,j) in visited:
                return
            if i < 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1:
                return
            if board[i][j] == "X":
                return
            board[i][j] = "X"
            visited.add((i,j))
            dfs_mark(i+1,j,visited)
            dfs_mark(i-1,j,visited)
            dfs_mark(i,j+1,visited)
            dfs_mark(i,j-1,visited)
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i,j) not in visited and board[i][j] == "O":
                    dfs_mark(i,j,visited)
        
        
        return board