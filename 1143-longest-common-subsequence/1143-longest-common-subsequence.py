class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1)-1,len(text2)-1
        memo = {}
        def findlongest(i,j):
            if (i,j) in memo: return memo[i,j]
            if i > m or j > n:
                return 0
            if text1[i] == text2[j]:
                memo[i,j] = 1 + findlongest(i+1,j+1)
            else:
                memo[i,j] = max(findlongest(i+1,j),findlongest(i,j+1))
            return memo[i,j]
        return findlongest(0,0)