class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        words = set(bank)
        letters = "ACGT"
        def findall(word):
            ans = []
            for i, letter in enumerate(word):
                for char in letters:
                    string = word[:i]+char+word[i+1:]
                    if string in words:
                        words.remove(string)
                        ans.append(string)
            return ans
        
        q = collections.deque([start])
        moves = 0
        while q:
            cur = len(q)
            for _ in range(cur):
                word = q.popleft()
                if word == end:
                    return moves
                
                res = findall(word)
                if res:
                    q += res
            moves += 1
        return -1
                