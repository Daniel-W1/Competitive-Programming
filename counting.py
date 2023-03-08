class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words: count += word.startswith(pref)
            
            
        return count
