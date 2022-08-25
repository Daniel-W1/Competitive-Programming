class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        breaker = "a"
        for idx, letter in enumerate(palindrome):
            if letter > breaker:
                word = palindrome[:idx] + breaker + palindrome[idx+1:]
                if not (len(word)%2 and idx == len(word)//2):
                    return word
        breaker = chr(ord(breaker)+1)
        word = palindrome[:-1] + breaker
        
        return word
        '''
        aabaa
        '''
        # time O(n), space O(n)
    