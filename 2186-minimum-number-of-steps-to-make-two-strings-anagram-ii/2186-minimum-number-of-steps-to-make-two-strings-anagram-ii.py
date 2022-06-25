class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt1 = Counter(s)
        cnt2 = Counter(t)
        steps = 0
        for char in cnt1:
            if cnt1[char] > cnt2.get(char,0):
                steps += (cnt1[char]-cnt2.get(char,0))
            
        for char in cnt2:
            if cnt2[char] > cnt1.get(char,0):
                steps += (cnt2[char]-cnt1.get(char,0))
        return steps
                
                
        
        