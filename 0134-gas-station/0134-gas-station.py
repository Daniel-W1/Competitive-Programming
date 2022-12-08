class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        left = 0
        cur = 0
        
        # print(gas)
        for right in range(2*n):
            cur += gas[right % (n)] - cost[right % (n)]
            
            if cur < 0:
                left = right + 1
                cur = 0
                
            elif right - left + 1 == n:
                return left
            # print(cur, "second")
        return -1
                