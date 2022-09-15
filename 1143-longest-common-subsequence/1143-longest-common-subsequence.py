class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @cache
        def find(pointer1, pointer2):
            if pointer1 == -1 or pointer2 == -1: return 0
            
            elif text1[pointer1] == text2[pointer2]:
                return 1 + find(pointer1-1, pointer2-1)
            else:
                return max(find(pointer1-1, pointer2), find(pointer1, pointer2-1))
            
        return find(len(text1)-1, len(text2)-1)