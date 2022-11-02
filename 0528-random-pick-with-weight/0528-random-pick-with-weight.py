class Solution:

    def __init__(self, w: List[int]):
        self.psums = list(accumulate(w))

    def pickIndex(self) -> int:
        total = self.psums[-1]
        randomnum = randint(1, total)
        
        idx = bisect_left(self.psums, randomnum)
        
        return idx if idx < len(self.psums) else idx - 1
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()