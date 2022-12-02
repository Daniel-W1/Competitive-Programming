class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        """
            [9,9,6,0,6,6,9]
            [1, 2, 1, 0, -1, -2, -1]
        """
        
        prefix = {0 : -1}
        cur_sum = 0
        answer = 0
        
        for idx, num in enumerate(hours):
            cur_sum += 1 if (num > 8) else -1
           
            val = 0 if cur_sum - 1 > 0 else cur_sum - 1
            
            if val in prefix:
                answer = max(answer, idx - prefix[val])
            
            prefix.setdefault(cur_sum, idx)
        
        return answer
                