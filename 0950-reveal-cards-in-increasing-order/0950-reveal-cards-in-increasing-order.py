class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        """
            17, 13, 11, 2, 3, 5, 7
            
            2, 3, 5, 7, 11, 13, 17
            
            2, 17, 3, 13, 5, 11, 7
            
            11, 17, 13 --> 11, 13, 17
            
            [2, 13, 3, 11 ,5, 17, 7]
            
            [1,4,7,18,22,33,45,55]
            
            [1, 22, 4, 33, 7, 45, 18, 55]
            
            [1,4,7,18,22,33,45,55, 64]
            
            [1,_, 4, 33, 7, _, 18, 45, 22]
        """
        deck.sort()
        cur_idx = 0
        ans = [-1] * len(deck)
        jump = False
        
        while cur_idx < len(deck):
            for idx, val in enumerate(ans):
                if val != -1: continue
                    
                if not jump:
                    ans[idx] = deck[cur_idx]
                    cur_idx += 1
                    
                jump = not jump
            
        return ans
        
        