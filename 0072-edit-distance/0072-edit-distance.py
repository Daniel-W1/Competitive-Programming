class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        
        @cache
        def dfs(idx1, idx2):
            
            # base cases
            if idx1 >= len(word1):
                return len(word2) - idx2
            
            if idx2 >= len(word2):
                return len(word1) - idx1
            
            # if they are the same good
            if word1[idx1] == word2[idx2]:
                return dfs(idx1+1, idx2 + 1)
            
            # if they are not the same, insert
            choice1 = dfs(idx1, idx2 + 1) + 1
            
            # delete
            choice2 = dfs(idx1 + 1, idx2) + 1
            
            # replace
            choice3 = dfs(idx1+1, idx2 + 1) + 1
            
            return min(choice1, choice2, choice3)
        
        return dfs(0, 0)
            