class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        for _ in range(1, n):
            i = 0
            newans = ""
            cnt = 0
            while i < len(ans):
                num = ans[i]
                cnt += 1
                i += 1
                while i < len(ans) and ans[i] == num:
                    cnt += 1
                    i += 1
                newans += str(cnt) + num
                cnt = 0
            ans = newans
        return ans
                    
                
                
                