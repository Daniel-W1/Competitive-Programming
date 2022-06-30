class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # this is the same us finding the longest common number subsequence
        n,m = len(nums1)-1, len(nums2)-1
        def LCNS(i,j,memo = {}):
            if (i,j) in memo: return memo[i,j]
            if i > n or j > m:
                return 0
            if nums1[i] == nums2[j]:
                memo[i,j] = 1 + LCNS(i+1,j+1)
                return memo[i,j]
            memo[i,j] = max(LCNS(i,j+1),LCNS(i+1,j))
            return memo[i,j]
        return LCNS(0,0)