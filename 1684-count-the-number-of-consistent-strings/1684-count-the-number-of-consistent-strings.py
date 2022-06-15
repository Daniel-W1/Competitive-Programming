class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        cnt = 0
        for word in words:
            word = set(word)
            check = True
            for letter in word:
                if letter not in allowed:
                    check = False
                    break
            if check: cnt += 1
        return cnt
                