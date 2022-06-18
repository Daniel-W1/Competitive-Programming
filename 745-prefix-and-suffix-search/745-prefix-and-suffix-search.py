class WordFilter:
    def __init__(self, words):
        self.d = {}
        for i, word in enumerate(words):
            for p, s in product(range(len(word) + 1), repeat=2):
                self.d[word[:p], word[s:]] = i

    def f(self, prefix, suffix):
        return self.d.get((prefix, suffix), -1)