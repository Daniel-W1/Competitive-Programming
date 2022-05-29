class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)-1
        n = len(board[0])-1
        used = {}
        def findword(a,b,i):
            if i == len(word):
                return True
            if a > m or b > n or a < 0 or b < 0 or (a,b) in used:
                return False
            if word[i] != board[a][b]:
                return False
            used[a,b] = True
            res =  findword(a+1,b,i+1) or findword(a,b+1,i+1) or findword(a-1,b,i+1) or findword(a,b-1,i+1)
            del used[a,b]
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    check = findword(i,j,0)
                    if check:
                        return True
        return False