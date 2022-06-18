class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.end = True
    def search(self, word: str) -> bool:
        # now what makes this difficult is the . so we need to do 
        # soem dfs when it comes to the nodes
        self.ans = False
        node = self.root
        self.dfs_search(node,word)
        return self.ans
    def dfs_search(self,node, word):
        if not word:
            if node.end:
                self.ans = True
            return
        if word[0] == ".":
            for n in node.children.values():
                self.dfs_search(n,word[1:])
        if word[0] in node.children:
            n = node.children[word[0]]
            self.dfs_search(n,word[1:])
        return


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# def dfs(self, node, word):
#         if not word:
#             if node.isWord:
#                 self.res = True
#             return 
#         if word[0] == ".":
#             for n in node.children.values():
#                 self.dfs(n, word[1:])
#         else:
#             node = node.children.get(word[0])
#             if not node:
#                 return 
#             self.dfs(node, word[1:])