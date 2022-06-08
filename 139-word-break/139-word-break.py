class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         def sol(s,dict,memo):
#             if s in memo: return memo[s]
#             if s == "": return True

#             for word in wordDict:
#                 if s.startswith(word):
#                     new_s = s[len(word):]
#                     if sol(new_s, wordDict,memo):
#                         memo[s] = True
#                         return True
#             memo[s] = False
#             return False
#         return sol(s,wordDict,{})
        # now let's solve the same problem bottom up.
        table = [False]*(len(s)+1)
        table[0] = True
        
        for i in range(len(table)):
            if table[i]:
                for word in wordDict:
                    if s[i:].startswith(word):
                        new_index = i+len(word)
                        if new_index < len(table):
                            table[new_index] = True
        return table[len(s)]
                
    