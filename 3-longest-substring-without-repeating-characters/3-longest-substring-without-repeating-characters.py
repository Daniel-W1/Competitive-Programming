class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
#         charset=set()
#         l=0
#         res=0
        
#         for h in range(len(s)):
#             while s[h] in charset:
#                 charset.remove(s[l])
#                 l += 1
#             charset.add(s[h])
#             res= max(res, h-l +1)
#         return res
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = ''
        mx = 0
        for i in s:
            while i in stack:
                stack = stack[1:]
            stack += i
            mx = mx  if mx > len(stack) else len(stack)
        return mx
        
                
            
        