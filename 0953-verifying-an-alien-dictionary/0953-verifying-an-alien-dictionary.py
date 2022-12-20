class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        idx_map = {char : idx for idx, char in enumerate(order)}
        
        n = len(words)
        
        for idx in range(n-1):
            i, j = 0, 0
            while i < len(words[idx]) and j < len(words[idx+1]):
                if words[idx][i] != words[idx+1][j]:
                    check = idx_map[words[idx][i]] < idx_map[words[idx+1][j]]
                    
                    if not check: 
                        return False
                    
                    break
                    
                j += 1
                i += 1
            
            if j == len(words[idx+1]) and i < len(words[idx]):
                return False
        
        return True