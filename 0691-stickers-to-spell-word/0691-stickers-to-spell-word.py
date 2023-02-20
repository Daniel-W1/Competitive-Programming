class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        
        
        # so it's easy to check impossible cases
        
        # dp ?
        
        
        # i know how many times i should repeat a word 
        
        # definitely a dp with messy implementation
        
        # state can be the target string
        
        # base case is when it becomes empty
        
        # all choices 
        
        # iterate through the words, then again iterate through the max times to use that word
        all_chars = set("".join(stickers))
        for char in target:
            if char not in all_chars:
                return -1
            
        n = len(stickers)
        cnts = [Counter(word) for word in stickers]
        
        cnts
        
        @cache
        def dp(word):
            if not word:
                return 0
            
            cur_cnt = Counter(word)
            res = float('inf')
            
            for idx, sticker in enumerate(stickers):
                the_max = 0
                cnt = cnts[idx]
                for char in sticker:
                    if char in cur_cnt:
                        the_max = max(ceil(cur_cnt[char]/cnt[char]), the_max)
            
            
                
                for word_use in range(1,the_max + 1):
                    new_word = [char * max(0, cur_cnt[char] - word_use*cnt[char]) for char in cur_cnt]
                    
                    # print(new_word, "here", word_use)
                    
                    new_word = "".join(new_word)
                
                    res = min(res, dp(new_word) + word_use)
            
            return res
    
        return dp(target) 
            
            
                    
                
        
        