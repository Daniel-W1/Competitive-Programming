class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def solve(s,dict):
            if s=="":
                return [[]]
            ans = []
            for word in dict:
                if s.startswith(word):
                    new= s[len(word):]
                    res= solve(new,dict)
                    for arr in res:
                        arr.append(word)
                        ans.append(arr)
            return ans
        result = solve(s,wordDict)
        return [" ".join(arr[::-1]) for arr in result]