class Solution:
    def ladderLength(self, start: str, end: str, words: List[str]) -> int:
        words = set(words)
        letters = string.ascii_lowercase
        
        def findall(word):
            ans = []
            for i, letter in enumerate(word):
                for char in letters:
                    string = word[:i]+char+word[i+1:]
                    if string in words:
                        ans.append(string)
                        words.remove(string)
            return ans
        
        q = collections.deque([start])
        moves = 1
        
        while q:
            cur = len(q)
            for _ in range(cur):
                word = q.popleft()
                if word == end:
                    return moves
                
                res = findall(word)
                q += res
            moves += 1
        return 0
                    
                
                
            