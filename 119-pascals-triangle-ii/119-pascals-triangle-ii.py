class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 2:
            return [1]*(rowIndex+1)
        ans = [1,1]
        for _ in range(1,rowIndex):
            new = []
            for ind in range(0,len(ans)-1):
                new.append(ans[ind]+ans[ind+1])
            ans = [1]+new+[1]
        return ans
            
            