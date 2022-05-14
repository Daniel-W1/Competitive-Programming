class Solution:
    def countVowels(self, s: str) -> int:
        # prefix = [0]*len(word)
        # vowels = "aeiou"
        # prev = 0
        # for i,letter in enumerate(word):
        #     if letter in vowels:
        #         prefix[i] = prev + 1
        #     else:
        #         prefix[i] = prev
        #     prev = prefix[i]
        # total = sum(prefix)
        # ans = 0
        # prev = 0
        # for i, val in enumerate(prefix):
        #     ans += total - prev*(len(prefix)-i)
        #     total -= prefix[i]
        #     prev = prefix[i]
        # return ans
        return sum((i + 1) * (len(s) - i) for i, c in enumerate(s) if c in 'aeiou')
    
            
        
    
    
        
            
        