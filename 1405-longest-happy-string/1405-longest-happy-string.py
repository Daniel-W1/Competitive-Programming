class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        vals = sorted([[a, "a"], [b, "b"], [c, "c"]])
        ans = ""
        long = False
        while vals[-1][0]:
            if vals[-1][0] > 1:
                if ans and vals[-1][1] == ans[-1]:
                    ans += vals[-1][1]
                    vals[-1][0] -= 1
                else:
                    if ans[-2:] == vals[-1][1]*2:
                        print(True)
                        break
                    if not ans:
                        ans += vals[-1][1]*2
                        vals[-1][0] -= 2
                    elif ans and ans[-1] != vals[-1][1]:
                        ans += vals[-1][1]*2
                        vals[-1][0] -= 2
            else:
                ans += vals[-1][1]
                vals[-1][0] -= 1
                
            if vals[-2][0]:
                ans += vals[-2][1]
                vals[-2][0] -= 1
            vals = sorted(vals)
            if vals[-2][0] == vals[-3][0] == 0 and vals[-1][0] > 1:
                long = True
                break
                                      
        if not long:
            return ans
        else:
            if vals[-1][0] > 1:
                if ans[-2:] != vals[-1][1]*2: return ans + vals[-1][1]*2
                else: return ans
            else: return ans + vals[-1][1]