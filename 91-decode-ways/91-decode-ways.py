class Solution:
    def numDecodings(self, s: str) -> int:
        possible_range = range(1, 27)
        memo = {}
        def decode(i,cur):
            if (cur,len(s)-i - 1) not in memo:
                if i == len(s)-1 and int(cur) in possible_range:
                    return 1
                if int(cur) not in possible_range:
                    return 0
                if int(cur) in possible_range:
                    memo[cur, len(s)-i-1] = decode(i+1, s[i+1]) + decode(i+1,cur+s[i+1])
            return memo[cur,len(s)-i-1]
            
        return decode(0,s[0])
            