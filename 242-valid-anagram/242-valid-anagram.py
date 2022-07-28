class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = Counter(s)
        if len(s) != len(t):
            return False
        
        for letter in t:
            if letter in s and count[letter]:
                count[letter] -= 1
            else:
                return False
        return True