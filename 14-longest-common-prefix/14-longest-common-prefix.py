class trienode:
    def __init__(self):
        self.children = {}
        self.end = False
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        self.root = trienode()
        for word in strs:
            cur = self.root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = trienode()
                cur = cur.children[char]
            cur.end = True
        cur = self.root
        res = ""
        while len(cur.children) == 1 and not cur.end:
            for char in cur.children:
                res += char
            cur = cur.children[char]
        return res
        
                