class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []
        min_leng = self.smallest(strs)
       
        for i in range(min_leng):
            check = strs[0][:i+1]
            for word in strs:
                if not word.startswith(check):
                    return prefix[-1] if prefix else ""
            prefix.append(check)
        return prefix[-1] if prefix else ""
                    
    def smallest(self, strs):
        min_leng = 201
        for word in strs:
            min_leng = min(min_leng, len(word))
        return min_leng
        
        