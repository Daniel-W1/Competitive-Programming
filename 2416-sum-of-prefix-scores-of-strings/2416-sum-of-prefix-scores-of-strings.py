class TrieNode:
    def __init__(self, val = None):
        self.cnt = 0
        self.children = {}
        self.end = False
        
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        '''
        first because it says prefix and some other thing 
        i am thinking about using a trie somehow to solve the problem
        
        
        let's build the trie for the first input and look what it looks like
        ["abc","ab","bc","b"]
        
        a   b e         [1, 1, 1]
     e b      c e
    e c
    
    what if i give them cnts for each of the letters(node) that are on the trie
    
    what about for other inputs like
    
     ["abc","acb","bc","b"]
     
        a2
       b  c
      c     b
      
      so ya this should work
        '''
        self.root = TrieNode()
        for word in words:
            cur = self.root
            for char in word:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                    
                cur.children[char].cnt += 1
                cur = cur.children[char]
            cur.end = True
        
        # so ya that should build our trie
        # now let's count
        ans = [0]*len(words)
        for idx in range(len(words)):
            res = 0
            cur = self.root
            for char in words[idx]:
                res += cur.children[char].cnt
                cur = cur.children[char]
            
            ans[idx] = res
        return ans
        
        
        
        
                    