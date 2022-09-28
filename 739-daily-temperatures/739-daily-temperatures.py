class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []
        
        for idx in range(len(temperatures)):
            while stack and temperatures[idx]>temperatures[stack[-1]]:
                poped = stack.pop()
                answer[poped] = idx-poped
            stack.append(idx)
            
        return answer