class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_pro = 1
        found = False
        for word in words:
            first_word = set(word)
            for another in words:
                if not set(another).intersection(first_word):
                    found = True
                    max_pro = max(max_pro,len(another)*len(word))
        return max_pro if found else 0
                
                
            