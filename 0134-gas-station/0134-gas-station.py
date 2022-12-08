class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        gas += gas
        n = len(gas)
        
        left = 0
        cur = 0
        
        # print(gas)
        for right in range(n):
            cur += gas[right] - cost[right % (n//2)]
            
            if cur < 0:
                left = right + 1
                cur = 0
                
            elif right - left + 1 == n//2:
                return left
            # print(cur, "second")
        return -1
                