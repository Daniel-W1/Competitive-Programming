class trienode:
    def __init__(self):
        self.children = {}
class trie:
    def __init__(self):
        self.root = trienode()
        self.ends = []
    def insert(self,word):
        root = self.root
        for i in range(len(word)-1,-1,-1):
            if word[i] not in root.children:
                root.children[word[i]] = trienode()
            root = root.children[word[i]]
        self.ends.append((root,len(word)+1))

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))
        t = trie()
        
        for w in words:
            t.insert(w)
        
        return sum([depth for node,depth in t.ends if len(node.children)==0])
            