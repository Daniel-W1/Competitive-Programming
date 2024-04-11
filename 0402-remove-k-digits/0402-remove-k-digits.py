class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
            123456 
        """
        q = deque([])
        
        for n in num:
            while q and q[-1] > n and k:
                q.pop()
                k -= 1
            q.append(n)
        
        while q and k:
            q.pop()
            k -= 1
            
        while q and q[0] == "0":
            q.popleft()
            
        return "".join(q) or "0"
            
            