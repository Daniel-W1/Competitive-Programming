class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        words = set(bank)
        letters = "ACGT"
        def check(start, end):
            if start == end:
                return 0
            ans = float('inf')
            for index, letter in enumerate(start):
                for char in letters:
                    string = start[:index] + char + start[index+1:]
                    if string in words:
                        words.remove(string)
                        res = check(string, end) + 1
                        words.add(string)
                        ans = min(ans, res)
            return ans
        ans = check(start, end) 
        return ans if ans < float('inf') else -1
                            
                        
            