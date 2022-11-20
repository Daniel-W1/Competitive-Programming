class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        '''
        [[1, 2], [2, 3], []]
        
        
        need to check if i already has the first two elements or not
        after that the whole thing is kinda forced to go in one direction
        '''
        n = len(arr)
        nums = set(arr)
        
        def findlen(num1, num2):
            cur = 2
            while num1 + num2 in nums:
                cur += 1
                num1, num2 = num2, num1 + num2
            return cur
        
        answer = 0
        for idx in range(n):
            for idx2 in range(idx + 1, n):
                answer = max(answer, findlen(arr[idx], arr[idx2]))
        
        return answer if answer > 2 else 0