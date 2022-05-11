class Solution:
    def countBits(self, n: int) -> List[int]:
        def findones(n):
            cnt = 0
            while n:
                if n%2 == 1:
                    cnt += 1
                n //= 2
            return cnt
        arr = [i for i in range(n+1)]
        ans = []
        for val in arr:
            ans.append(findones(val))
        return ans
    
            