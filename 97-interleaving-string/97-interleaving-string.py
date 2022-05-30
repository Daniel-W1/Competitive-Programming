class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        def check(i,j,res):
            if (i,j,res) not in memo:
                if i > len(s1)-1 and j > len(s2)-1 or not s3.startswith(res):
                    return res == s3
                if i > len(s1)-1 and j < len(s2):
                    return check(i,j+1,res+s2[j])
                elif i < len(s1) and j > len(s2)-1:
                    return check(i+1,j,res+s1[i])
                else:
                    memo[i,j,res] = check(i+1,j,res+s1[i]) or check(i,j+1,res+s2[j])
            return memo[i,j,res]
        return check(0,0,"")
            
                