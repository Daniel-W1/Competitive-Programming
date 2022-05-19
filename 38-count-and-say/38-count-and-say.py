class Solution:
    def countAndSay(self, n: int) -> str:
        # ans = "1"
        # for _ in range(1, n):
        #     i = 0
        #     newans = ""
        #     cnt = 0
        #     while i < len(ans):
        #         num = ans[i]
        #         cnt += 1
        #         i += 1
        #         while i < len(ans) and ans[i] == num:
        #             cnt += 1
        #             i += 1
        #         newans += str(cnt) + num
        #         cnt = 0
        #     ans = newans
        # return ans
        # well the above is an easy iterative solution to this problem, now let's do the
        # recursive one and we will be good to go
        def realcount(val, ans):
            if val == n:
                return ans
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
            return realcount(val+1,ans)
        return realcount(1,"1")
                
            
            
                
                
                