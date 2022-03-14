class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = list(range(1, n+1))
        pos = 0
        num = len(players)
        
        def mywinner(players, k, pos, num):
            if num == 1:
                return players[pos]
            count = 0
            
            while count < (k):
                if pos == len(players): pos = 0
                if players[pos] == 0: 
                    pos += 1
                    continue
                else: 
                    pos += 1
                    count += 1
            players[pos-1] = 0
            
            if pos >= len(players): pos = 0
            while players[pos] == 0:
                pos += 1
                if pos == len(players):
                    pos = 0
            num -= 1
            
            return mywinner(players, k, pos, num)
        
        return mywinner(players, k, pos, num)
            
                
            
            
        
            
            
            
            
            
        
        