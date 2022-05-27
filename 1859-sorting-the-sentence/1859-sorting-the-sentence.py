class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        words.sort(key = lambda word:int(word[-1]))
        for i, word in enumerate(words):
            words[i] = word.strip(word[-1])
        return " ".join(words)