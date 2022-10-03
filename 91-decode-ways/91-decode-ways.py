class Solution:
    def numDecodings(self, s: str) -> int:
            
    
        dp = [0]*(len(s)+1)
        dp[-1] = 1

        for i in range(len(s)-1,-1,-1):
            if s[i] == "0":
                continue

            if i+1<len(s) and int(s[i]+s[i+1])<27:
                dp[i] += dp[i+2]
            dp[i]+=dp[i+1]


        return dp[0]

#             '''
#             226
#             [1, 2, 3]

#             1111
#         [1, 2, 3,]
        
#         at each index their are choices i need to make for example 
#         if the cur num is 1 we definetly have two choices 
        
#         if the cur is 2 and the next is <= 6 we will have two choices
        
#         else we only have on choices
        
        
#         that makes sense but how are u going to handle the 0s
        
#         if we find a zero we will look at the value we get before 0 and 
#         if that value with 0 gives us a valid thing then the whole thing 
#         must be valid
        
#         my state is one and time comp 2^n am making 2 decision at each index
#         O(N)
        
#         @cache
#         def dfs(idx):
#             if idx >= len(s): return 1
            
#             if s[idx] == "1" and idx + 1 < len(s):
#                 return dfs(idx + 1) + dfs(idx + 2)
            
#             elif s[idx] == "2" and idx + 1 < len(s) and int(s[idx+1]) <= 6:
#                 return dfs(idx + 1) + dfs(idx + 2)
        
#             elif int(s[idx]) >= 1:
#                 return dfs(idx+1)  
#             else:
#                 return 0
#         return dfs(0)
        
#         '''
        
#         # time comp is O(n) and space comp is O(n)
#         # so how are u going to change this in to bottom up 
#         # may be even some space optimisation
#         '''
#         "226"
#         [3,2,1]
        
#         1111
#         [1,3,2,1]
        
#         1234
#         [3,2,1,1]
#         '''
# #         dp = [0, 0, 1]
# #         if s[-1] != "0": dp[1] = 1
        
# #         for idx in range(len(s)-2, -1, -1):
# #             if s[idx] == "0":
# #                 dp[0] = 0
                
# #             elif s[idx] == "1":
# #                 dp[0] = dp[1] + dp[2]
                
# #             elif s[idx] == "2" and int(s[idx+1]) <= 6:
# #                 dp[0] = dp[1] + dp[2]
# #             else:
# #                 dp[0] = dp[1]
            
# #             dp[0], dp[1], dp[2] = 0, dp[0], dp[1]
# #         # print(dp)
# #         return dp[1]
    
#         '''
#         so can u optimise the space even more ?
        
#         ya as we can see we are only looking at the last element parts
#         so i think I can do that
#         '''
        