class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = [float('inf')]*len(s)
        
        for i in range(len(s)):
            if s[i] == c:
                ans[i] = 0
        for i,val in enumerate(ans):
            if val == 0:
                l,h = i-1,i+1
                cnt = 1
                while l >= 0 or h < len(s):
                    if l >= 0 and ans[l] == 0:
                        l = -1
                    if h < len(s) and ans[h] == 0:
                        h = len(s)
                    if l >= 0:
                        ans[l] = cnt if cnt<ans[l] else ans[l]
                    if h < len(s):
                        ans[h] = cnt if cnt<ans[h]  else ans[h]
                    cnt += 1
                    l -= 1
                    h += 1
        return ans
                    
                        
            
            
        