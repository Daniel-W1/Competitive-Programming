class Solution:
    def robotWithString(self, s: str) -> str:
        
        """
            bddabba
            
            01234567
        """
        
        ans = []
        
        prev = []
        
        the_min = "z"
        s += "z"
        min_arr = [None]*len(s)

        # precompute the min at each index
        for idx in range(len(s)-1, -1, -1):
            the_min = min(the_min, s[idx])
            min_arr[idx] = the_min
        
        # print(min_arr)
        ans = []
        for idx, char in enumerate(s):
            while prev and prev[-1] <= min_arr[idx]:
                ans.append(prev.pop())
            
            if s[idx] == min_arr[idx]:
                ans.append(s[idx])
            else:
                prev.append(s[idx])
        
        return "".join(ans[:-1])
            