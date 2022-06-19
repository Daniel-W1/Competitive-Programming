class trienode:
    def __init__(self):
        self.children = {}
        self.end = False
class Solution:
    def __init__(self):
        self.root = trienode()
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        for word in dictionary:
            cur = self.root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = trienode()
                cur = cur.children[char]
            cur.end = True
        res = []
        for word in sentence.split():
            current = ""
            cur = self.root
            for char in word:
                if char not in cur.children or cur.end:
                    break
                current += char
                cur = cur.children[char]
            if current and cur.end:
                res.append(current)
            else:
                res.append(word)
        return " ".join(res)
                