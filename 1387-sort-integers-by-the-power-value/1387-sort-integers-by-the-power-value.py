class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        def getSteps(num):
            steps = 0
            while num != 1:
                if num & 1:
                    num = 3*num + 1
                else:
                    num //= 2
                steps += 1
            return steps
        
        
        answer = []
        for num in range(lo, hi+1):
            answer.append((getSteps(num), num))
        
        answer.sort()
        # print(answer)
        return answer[k-1][1]