class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        path = []
        
        def backtrack(idx, cur, cnt):
            if idx == n:
                if path.count(".") == 3:
                    ans.append("".join(list(path)))
                return 
            # there are two choices 
            # add if cur != 0 or cur + s[idx] <= 255
            
            if not cur or (cur[0] != "0" and int(cur + s[idx]) <= 255):
                path.append(s[idx])
                
                backtrack(idx + 1, cur + s[idx], cnt)
                
                path.pop()
            
            if cnt < 3 and cur != "":
                path.append(".")
                backtrack(idx, "", cnt + 1)
                path.pop()
            

        
        backtrack(0, "", 0)
        return ans
            
            