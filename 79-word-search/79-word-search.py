class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        counts = Counter(sum(board, []))
        
        if counts[word[0]] > counts[word[-1]]:
            word = word[::-1]
            
        word_counts = collections.Counter(word)
        
        for c, count in word_counts.items():
            if counts[c] < count:
                return False
            
        directions = (
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        )
        
        visiting = [[False]*len(board[0]) for _ in range(len(board))]
        
        def in_bounds(i,j):
            return i < len(board) and j < len(board[0]) and i >= 0 and j >= 0
        
        def backtrack(curr, i, j):
            # print(curr)
            visiting[i][j] = True
            if curr == word:
                return True
            
            target_char = word[len(curr)]
            for d in directions:
                di, dj = d[0] + i, d[1] + j
                if in_bounds(di,dj) and not visiting[di][dj] and board[di][dj] == target_char:
                    if backtrack(curr + board[di][dj], di, dj):
                        return True
                                
            visiting[i][j] = False
            return False
            
        
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] == word[0]:
                    if backtrack(word[0], y, x):
                        return True
        return False