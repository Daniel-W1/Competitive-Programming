class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        @cache
        def getSteps(num):
            if num == 1: return 0
            if num & 1:
                return getSteps(3*num + 1) + 1
            else:
                return getSteps(num//2) + 1
        
        
        answer = []
        for num in range(lo, hi+1):
            answer.append((getSteps(num), num))
        
        answer.sort()
        return answer[k-1][1]