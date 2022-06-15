class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        wordset = set(words)
        memo = {}
        
        def recur(word):
            if word not in wordset: return 0
            if word in  memo: return memo[word]
            
            n = len(word)
            the_max= 0
            for i in range(n):
                the_max = max(the_max,recur(word[:i]+word[i+1:])+1)
            memo[word] = the_max
            
            return the_max
        for word in words:
            recur(word)
        return max(memo.values())
            
            
        